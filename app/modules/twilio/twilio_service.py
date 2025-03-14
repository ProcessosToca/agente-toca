import json
from twilio.rest import Client
from app.config import Settings

# 🔑 Configurar cliente Twilio
twilio_client = Client(Settings.TWILIO_ACCOUNT_SID, Settings.TWILIO_AUTH_TOKEN)

class TwilioService:
    """
    Serviço para envio de mensagens via WhatsApp usando Twilio.
    """

    @staticmethod
    def send_whatsapp_message(to_number: str, message_body: str):
        """
        Envia uma mensagem simples via WhatsApp pelo Twilio.

        :param to_number: Número do destinatário (ex: 'whatsapp:+5511999999999')
        :param message_body: Texto da mensagem
        """
        try:
            message = twilio_client.messages.create(
                from_=Settings.TWILIO_WHATSAPP_NUMBER,
                to=to_number,
                body=message_body
            )
            print(f"✅ Mensagem enviada para {to_number}. SID: {message.sid}")
            return True
        except Exception as e:
            print(f"❌ [ERRO] Falha ao enviar mensagem para {to_number}: {e}")
            return False

    @staticmethod
    def send_whatsapp_media(to_number: str, media_url: str):
        """
        Envia uma mensagem de WhatsApp com uma imagem/media.

        :param to_number: Número do destinatário
        :param media_url: URL da mídia a ser enviada
        """
        try:
            message = twilio_client.messages.create(
                from_=Settings.TWILIO_WHATSAPP_NUMBER,
                to=to_number,
                media_url=[media_url],
                body="✅ Sua imagem foi tratada com sucesso, aqui está o resultado:"
            )
            print(f"✅ Mídia enviada para {to_number}. SID: {message.sid}")
            return True
        except Exception as e:
            print(f"❌ [ERRO] Falha ao enviar mídia para {to_number}: {e}")
            return False

    @staticmethod
    def send_whatsapp_template(to_number: str, template_sid: str):
        """
        Envia uma mensagem de WhatsApp com um template interativo.

        :param to_number: Número do destinatário
        :param template_sid: O Template SID configurado no Twilio
        """
        try:
            message = twilio_client.messages.create(
                from_=Settings.TWILIO_WHATSAPP_NUMBER,
                to=to_number,
                content_sid=template_sid,
                content_variables=json.dumps({})
            )
            print(f"✅ Template {template_sid} enviado para {to_number}. SID: {message.sid}")
            return True
        except Exception as e:
            print(f"❌ [ERRO] Falha ao enviar template para {to_number}: {e}")
            return False
