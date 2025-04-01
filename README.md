# Chatbot IA para WhatsApp com EvolutionAPI

Este projeto é um chatbot para WhatsApp utilizando:

- [EvolutionAPI](https://doc.evolution-api.com/v2/pt/get-started/introduction) para integração com o WhatsApp
- [FastAPI](https://fastapi.tiangolo.com/) para a API
- [LangChain](https://www.langchain.com/) para gestão da conversa com IA
- Modelos da [OpenAI](https://platform.openai.com/)
- Docker e Docker Compose para facilitar o deploy

---

## Como subir o projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/pycodebr/whatsapp_ai_bot.git
cd whatsapp_ai_bot
```

2. **Crie seu `.env` a partir do `.env.example`**

Copie o arquivo de exemplo e edite com suas chaves:

```bash
cp .env.example .env
```

Edite o `.env` e adicione os seguintes valores:

- `OPENAI_API_KEY` (sua chave da OpenAI)
- `AUTHENTICATION_API_KEY` (chave de autenticação da EvolutionAPI)
- `EVOLUTION_INSTANCE_NAME` (nome da instância no EvolutionAPI)

⚠️ O valor de `EVOLUTION_INSTANCE_NAME` deve ser exatamente o mesmo nome da instância que será criada no painel da EvolutionAPI em:

[http://localhost:8080/manager](http://localhost:8080/manager)

É por meio desse painel que você adiciona e conecta uma nova instância do WhatsApp e define seu nome.

3. **Adicione documentos para RAG (Busca por documentos):**

Coloque os documentos que deseja usar para busca com RAG (Retrieval-Augmented Generation) na pasta:

```
rag_files/
```

Arquivos nessa pasta serão automaticamente vetorizados e utilizados nas respostas com IA.

4. **Ajuste os prompts no `.env`:**

Antes de subir os containers, personalize os seguintes prompts conforme o contexto da sua aplicação:

- `AI_CONTEXTUALIZE_PROMPT` (prompt usado para gerar contexto com base nas mensagens do usuário)
- `AI_SYSTEM_PROMPT` (prompt que define o comportamento e papel do assistente)

Essas variáveis são fundamentais para que o chatbot responda de forma adequada ao seu caso de uso.

⚠️ Esta etapa deve ser feita **antes** de subir os containers.

5. **Suba os containers com Docker Compose:**

```bash
docker-compose up --build
```

6. **Acesse o painel da EvolutionAPI:**

O painel da EvolutionAPI estará disponível em: [http://localhost:8080/manager](http://localhost:8080/manager)

Utilize o painel para adicionar e gerenciar suas instâncias.

7. **Conecte a instância do WhatsApp e configure o webhook:**

Após conectar sua instância ao WhatsApp, acesse as configurações da instância no painel da EvolutionAPI e:

- Adicione o seguinte webhook:

```
http://bot:8000/webhook
```

- Habilite o evento `MESSAGES_UPSERT`

---

### Dúvidas ou melhorias?
Fique à vontade para abrir issues ou contribuir com o projeto.
