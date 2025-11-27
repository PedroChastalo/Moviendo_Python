import api from "./api";

export const generosService = {
  getAll: async () => {
    const response = await api.get("/generos/");
    return response.data;
  },

  getById: async (id) => {
    const response = await api.get(`/generos/${id}/`);
    return response.data;
  },

  create: async (genero) => {
    const response = await api.post("/generos/", genero);
    return response.data;
  },
};

export default generosService;
