export const STATUS_LABELS = {
  quero_assistir: "Quero Assistir",
  assistindo: "Assistindo",
  assistido: "Assistido",
};

export const STATUS_OPTIONS = Object.entries(STATUS_LABELS).map(
  ([value, label]) => ({
    value,
    label,
  })
);

export const getStatusLabel = (status) => STATUS_LABELS[status] || status;
