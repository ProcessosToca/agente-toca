import os
import json
import boto3
from dotenv import load_dotenv

# 🚀 Carrega as variáveis de ambiente do arquivo .env (se estiver rodando localmente)
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".env"))
load_dotenv(dotenv_path)

class Settings:
    """
    Classe centralizada para armazenar as configurações do projeto.

    🔹 Variáveis carregadas do .env (desenvolvimento) ou AWS Secrets Manager (produção).
    🔹 Segurança reforçada para evitar exposição de credenciais.
    """

    # 🔹 Configuração da OpenAI (ChatGPT)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    CLAID_API_KEY = os.getenv("CLAID_API_KEY")  # API para processamento de imagens

    # 🔹 Configurações do AWS S3 (Armazenamento em Nuvem)
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")  # Padrão: us-east-1
    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")  # Nome do Bucket S3
    S3_ORIGINALS_FOLDER = os.getenv("S3_ORIGINALS_FOLDER", "originals")  # Pasta de uploads brutos
    S3_PROCESSED_FOLDER = os.getenv("S3_PROCESSED_FOLDER", "processed")  # Pasta de imagens processadas

    # 🔹 Configurações do Twilio (WhatsApp)
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER", "whatsapp:+14155238886")  # Número padrão do Twilio

    # 🔹 Configuração de Cache (Para armazenar sessões temporárias)
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")  # URL do Redis para cache de sessão

    @classmethod
    def verificar_configuracoes(cls):
        """
        Verifica quais configurações foram carregadas corretamente.

        🔹 Evita expor valores sensíveis diretamente no log.
        🔹 Ajuda a identificar configurações ausentes.
        """
        print("\n🔹 Verificação das Configurações:")
        print(f"✅ OPENAI_API_KEY: {'OK' if cls.OPENAI_API_KEY else '❌ NÃO ENCONTRADA'}")
        print(f"✅ TWILIO_ACCOUNT_SID: {'OK' if cls.TWILIO_ACCOUNT_SID else '❌ NÃO ENCONTRADA'}")
        print(f"✅ TWILIO_AUTH_TOKEN: {'OK' if cls.TWILIO_AUTH_TOKEN else '❌ NÃO ENCONTRADA'}")
        print(f"✅ TWILIO_WHATSAPP_NUMBER: {'OK' if cls.TWILIO_WHATSAPP_NUMBER else '❌ NÃO ENCONTRADO'}")
        print(f"✅ AWS Configurado: {'OK' if cls.AWS_ACCESS_KEY_ID and cls.AWS_SECRET_ACCESS_KEY else '❌ NÃO ENCONTRADO'}")
        print(f"✅ Redis Configurado: {'OK' if cls.REDIS_URL else '❌ NÃO CONFIGURADO'}\n")

    @classmethod
    def carregar_segredos_aws(cls, secret_name):
        """
        Carrega credenciais do AWS Secrets Manager (usado em produção).

        Parâmetros:
            secret_name (str): Nome do segredo no AWS Secrets Manager.

        Retorna:
            dict: Dicionário com os valores das credenciais.

        Exemplo de Uso:
            secrets = Settings.carregar_segredos_aws("meu-segredo")
            OPENAI_API_KEY = secrets["OPENAI_API_KEY"]
        """
        try:
            client = boto3.client("secretsmanager", region_name=cls.AWS_REGION)
            response = client.get_secret_value(SecretId=secret_name)
            secrets = json.loads(response["SecretString"])
            return secrets
        except Exception as e:
            print(f"⚠ [WARNING] Erro ao carregar segredos do AWS: {e}")
            return None  # Retorna None em vez de {}

# Criar uma instância das configurações
settings = Settings()

# Opcional: Executa a verificação ao importar o módulo
Settings.verificar_configuracoes()
