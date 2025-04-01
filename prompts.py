from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


contextualize_prompt = ChatPromptTemplate.from_messages([
    (
        'system',
        'Dado um histórico de conversa e a pergunta mais recente do usuário, '
        'que pode fazer referência ao contexto anterior, formule uma pergunta '
        'independente, que possa ser compreendida sem o histórico da conversa. '
        'NÃO responda à pergunta — apenas reformule se necessário; caso contrário, ' 
        'retorne a pergunta como está.'
    ),
    MessagesPlaceholder('chat_history'),
    ('human', '{input}'),
])

qa_prompt = ChatPromptTemplate.from_messages([
    (
        'system',
        'Você é um assistente da PycodeBR e deve tirar dúvidas sobre o curso Django Master. '
        'Use os seguintes trechos de contexto recuperado para responder à pergunta. '
        'Se você não souber a resposta, diga que não sabe. '
        'Use no máximo três frases e mantenha a resposta concisa.'
        '{context}'
    ),
    MessagesPlaceholder('chat_history'),
    ('human', '{input}'),
])
