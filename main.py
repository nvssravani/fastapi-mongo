from fastapi import FastAPI
import ssl
import uvicorn
from app.server.routes.student import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouter, tags=["Student"], prefix="/student")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
if __name__ == "__main__":
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile="./open-ssl-certificate/certificate.pem", keyfile="./open-ssl-certificate/key.pem")
    uvicorn.run("main:app", host="localhost", port=443, reload=True, ssl_keyfile="./open-ssl-certificate/key.pem", ssl_certfile="./open-ssl-certificate/certificate.pem")
