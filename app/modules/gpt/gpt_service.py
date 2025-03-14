import openai
import os
from app.config import Settings

class GPTService:
    """
    Serviço de integração com o OpenAI GPT-4.
    """

    def __init__(self):
        """Inicializa o serviço com a chave da API OpenAI."""
        self.client = openai.OpenAI(api_key=Settings.OPENAI_API_KEY)

    def gerar_resposta(self, mensagem_usuario):
        """
        Envia uma mensagem para o GPT-4 e retorna a resposta.

        Parâmetros:
            mensagem_usuario (str): Texto enviado pelo usuário.

        Retorno:
            str: Resposta gerada pelo GPT-4.
        """
        try:
            resposta = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Você é um assistente imobiliário chamado Agente Toca. Seu objetivo é ajudar clientes a encontrar imóveis, tirar dúvidas e facilitar o cadastro no CRM."},
                    {"role": "user", "content": mensagem_usuario}
                ],
                temperature=0.7
            )
            return resposta.choices[0].message.content
        except Exception as e:
            print(f"❌ [ERRO] Falha ao gerar resposta do GPT: {e}")
            return "Desculpe, ocorreu um erro ao processar sua solicitação. Tente novamente mais tarde."

# Criar uma instância do serviço GPT
gpt_service = GPTService()
