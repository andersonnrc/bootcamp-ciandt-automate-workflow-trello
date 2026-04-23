from google.adk.agents.llm_agent import Agent
from trello import TrelloClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

API_KEY = os.getenv('TRELLO_API_KEY')
API_SECRET = os.getenv('TRELLO_API_SECRET')
TOKEN = os.getenv('TRELLO_TOKEN')

BOARD_NAME = "DIO"

# ==========================================
# HELPERS
# ==========================================

def get_client():
    return TrelloClient(
        api_key=API_KEY,
        api_secret=API_SECRET,
        token=TOKEN
    )

def get_board(client):
    boards = client.list_boards()
    return next((b for b in boards if b.name == BOARD_NAME), None)

def get_listas(board):
    return board.list_lists()

def normalizar_status(status):
    mapa = {
        "a fazer": ["A FAZER", "TO DO", "TODO"],
        "em andamento": ["EM ANDAMENTO", "DOING"],
        "concluído": ["CONCLUÍDO", "DONE"]
    }
    return mapa.get(status.lower(), [])

def get_temporal_context():
    return datetime.now().strftime('%Y/%m/%d %H:%M:%S')

# ==========================================
# FUNÇÕES PRINCIPAIS
# ==========================================

def adicionar_tarefa(nome_da_task, descricao_da_task, due_date=None):
    client = get_client()
    board = get_board(client)

    if not board:
        return "Board não encontrado"

    listas = get_listas(board)

    lista = next(
        (l for l in listas if l.name.upper() in ["A FAZER", "TO DO", "TODO"]),
        None
    )

    if not lista:
        return "Lista não encontrada"

    lista.add_card(name=nome_da_task, desc=descricao_da_task, due=due_date)

    return f"Tarefa '{nome_da_task}' criada"

def listar_tarefas(status="todas"):
    client = get_client()
    board = get_board(client)

    if not board:
        return []

    listas = get_listas(board)

    if status.lower() != "todas":
        nomes = normalizar_status(status)
        listas = [l for l in listas if l.name.upper() in nomes]

    tarefas = []
    for lista in listas:
        for card in lista.list_cards():
            tarefas.append({
                "nome": card.name,
                "descricao": card.desc,
                "status": lista.name
            })

    return tarefas

def mudar_status_tarefa(nome_da_task, novo_status):
    client = get_client()
    board = get_board(client)

    if not board:
        return "Board não encontrado"

    listas = get_listas(board)
    nomes = normalizar_status(novo_status)

    lista_destino = next((l for l in listas if l.name.upper() in nomes), None)

    if not lista_destino:
        return "Lista destino não encontrada"

    for lista in listas:
        for card in lista.list_cards():
            if card.name.lower() == nome_da_task.lower():
                card.change_list(lista_destino.id)
                return f"{nome_da_task} movido para {lista_destino.name}"

    return "Card não encontrado"

# ==========================================
# AGENT
# ==========================================

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    instruction="""
        Você é um agente de organização de tarefas.
        Sua função é receber uma tarefa e criar no Trello com o nome e descrição da tarefa.
        Você deve me perguntar as atividades que tenho no dia e criar um card para cada uma delas.
        Você inicia a conversa assim que for ativado, perguntando quais são as tarefas do dia.
        Sempre inicie a conversa perguntando quais são as tarefas do dia informando a data pela tool get_temporal_context,
        e depois vá perguntando se tem mais alguma tarefa, até que o usuário diga que não tem mais tarefas.
        Suas funções:
        1. Adicionar novas tarefas com nome e descrição
        2. Listas todas as tarefas ou filtrar por status
        3. Marcar tarefas como concluídas
        4. Remover tarefas da lista
        5. Mudar o status da tarefa (ex: de "A fazer" para "Em andamento" e de "Em andamento" para "Concluído")
        6. Gerar contexto temporal (data e hora atual) para organizar as tarefas do dia.
    """,
    tools=[
        get_temporal_context,
        adicionar_tarefa,
        listar_tarefas,
        mudar_status_tarefa
    ],
)