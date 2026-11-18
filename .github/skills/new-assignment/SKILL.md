---
name: new-assignment
description: Cria uma nova tarefa (assignment) no projeto, incluindo a pasta, o README.md no formato do template, a entrada em config.json e anexos opcionais. Use quando o usuário pedir para criar, adicionar ou publicar uma nova tarefa/exercício.
---

# Criar um novo assignment

## Passos

1. **Definir o escopo**: consulte [references/assignment-guide.md](references/assignment-guide.md) para escolher o nível de dificuldade, o número de tarefas (2 a 4) e se deve haver starter code.
2. **Criar a pasta**: `assignments/<assignment-id>/`, usando um id descritivo em kebab-case (ex.: `python-basics`).
3. **Criar o `README.md`**: siga [templates/assignment-template.md](../../../templates/assignment-template.md) e as regras de [.github/instructions/assignments.instructions.md](../../instructions/assignments.instructions.md). Não traduza os cabeçalhos do template.
4. **Registrar no `config.json`**:
   ```bash
   node .github/skills/new-assignment/scripts/update-config.js <id> "<título>" "<descrição>"
   ```
   O script adiciona a entrada com `path: assignments/<id>` e prazo de 7 dias.
5. **Anexar arquivos (opcional)**: coloque o arquivo em `assignments/<id>/` e execute:
   ```bash
   node .github/skills/new-assignment/scripts/add-attachment.js <id> "<nome exibido>" <arquivo> <tipo>
   ```
   O script valida que o arquivo existe e que o assignment está no `config.json`. Anexos já registrados são ignorados.

## Verificação

- `config.json` continua sendo JSON válido e contém a nova entrada.
- O `README.md` possui todas as seções do template com os cabeçalhos originais.
- Os links do `README.md` apontam para arquivos existentes.
