🎬 Projeto: Especialista em Cultura Pop
Este projeto usa a biblioteca CrewAI para criar uma equipe de agentes que trabalham juntos para buscar informações sobre um filme, um personagem e gerar uma citação inspiradora. Tudo é salvo em arquivos .txt.

👥 Agentes e Funções
Especialista em Filmes
Busca dados do filme (nome, descrição e data).
🔗 API: The Movie Database - TMDB

Consultor de Heróis e Vilões
Procura um personagem relacionado ao filme e retorna seus atributos.
🔗 API: SuperHero API

Filósofo Pop
Gera uma citação inspiradora com base no tema do filme.
🔗 API: Quotable API

▶️ Como usar
Crie um arquivo .env com suas chaves de API:

ini
Copiar
Editar
TMDB_API_KEY=...
SUPERHERO_API_TOKEN=...
Edite o main.py e troque o título do filme:

python
Copiar
Editar
titulo_filme = "Batman"
Execute:

bash
Copiar
Editar
python main.py
Os resultados serão salvos na pasta output.