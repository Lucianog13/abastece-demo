# Captura las pantallas clave de Abastece (catálogo, carrito, checkout, pedido)
# con Chrome headless + CDP. Guarda PNGs 1080x2400 (viewport movil dsf 3).
import json, subprocess, time, urllib.request, base64, os
import websocket

PORT = 9333
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
DIR = r"C:\Users\Luchi$\Desktop\PROYECTOS\pedidos-demo\assets\capturas"
os.makedirs(DIR, exist_ok=True)

subprocess.Popen(
    [CHROME, "--headless=new", f"--remote-debugging-port={PORT}",
     "--user-data-dir=C:/Users/Luchi$/AppData/Local/Temp/abastece-cdp",
     "--window-size=360,800", "--force-device-scale-factor=3",
     "--hide-scrollbars", "about:blank"],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(3)

tabs = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json/list").read())
ws_url = [t for t in tabs if t["type"] == "page"][0]["webSocketDebuggerUrl"]
ws = websocket.create_connection(ws_url, timeout=30)

_counter = {"n": 1}

def cmd(method, params=None):
    _counter["n"] += 1
    mid = _counter["n"]
    ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
    while True:
        m = json.loads(ws.recv())
        if m.get("id") == mid:
            return m.get("result"), m.get("error")

def evaljs(expr):
    r, e = cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True})
    return (r or {}).get("result", {}).get("value") if r else None

def shot(path):
    r, e = cmd("Page.captureScreenshot", {"format": "png"})
    with open(path, "wb") as f:
        f.write(base64.b64decode(r["data"]))
    print("  shot:", os.path.basename(path), os.path.getsize(path), "bytes")

def wait_for(expr, timeout=15):
    t0 = time.time()
    while time.time() - t0 < timeout:
        if evaljs(expr):
            return True
        time.sleep(0.5)
    return False

cmd("Page.enable")
cmd("Runtime.enable")
cmd("Page.navigate", {"url": "https://lucianog13.github.io/abastece-demo/"})

ok = wait_for("[...document.querySelectorAll('.grilla button')].some(b => b.textContent.includes('Agregar'))", 20)
print("catalogo cargado:", ok)

# ── 1. Catálogo (con promos) ──
shot(os.path.join(DIR, "01-catalogo.png"))

# ── 2. Agregar varios productos sin sabores y abrir carrito ──
evaljs("[...document.querySelectorAll('[data-accion=\"agregar\"]')].slice(0, 10).forEach(b => b.click())")
time.sleep(0.8)
print("carrito contador:", evaljs("document.getElementById('contador-carrito').textContent"))
evaljs("document.getElementById('btn-carrito').click()")
wait_for("!document.getElementById('vista-carrito').hidden && document.querySelectorAll('#items-carrito .item, #items-carrito [data-id]').length > 0", 10)
time.sleep(0.5)
shot(os.path.join(DIR, "02-carrito.png"))

# ── 3. Checkout con datos de ejemplo ──
evaljs("document.getElementById('btn-confirmar').click()")
wait_for("!document.getElementById('vista-checkout').hidden", 10)
evaljs("""
(() => {
  const form = document.getElementById('form-cliente');
  const inputs = [...form.querySelectorAll('input')];
  const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
  inputs.forEach((el) => {
    let v = 'Juan Pérez';
    if (/direc/i.test(el.placeholder || '')) v = 'Av. Siempre Viva 742';
    else if (/tel|num|whatsapp/i.test(el.placeholder || '')) v = '3434123456';
    else if (/nota|obs/i.test(el.placeholder || '')) v = '';
    setter.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  });
})()
""")
time.sleep(0.5)
shot(os.path.join(DIR, "03-checkout.png"))

# ── 4. Generar pedido → vista de pedido final ──
evaljs("document.getElementById('btn-generar').click()")
wait_for("!document.getElementById('vista-pedido').hidden", 10)
time.sleep(0.8)
txt = evaljs("document.body.innerText.slice(0, 400)")
print("estado final (primeros 300):", (txt or "")[:300].replace(chr(10), " | "))
shot(os.path.join(DIR, "04-pedido-enviado.png"))

ws.close()
print("listo.")
