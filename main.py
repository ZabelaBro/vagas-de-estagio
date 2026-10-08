from fastapi import FastAPI
from app.routes import empresas_routes, vagas_routes

app = FastAPI(title="API Vagas de Estágio")

app.include_router(empresas_routes.router)
app.include_router(vagas_routes.router)

