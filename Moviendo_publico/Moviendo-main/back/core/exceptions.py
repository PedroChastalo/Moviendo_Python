from datetime import datetime
import logging

from django.conf import settings
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        if isinstance(exc, IntegrityError):
            response = Response(
                {"message": "Erro de integridade de dados (Conflito de Unique ou FK)"},
                status=status.HTTP_409_CONFLICT,
            )
        elif isinstance(exc, ValidationError):
            response = Response(
                {"message": str(exc)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            # Loga a exceção completa para aparecer no terminal / logs
            logger.exception("Unhandled exception in API", exc_info=exc)
            response = Response(
                {"message": "Ocorreu um erro interno no servidor."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    payload = {
        "status": response.status_code,
        "path": context["request"].path,
        "timestamp": datetime.now().isoformat(),
    }

    if response.status_code == 400:
        if hasattr(response, "data") and isinstance(response.data, dict):
            errors = []
            for field, messages in response.data.items():
                if isinstance(messages, list):
                    for message in messages:
                        errors.append(f"{field}: {message}")
                else:
                    errors.append(f"{field}: {messages}")
            payload["message"] = "; ".join(errors)
        else:
            payload["message"] = "Dados inválidos"
    elif response.status_code == 404:
        payload["message"] = "Recurso não encontrado"
    elif hasattr(response, "data") and "message" in response.data:
        payload["message"] = response.data["message"]
    else:
        payload["message"] = "Erro no servidor"

    # Em modo de desenvolvimento, expõe informações extras da exceção
    if getattr(settings, "DEBUG", False):
        payload["exception_type"] = exc.__class__.__name__
        payload["exception_message"] = str(exc)

    response.data = payload
    return response
