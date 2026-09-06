// Overlay de sabores — DEMO de Abastece.
// Productos de ejemplo con variedades para mostrar el selector de sabores.
(function (root) {
  "use strict";
  root.SABORES_OVERLAY = {
    familias: {
      "demo-agua-sab-1-5l-x6": {
        nombre: "Agua Saborizada 1,5L",
        sabores: ["Manzana", "Naranja", "Pomelo"],
      },
      "demo-gaseosa-lima-2-25l-x8": {
        nombre: "Gaseosa Lima Limón 2,25L",
        sabores: ["Lima", "Limón", "Pomelo"],
      },
    },
    ocultar: [],
  };
})(typeof window !== "undefined" ? window : globalThis);
