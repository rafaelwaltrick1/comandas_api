from crewai import Crew
from agents import create_agente_filmes, create_agente_heroi, create_agente_frase
from tasks import buscar_dados_do_filme, buscar_heroi, gerar_citacao
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

# Entrada do usuário
titulo_filme = "Batman"  # Altere aqui conforme o teste desejado

# Criação dos agentes
agente_filmes = create_agente_filmes()
agente_heroi = create_agente_heroi()
agente_frase = create_agente_frase()

# Criação das tarefas
task1 = buscar_dados_do_filme(agente_filmes, titulo_filme)
task2 = buscar_heroi(agente_heroi, [task1])
task3 = gerar_citacao(agente_frase, [task1, task2])

# Monta a equipe
crew = Crew(
    agents=[agente_filmes, agente_heroi, agente_frase],
    tasks=[task1, task2, task3],
    verbose=True
)

# Executa o fluxo
print("🎬 Iniciando o Especialista em Cultura Pop...")
resultado = crew.kickoff()

print("\n✅ RESULTADO FINAL:")
print(resultado)

# Salvar os resultados manualmente
for task in crew.tasks:
    if task.output_file and task.output:
        try:
            with open(task.output_file, "w", encoding="utf-8") as f:
                f.write(str(task.output))  # CORRETO: task.output já é string
            print(f"✅ Resultado salvo em: {task.output_file}")
        except Exception as e:
            print(f"❌ Erro ao salvar {task.output_file}: {e}")

