# Arma los assets para redes: portada + capturas recortadas 4:5 (1080x1350).
from PIL import Image, ImageDraw, ImageFont
import os

BASE = r"C:\Users\Luchi$\Desktop\PROYECTOS\pedidos-demo\assets"
SOC = os.path.join(BASE, "social")
os.makedirs(SOC, exist_ok=True)
W, H = 1080, 1350

# ── Portada (slide 1 del carrusel) ──
portada = Image.new("RGB", (W, H))
d = ImageDraw.Draw(portada)
# gradiente vertical navy → violeta oscuro
for y in range(H):
    t = y / H
    r = int(15 + (30 - 15) * t)
    g = int(23 + (27 - 23) * t)
    b = int(42 + (94 - 42) * t)
    d.line([(0, y), (W, y)], fill=(r, g, b))
# logo (con transparencia)
icono = Image.open(os.path.join(BASE, "logo-icono-512.png")).convert("RGBA")
icono = icono.resize((420, 420), Image.LANCZOS)
portada.paste(icono, ((W - 420) // 2, 260), icono)
# textos
fuente_grande = os.path.join(r"C:\Windows\Fonts", "arialbd.ttf")
fuente_chica = os.path.join(r"C:\Windows\Fonts", "arial.ttf")
f1 = ImageFont.truetype(fuente_grande, 130)
f2 = ImageFont.truetype(fuente_grande, 46)
f3 = ImageFont.truetype(fuente_chica, 40)
d.text(((W) / 2, 760), "Abastece", font=f1, fill=(255, 255, 255), anchor="mm")
d.text((W / 2, 870), "PEDIDOS ONLINE PARA TU COMERCIO", font=f2, fill=(196, 181, 253), anchor="mm")
d.text((W / 2, 1230), "Demo gratuita: lucianog13.github.io/abastece-demo", font=f3, fill=(148, 163, 184), anchor="mm")
portada.save(os.path.join(SOC, "00-portada.png"))

# ── Recortes 4:5 de las capturas ──
for name in ["01-catalogo", "02-carrito", "03-checkout", "04-pedido-enviado"]:
    img = Image.open(os.path.join(BASE, "capturas", name + ".png")).convert("RGB")
    if img.size != (1080, 2400):
        img = img.resize((1080, 2400), Image.LANCZOS)
    crop = img.crop((0, 0, 1080, 1350))
    crop.save(os.path.join(SOC, name + "-45.png"))
    print("ok:", name, crop.size)
print("portada lista")
