from crewai import Task

def buscar_dados_do_filme(agent, titulo):
    return Task(
        description=f"Buscar informações completas sobre o filme '{titulo}', incluindo descrição e data de lançamento.",
        agent=agent,
        expected_output="Título, descrição e data de lançamento do filme.",
        output_file="output/filme.txt",
        verbose=True
    )

def buscar_heroi(agent, contexto):
    return Task(
        description="Com base no filme pesquisado, selecione um personagem famoso associado a ele e retorne seus atributos principais (inteligência, força, etc).",
        agent=agent,
        context=contexto,
        expected_output="Nome do herói, atributos principais e editora.",
        output_file="output/personagem.txt",
        verbose=True
    )

def gerar_citacao(agent, contexto):
    return Task(
        description="Forneça uma citação inspiradora e relacionada ao universo de cultura pop, conectando com o conteúdo anterior.",
        agent=agent,
        context=contexto,
        expected_output="Citação famosa com autor.",
        output_file="output/citacao.txt",
        verbose=True
    )
