# Abastece — Demo

App de pedidos online para comercios (distribuidoras, mayoristas, tiendas).

> **Esta es una DEMO**: el catálogo es ficticio y no hay base de datos conectada.
> Los pedidos se guardan en el dispositivo y salen por WhatsApp.

## Qué hace

- Catálogo con búsqueda, categorías, promos y selector de sabores.
- Carrito con pedido mínimo y control de envases retornables.
- Checkout con datos del cliente y "repetir último pedido".
- Pedido que se envía por WhatsApp o se imprime como remito.
- Panel de administración incluido en el código (se activa con la base de datos).

## Probar

https://lucianog13.github.io/abastece-demo/

## Para ponerla en producción

1. Completar `js/config.js` con el proyecto Supabase del comercio (tablas `productos`, `pedidos`, `clientes`).
2. Cargar el catálogo real (desde la nube o en `js/data/products.js`).
3. Personalizar nombre, logo, WhatsApp y zonas en `js/app.js`, `js/core/order.js`, `js/ui/checkout.js` y `js/data/zonas.js`.

---

Producto de **[Vértice](https://lucianog13.github.io/portfolio/)** — IA . AUTOMATIZACIÓN . SaaS
