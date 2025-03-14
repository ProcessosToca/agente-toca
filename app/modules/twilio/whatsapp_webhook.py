import time
from fastapi import APIRouter, Request
from fastapi.responses import Response
from app.modules.twilio.twilio_service import TwilioService
from app.modules.gpt.gpt_service import gpt_service

router = APIRouter()

@router.post("/webhook")
async def whatsapp_webhook(request: Request):
    """ 
    Webhook do WhatsApp via Twilio. Recebe mensagens e responde automaticamente com GPT.
    """
    print("\n🔹 [DEBUG] Webhook foi chamado! Esperando mensagem...")  # 🔥 Verificação importante!

    form = await request.form()
    msg = form.get("Body", "").strip() if form.get("Body") else ""
    sender = form.get("From", "")

    print(f"\n🔹 [DEBUG] Mensagem recebida: '{msg}' de {sender}")  # 🔥 Verificação importante!

    # Se o usuário enviar uma mensagem, respondemos com GPT
    if msg:
        resposta_gpt = gpt_service.gerar_resposta(msg)
        TwilioService.send_whatsapp_message(sender, resposta_gpt)
        print(f"✅ [DEBUG] Resposta enviada pelo GPT: {resposta_gpt}")

    return Response(content="OK", media_type="text/xml")
