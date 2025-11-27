export const TIPO_LABELS = {
  filme: "Filme",
  serie: "Série",
};

export const TIPO_OPTIONS = Object.entries(TIPO_LABELS).map(
  ([value, label]) => ({
    value,
    label,
  })
);

export const getTipoLabel = (tipo) => TIPO_LABELS[tipo] || tipo;
