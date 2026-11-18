# API de Consulta de Livros

Projeto da Lista de Exercícios 1 — Programação / Web Coding.

## Objetivo

Criar uma API mínima com Python e Flask que disponibiliza uma rota `GET /livros`, retornando os dados de três livros em JSON.

## Estrutura

```text
lista1_api_flask/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 1. Criar o ambiente virtual

Linux / Fedora / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (Prompt de Comando):

```bat
python -m venv .venv
.venv\Scripts\activate
```

## 2. Instalar dependências

```bash
pip install -r requirements.txt
```

## 3. Executar a aplicação

```bash
python app.py
```

O servidor será iniciado em `http://127.0.0.1:5000`.

## 4. Consultar os livros

Acesse no navegador:

`http://127.0.0.1:5000/livros`

Ou use o terminal:

```bash
curl -i http://127.0.0.1:5000/livros
```

A resposta esperada é HTTP 200 e um JSON com a chave `livros`, contendo os três registros:

```json
{
  "livros": [
    {
      "id": 1,
      "titulo": "Dom Casmurro",
      "autor": "Machado de Assis",
      "ano": 1899
    },
    { "id": 2, "titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890 },
    {
      "id": 3,
      "titulo": "A Hora da Estrela",
      "autor": "Clarice Lispector",
      "ano": 1977
    }
  ]
}
```

## 5. Publicar no GitHub

Crie um repositório público e, dentro desta pasta, execute:

```bash
git init
git add .
git commit -m "Implementa API de consulta de livros com Flask"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
git push -u origin main

Troque o endereço de exemplo pelo endereço do seu repositório.

## Observação

Os livros ficam em uma lista Python na memória. Não há banco de dados nesta atividade; os dados voltam ao estado inicial quando a aplicação é reiniciada.
