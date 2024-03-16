# Sobre Votar

Este é um projeto de API desenvolvido em Python utilizando o framework FastAPI, voltado para fornecer informações sobre a votação em Portugal em 2024.

## Utilização

1. **Pré-requisitos:** Certifique-se de ter o Python instalado em sua máquina e uma chave de API válida configurada para acessar recursos externos, se necessário.

2. **Instalação:** Clone este repositório em sua máquina local e instale as dependências Python executando o seguinte comando no terminal:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuração:** Se necessário, configure qualquer variável de ambiente ou arquivo de configuração para o seu ambiente específico.

4. **Execução:** Inicie o servidor FastAPI executando o seguinte comando:

   ```bash
   uvicorn main:app --reload
   ```

5. **Uso:** Acesse a API em `http://localhost:8000` e utilize os endpoints disponíveis para obter informações sobre a votação em Portugal em 2024.

## Endpoints

- `GET /`: Retorna uma mensagem de boas-vindas e uma visão geral do propósito da API.

- `POST /prompt`: Permite aos usuários enviar consultas ou prompts para obter informações sobre a votação em Portugal em 2024.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas para relatar bugs, solicitar recursos adicionais ou propor melhorias. Se desejar contribuir com código, faça um fork deste repositório, faça suas alterações e envie uma solicitação pull.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

---

Desenvolvido por Otavio Serra - [GitHub](https://github.com/olserra)
