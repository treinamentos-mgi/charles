# 📘 Tarefa: Criando APIs REST com FastAPI

## 🎯 Objective

Aprenda a criar uma API REST com o framework FastAPI, definindo rotas, validando dados com Pydantic e implementando operações CRUD com os códigos de status HTTP adequados.

## 📝 Tasks

### 🛠️ Criar a Primeira Rota

#### Descrição
Crie uma aplicação FastAPI com duas rotas: uma rota raiz que dá boas-vindas e uma rota que retorna um item a partir do seu identificador na URL. Depois, execute a aplicação com `uvicorn` e explore a documentação automática em `/docs`.

#### Requisitos
O programa completo deve:

- Criar uma instância de `FastAPI` chamada `app`
- Implementar `GET /` retornando a mensagem `{"message": "Welcome to the Task API"}`
- Implementar `GET /items/{item_id}` retornando `{"item_id": item_id}`, com `item_id` do tipo `int`
- Mostrar, no README ou em comentário, o comando usado para iniciar o servidor (`uvicorn main:app --reload`)
- Acessar `http://127.0.0.1:8000/docs` e confirmar que as duas rotas aparecem na documentação

### 🛠️ Modelar Dados com Pydantic

#### Descrição
Crie um modelo para representar uma tarefa (`Task`) e use-o para validar os dados recebidos pela API. Um cliente deve conseguir cadastrar tarefas e listá-las.

#### Requisitos
O programa completo deve:

- Definir um modelo `Task` com `BaseModel` contendo os campos `id` (int), `title` (str), `done` (bool, padrão `False`)
- Armazenar as tarefas em uma lista em memória
- Implementar `POST /tasks` que recebe uma tarefa, a salva e retorna status `201 Created`
- Implementar `GET /tasks` que retorna a lista de todas as tarefas
- Ao enviar um `title` vazio ou ausente, a API deve responder com status `422 Unprocessable Entity`

Exemplo de entrada (`POST /tasks`):

```json
{"id": 1, "title": "Estudar FastAPI"}
```

Exemplo de saída (`GET /tasks`):

```json
[{"id": 1, "title": "Estudar FastAPI", "done": false}]
```

### 🛠️ Buscar, Atualizar e Remover Tarefas

#### Descrição
Complete o CRUD da API. Cada operação deve tratar corretamente o caso em que a tarefa não existe.

#### Requisitos
O programa completo deve:

- Implementar `GET /tasks/{task_id}` retornando a tarefa correspondente
- Implementar `PUT /tasks/{task_id}` para substituir os dados de uma tarefa existente
- Implementar `DELETE /tasks/{task_id}` retornando status `204 No Content` ao remover a tarefa
- Quando o `task_id` não existir, retornar status `404 Not Found` com uma mensagem de erro, usando `HTTPException`

### 🛠️ Filtrar Tarefas com Query Parameters

#### Descrição
Permita que o cliente filtre a lista de tarefas pelo estado de conclusão, usando parâmetros de consulta na URL.

#### Requisitos
O programa completo deve:

- Alterar `GET /tasks` para aceitar o parâmetro opcional `done` (bool)
- Quando `done` for informado, retornar apenas as tarefas com aquele valor
- Quando `done` não for informado, retornar todas as tarefas
- Exemplo de uso: `GET /tasks?done=true` retorna somente as tarefas concluídas
