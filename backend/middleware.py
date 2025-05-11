from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.main import get_drivers

app = FastAPI()

# Allow localhost:5173 for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/drivers")
async def load_drivers():
    return await get_drivers()