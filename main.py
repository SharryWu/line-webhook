from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def health_check():
    return "ok"

@app.post("/line/webhook")
async def line_webhook(request: Request):
    body = await request.json()
    print(body)
    return {"status": "ok"}
