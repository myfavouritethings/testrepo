from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from whitenoise import WhiteNoise

app = FastAPI()

# Configure CORS for development (React dev server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def read_root():
    return {"status": "ok"}

# Mount WhiteNoise to serve static files from the 'static' directory
# This will be used in the production Docker container
# The frontend build will be placed in /app/static
try:
    app.mount("/", WhiteNoise(directory="static", html=True), name="static")
except:
    print("Could not find static directory, serving API only.")

