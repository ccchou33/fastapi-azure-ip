from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

# Store the IP in memory (simple demo)
android_ip = None

class IPData(BaseModel):
    ip: str

# Endpoint for Android to POST its IP
@app.post("/update-ip")
async def update_ip(data: IPData):
    global android_ip
    android_ip = data.ip
    return {"status": "IP received", "ip": android_ip}

# Endpoint to GET the stored IP
@app.get("/get-ip")
async def get_ip():
    if android_ip:
        return {"ip": android_ip}
    return {"error": "No IP stored yet"}
