import uvicorn
from fastapi import FastAPI
from app.modules.twilio.whatsapp_webhook import router as whatsapp_router

# 🚀 Inicializar FastAPI
app = FastAPI(title="Agente Toca API")

# 🔗 Registrar as rotas do webhook do WhatsApp
app.include_router(whatsapp_router, prefix="/twilio")

@app.get("/")
async def root():
    return {"message": "🚀 Agente Toca API está rodando!"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
