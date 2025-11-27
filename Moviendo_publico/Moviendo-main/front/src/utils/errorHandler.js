import toast from "react-hot-toast";

/**
 * Extrai mensagem de erro da resposta da API
 * @param {Error} error - Erro da requisição
 * @param {string} defaultMessage - Mensagem padrão se não houver mensagem específica
 * @returns {string} Mensagem de erro formatada
 */
export const getErrorMessage = (
  error,
  defaultMessage = "Ocorreu um erro inesperado"
) => {
  // Se há resposta da API
  if (error.response?.data) {
    const { data } = error.response;

    // Mensagem direta
    if (data.message) {
      return data.message;
    }

    // Erros de validação (formato DRF)
    if (data.detail) {
      return data.detail;
    }

    // Erros de campo específico
    if (typeof data === "object") {
      const fieldErrors = [];
      for (const [field, messages] of Object.entries(data)) {
        if (Array.isArray(messages)) {
          fieldErrors.push(`${field}: ${messages.join(", ")}`);
        } else if (typeof messages === "string") {
          fieldErrors.push(`${field}: ${messages}`);
        }
      }
      if (fieldErrors.length > 0) {
        return fieldErrors.join("; ");
      }
    }
  }

  // Erro de rede
  if (error.code === "NETWORK_ERROR") {
    return "Erro de conexão. Verifique sua internet e tente novamente.";
  }

  // Timeout
  if (error.code === "ECONNABORTED") {
    return "A requisição demorou muito para responder. Tente novamente.";
  }

  // Mensagem do erro nativo
  if (error.message) {
    return error.message;
  }

  return defaultMessage;
};

/**
 * Exibe toast de erro com mensagem extraída
 * @param {Error} error - Erro da requisição
 * @param {string} defaultMessage - Mensagem padrão
 */
export const showErrorToast = (error, defaultMessage) => {
  const message = getErrorMessage(error, defaultMessage);
  toast.error(message);
};

/**
 * Wrapper para chamadas de API com tratamento de erro automático
 * @param {Function} apiCall - Função da API a ser chamada
 * @param {string} errorMessage - Mensagem de erro padrão
 * @returns {Promise} Resultado da API ou null em caso de erro
 */
export const handleApiCall = async (apiCall, errorMessage) => {
  try {
    return await apiCall();
  } catch (error) {
    console.error("API Error:", error);
    showErrorToast(error, errorMessage);
    return null;
  }
};

/**
 * Wrapper para operações CRUD com feedback automático
 * @param {Function} apiCall - Função da API
 * @param {string} successMessage - Mensagem de sucesso
 * @param {string} errorMessage - Mensagem de erro
 * @returns {Promise<boolean>} true se sucesso, false se erro
 */
export const handleCrudOperation = async (
  apiCall,
  successMessage,
  errorMessage
) => {
  try {
    const result = await apiCall();
    toast.success(successMessage);
    return result;
  } catch (error) {
    console.error("CRUD Error:", error);
    showErrorToast(error, errorMessage);
    throw error; // Re-throw para que o componente possa lidar com o estado
  }
};
