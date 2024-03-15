import pydantic
import fastapi
import fastapi.middleware.cors
import os
import datetime

app = fastapi.FastAPI()
app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    # Allow the frontend's origin to make requests to the backend.
    # For information on this env var, see process-compose.yml.
    allow_origins=[os.environ.get("CORS_ORIGIN", "*")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EchoRequest(pydantic.BaseModel):
    message: str

class EchoResponse(pydantic.BaseModel):
    message: str
    time: datetime.datetime

@app.post("/api/echo")
def echo(req: EchoRequest) -> EchoResponse:
    time = datetime.datetime.now()
    return EchoResponse(message=req.message, time=time)
