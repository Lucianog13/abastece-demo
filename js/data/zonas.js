// Zonas de reparto — DEMO de Abastece (coordenadas de ejemplo, Paraná).
// En producción cada comercio define sus propias zonas desde el panel admin.
(function (root) {
  root.ZONAS = {
    distribuidora: { lat: -31.7446, lon: -60.4983, nombre: "Depósito central" },
    zonas: {
      1: {
        nombre: "Zona Norte",
        centro: { lat: -31.7246, lon: -60.5083 },
        color: "#7c3aed",
      },
      2: {
        nombre: "Zona Sur",
        centro: { lat: -31.7746, lon: -60.4883 },
        color: "#3b82f6",
      },
    },
  };
})(typeof window !== "undefined" ? window : globalThis);
