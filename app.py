from fastapi import FastAPI, Request

from chains import get_conversational_rag_chain
from evolution_api import send_whatsapp_message


app = FastAPI()

conversational_rag_chain = get_conversational_rag_chain()

@app.post('/webhook')
async def webhook(request: Request):
    data = await request.json()
    chat_id = data.get('data').get('key').get('remoteJid')
    message = data.get('data').get('message').get('conversation')

    if chat_id and message and not '@g.us' in chat_id:
        ai_response = conversational_rag_chain.invoke(
            input={'input': message},
            config={'configurable': {'session_id': chat_id}},
        )['answer']

        send_whatsapp_message(
            number=chat_id,
            text=ai_response,
        )

    return {'status': 'ok'}
