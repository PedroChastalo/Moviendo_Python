import toast from "react-hot-toast";

export const getErrorMessage = (
  error,
  defaultMessage = "Ocorreu um erro inesperado"
) => {
  if (error.response?.data) {
    const { data } = error.response;

    if (data.message) {
      return data.message;
    }

    if (data.detail) {
      return data.detail;
    }

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

  if (error.code === "NETWORK_ERROR") {
    return "Erro de conexão. Verifique sua internet e tente novamente.";
  }
  if (error.code === "ECONNABORTED") {
    return "A requisição demorou muito para responder. Tente novamente.";
  }

  if (error.message) {
    return error.message;
  }

  return defaultMessage;
};


export const showErrorToast = (error, defaultMessage) => {
  const message = getErrorMessage(error, defaultMessage);
  toast.error(message);
};

export const handleApiCall = async (apiCall, errorMessage) => {
  try {
    return await apiCall();
  } catch (error) {
    console.error("API Error:", error);
    showErrorToast(error, errorMessage);
    return null;
  }
};

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
    throw error;
  }
};