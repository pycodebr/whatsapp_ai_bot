from fastapi import FastAPI, Request

from message_buffer import buffer_message


app = FastAPI()

@app.post('/webhook')
async def webhook(request: Request):
    data = await request.json()
    chat_id = data.get('data').get('key').get('remoteJid')
    message = data.get('data').get('message').get('conversation')

    if chat_id and message and not '@g.us' in chat_id:
        await buffer_message(
            chat_id=chat_id,
            message=message,
        )

    return {'status': 'ok'}
