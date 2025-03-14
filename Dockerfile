# Usar uma imagem leve do Python
FROM python:3.10

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto para dentro do container
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta usada pelo FastAPI/Uvicorn
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
