import requests
from crewai.tools import BaseTool
from typing import Optional
import os

class FetchMovieInfoTool(BaseTool):
    name: str = "Especialista em Filmes"
    description: str = "Busca informações sobre filmes ou séries no TMDB."

    def _run(self, titulo: str) -> str:
        api_key = os.getenv("TMDB_API_KEY")
        response = requests.get(
            f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={titulo}&language=pt-BR"
        )
        data = response.json()
        if "results" not in data or not data["results"]:
            return "Filme não encontrado ou resposta inválida da API."
        filme = data["results"][0]
        return f"Título: {filme['title']}\nDescrição: {filme['overview']}\nLançamento: {filme['release_date']}"

class FetchHeroTool(BaseTool):
    name: str = "Consultor de Heróis"
    description: str = "Retorna informações sobre um super-herói ou vilão."

    def _run(self, nome: str) -> str:
        access_token = os.getenv("SUPERHERO_API_TOKEN")
        response = requests.get(f"https://superheroapi.com/api/{access_token}/search/{nome}")
        data = response.json()
        if data["response"] != "success":
            return "Personagem não encontrado."
        hero = data["results"][0]
        return (
            f"Nome: {hero['name']}\n"
            f"Inteligência: {hero['powerstats']['intelligence']}\n"
            f"Força: {hero['powerstats']['strength']}\n"
            f"Publisher: {hero['biography']['publisher']}"
        )

class FetchQuoteTool(BaseTool):
    name: str = "Gerador de Citações"
    description: str = "Fornece uma citação inspiradora ou icônica."

    def _run(self, _: str = None) -> str:
        try:
            response = requests.get("https://api.quotable.io/random?tags=famous-quotes|inspirational", timeout=5)
            response.raise_for_status()
            data = response.json()
            return f'"{data["content"]}" — {data["author"]}'
        except Exception as e:
            return f"Citação não disponível no momento. Erro: {str(e)}"
