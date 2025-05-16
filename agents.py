from crewai import Agent
from tools import FetchMovieInfoTool, FetchHeroTool, FetchQuoteTool
from config import get_llm  # Garante que todos usem a mesma LLM

def create_agente_filmes():
    return Agent(
        role="Especialista em Filmes",
        goal="Buscar detalhes sobre filmes populares e recomendados",
        backstory="Crítico de cinema renomado, com memória fotográfica de cada lançamento do TMDB.",
        tools=[FetchMovieInfoTool()],
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

def create_agente_heroi():
    return Agent(
        role="Consultor de Heróis e Vilões",
        goal="Analisar personagens famosos da cultura pop",
        backstory="Especialista em quadrinhos e filmes, conhece o histórico e habilidades de todos os heróis.",
        tools=[FetchHeroTool()],
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

def create_agente_frase():
    return Agent(
        role="Filósofo Pop",
        goal="Finalizar com uma citação impactante e inspiradora",
        backstory="Intelectual das artes, mistura filosofia com cultura pop para criar reflexões profundas.",
        tools=[FetchQuoteTool()],
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )
