# 📘 Atividade: Sistema de Notas da Turma

## 🎯 Objetivo

Aprenda a criar funções que recebem listas e dicionários, e a combinar essas funções para gerar um relatório de desempenho da turma.

## 📝 Tarefas

### 🛠️ Calcular a Média de um Aluno

#### Descrição
Crie a função `calcular_media(notas)`, que recebe uma lista de notas de um aluno e retorna a média aritmética delas.

#### Requisitos
O programa concluído deve:

- Definir a função `calcular_media(notas)`
- Retornar a soma das notas dividida pela quantidade de notas
- Testar a função com a lista `[8, 9, 7]`, que deve resultar em `8.0`


### 🛠️ Classificar a Situação do Aluno

#### Descrição
Crie a função `classificar(media)`, que recebe a média de um aluno e retorna a sua situação de acordo com as regras da escola.

#### Requisitos
O programa concluído deve:

- Definir a função `classificar(media)`
- Retornar `"Aprovado"` quando a média for maior ou igual a 7
- Retornar `"Recuperação"` quando a média for maior ou igual a 5 e menor que 7
- Retornar `"Reprovado"` nos demais casos

Exemplo:

```python
classificar(8.0)  # "Aprovado"
classificar(6.5)  # "Recuperação"
classificar(3.0)  # "Reprovado"
```


### 🛠️ Gerar o Relatório da Turma

#### Descrição
Crie a função `gerar_relatorio(alunos)`, que recebe um dicionário em que cada chave é o nome de um aluno e cada valor é a lista de suas notas. Para cada aluno, a função deve imprimir o nome, a média e a situação. Ao final, deve imprimir quantos alunos foram aprovados.

#### Requisitos
O programa concluído deve:

- Definir a função `gerar_relatorio(alunos)`
- Percorrer o dicionário com `for` e usar `calcular_media()` e `classificar()` para cada aluno
- Imprimir uma linha por aluno no formato `Nome: média (situação)`, com a média arredondada em uma casa decimal
- Imprimir ao final a quantidade de alunos aprovados
- Executar a função com o dicionário `{"Ana": [8, 9, 7], "Bruno": [4, 6, 5], "Carla": [3, 4, 2]}`
