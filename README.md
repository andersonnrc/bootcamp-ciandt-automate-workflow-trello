# 🤖 Automação de Tarefas no Trello com IA (Python)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![VSCode](https://img.shields.io/badge/Editor-VSCode-blue?logo=visualstudiocode)
![Trello](https://img.shields.io/badge/Trello-API-blue?logo=trello)
![AI](https://img.shields.io/badge/AI-Google%20AI%20Studio-orange)

---

## 📖 Sobre o projeto

Este projeto consiste em uma aplicação de **automação de fluxo de tarefas** utilizando **Python + Inteligência Artificial**, integrada ao **Trello**.

A aplicação funciona como uma **agenda inteligente**, onde um agente conversacional interpreta o que o usuário digita e automaticamente:

- Cria tarefas no quadro
- Organiza o fluxo de trabalho
- Move tarefas entre status

---

## ⚙️ Como funciona

O sistema utiliza um **agente de IA** que interage com o usuário e executa ações no Trello com base nas instruções fornecidas.

### 🔄 Fluxo das tarefas

```text
A fazer → Em andamento → Concluído

Dependendo do comando do usuário, o agente pode:

Criar uma nova task (em A fazer)
Listar tarefas
Alterar status da task
Organizar atividades do dia
```

---

## 🧠 Funcionalidades

- ✅ Criar tarefas automaticamente
- 📋 Listar tarefas (todas ou por status)
- 🔄 Atualizar status da tarefa
- 📅 Contexto temporal (data/hora atual)
- 🤖 Interação via agente inteligente
- 📌 Organização automática do fluxo de trabalho

---

## 🏗️ Arquitetura do projeto

O projeto é dividido em três partes principais:

#### 1. Integração com Trello

Responsável por:
- Autenticação via API
- Manipulação de boards, listas e cards

#### 2. Regras de negócio

Funções principais:
- adicionar_tarefa
- listar_tarefas
- mudar_status_tarefa

#### 3. Agente de IA

Utiliza o Google AI Studio (ADK) para:
- Interpretar comandos do usuário
- Orquestrar chamadas das funções
- Automatizar o fluxo de tarefas

---

## 🧰 Tecnologias utilizadas
- Python 3.x
- Trello API
- Google AI Studio (ADK)
- VSCode

---

## 🚀 Configuração do ambiente

Siga os passos abaixo para configurar e executar o projeto localmente.

### 🔹 1. Pré-requisitos

- Conta no Trello: https://trello.com/
- Conta no Google AI Studio: https://aistudio.google.com/


### 🔹 2. Configuração no Trello

1. Crie uma conta no Trello  
2. Crie um aplicativo (Power-Up): https://trello.com/power-ups/admin/  
3. Gere as credenciais:
   - API Key
   - API Secret
   - Token
4. Crie um quadro (board). O nome do board deve coincidir com a variável no código:


5. Crie as listas obrigatórias no quadro:

- A FAZER  
- EM ANDAMENTO  
- CONCLUÍDO  

### 🔹 3. Configuração do projeto

Clone o repositório e configure o ambiente virtual:

```
python -m venv .automate-workflow
source .automate-workflow/bin/activate  # Linux/Mac
# .automate-workflow\Scripts\activate   # Windows

pip install -r requirements.txt
```

### 🔹 4. Variáveis de ambiente

Crie um arquivo .env com as seguintes variáveis:

```bash
GOOGLE_API_KEY=your_key
TRELLO_API_KEY=your_key
TRELLO_API_SECRET=your_secret
TRELLO_TOKEN=your_token
```
### 🔹 5. Configuração do agente (IA)

Crie o agente utilizando o ADK:
```
adk create agenttaskmanager
```

Gere sua API Key no Google AI Studio:

👉 https://aistudio.google.com/apikey

### 🔹 6. Executando a aplicação

Inicie o servidor local:
```
adk web
```

Acesse no navegador:
👉 http://127.0.0.1:8000

---

## 💬 Exemplo de uso

Ao iniciar, o agente irá perguntar:

> "Quais são as tarefas do dia?"

Você pode responder:

- "Estudar Python"
- "Fazer exercício do capítulo 3"
- "Atualizar projeto no GitHub"

O sistema irá automaticamente:

- Criar cards no Trello  
- Colocar em **A fazer**

Depois, você pode dizer:

- "Começar tarefa estudar Python" → move para **Em andamento**
- "Finalizar tarefa estudar Python" → move para **Concluído**

![](/images/agente.png "Resultado da interação com o agente")

---

## 👨‍💻 Contato

[Linkedin](https://www.linkedin.com/in/anderson-ribeiro-carvalho)