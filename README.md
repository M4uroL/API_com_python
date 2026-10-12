# API de Animes

Uma API REST simples, desenvolvida com Flask, para consultar, cadastrar, editar e excluir animes.

## Requisitos

- Python 3
- Flask

## Instalação e execução

1. Instale o Flask:

   ```bash
   pip install Flask
   ```

2. Salve o código da aplicação em um arquivo, por exemplo, `app.py`.

3. Execute a aplicação:

   ```bash
   python app.py
   ```

A API será iniciada em `http://localhost:5000`.

> A aplicação também precisa importar `Flask`, `request` e `jsonify`, criar o objeto `app` e definir a lista `animes`.

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/animes/<id>` | Busca um anime pelo ID |
| `POST` | `/animes/` | Cadastra um anime |
| `PUT` | `/animes/<id>` | Atualiza os dados de um anime |
| `DELETE` | `/animes/<id>` | Exclui um anime |

### Buscar anime por ID

```bash
curl http://localhost:5000/animes/1
```

### Cadastrar anime

Envie os dados no formato JSON. O código atual não cria IDs automaticamente; por isso, inclua o campo `id` no corpo da requisição.

```bash
curl -X POST http://localhost:5000/animes/ \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "nome": "Naruto", "genero": "Aventura"}'
```

### Editar anime

Envie no corpo da requisição os campos que deseja atualizar.

```bash
curl -X PUT http://localhost:5000/animes/1 \
  -H "Content-Type: application/json" \
  -d '{"genero": "Ação e aventura"}'
```

### Excluir anime

```bash
curl -X DELETE http://localhost:5000/animes/1
```

## Armazenamento

Os animes são guardados em uma lista na memória da aplicação. Os dados não são persistidos: eles serão perdidos quando o servidor for reiniciado.

## Observações

- O código atual não define uma resposta específica para IDs inexistentes.
- A rota `PUT` atualiza o anime, mas não retorna uma resposta explícita.
- Na rota `DELETE`, o `return` está dentro do laço de busca, o que pode interromper a verificação antes de encontrar o anime.
- Não há validação dos dados recebidos nem geração automática de IDs.
- `debug=True` é útil durante o desenvolvimento, mas deve ser desativado em produção.
