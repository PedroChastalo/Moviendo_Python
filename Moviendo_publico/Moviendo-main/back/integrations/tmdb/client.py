import logging
import requests
from django.conf import settings
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)


class TMDBClient:
    def __init__(self):
        self.api_key = settings.TMDB_API_KEY
        self.base_url = settings.TMDB_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json;charset=utf-8"
        }
        self.params_common = {"language": "pt-BR"}

    def buscar(self, query):
        if not query:
            raise ValidationError("Query é obrigatória")
        
        url = f"{self.base_url}/search/multi"
        params = {**self.params_common, "query": query}
        
        response = requests.get(url, headers=self.headers, params=params)
        
        if response.status_code != 200:
            logger.error(f"Erro TMDB buscar: {response.status_code}", extra={
                'response': response.text,
                'query': query
            })
            raise ValidationError(f"Erro ao buscar no TMDB: {response.status_code}")
        
        return response.json().get('results', [])

    def get_detalhes(self, tmdb_id, tipo):
        if not tmdb_id or not tipo:
            raise ValidationError("tmdb_id e tipo são obrigatórios")
        
        endpoint = "movie" if tipo == 'movie' else "tv"
        url = f"{self.base_url}/{endpoint}/{tmdb_id}"
        params = {**self.params_common, "append_to_response": "credits"}
        
        response = requests.get(url, headers=self.headers, params=params)
        
        if response.status_code == 404:
            raise ValidationError(f"Obra não encontrada no TMDB (ID: {tmdb_id})")
        
        if response.status_code != 200:
            logger.error(f"Erro TMDB detalhes: {response.status_code}", extra={
                'tmdb_id': tmdb_id,
                'tipo': tipo,
                'response': response.text
            })
            raise ValidationError(f"Erro ao buscar detalhes no TMDB")
        
        return response.json()
