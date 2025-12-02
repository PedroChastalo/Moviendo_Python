import api from "./api";

const tmdbService = {
  search: async (query, page = 1) => {
    const response = await api.get("/obras/pesquisar_tmdb/", {
      params: { query, page },
    });
    return response.data;
  },

  getDetails: async (tmdbId, type) => {
    const response = await api.get("/obras/get_tmdb_details/", {
      params: { tmdb_id: tmdbId, tipo: type },
    });
    return response.data;
  },

  importMovie: async (tmdbId) => {
    const response = await api.post("/obras/importar_tmdb/", {
      tmdb_id: tmdbId,
      tipo: "movie",
    });
    return response.data;
  },

  importTv: async (tmdbId) => {
    const response = await api.post("/obras/importar_tmdb/", {
      tmdb_id: tmdbId,
      tipo: "tv",
    });
    return response.data;
  },

  buildPosterUrl: (path, size = "w500") => {
    if (!path) return null;
    return `https://image.tmdb.org/t/p/${size}${path}`;
  },
};

export default tmdbService;
