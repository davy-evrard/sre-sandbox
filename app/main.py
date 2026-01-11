import time
import random
from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# This sets up the instrumentator to automatically track every request
instrumentator = Instrumentator().instrument(app)

# This exposes the /metrics endpoint
@app.on_event("startup")
async def _startup():
    instrumentator.expose(app)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "System is healthy"}

@app.get("/risky")
def read_risky():
    """
    This endpoint simulates a flaky service.
    - 20% chance of 500 Error (Server Crash)
    - 20% chance of high latency (Slow Database)
    """
    val = random.random()
    
    # Simulate a crash (Error Budget Burn)
    if val < 0.2:
        raise HTTPException(status_code=500, detail="Internal Server Error: Something broke!")
    
    # Simulate latency (Toil for the user)
    if val < 0.4:
        time.sleep(2) # Sleep for 2 seconds
        return {"status": "slow", "message": "Sorry that took so long."}

    return {"status": "success", "message": "Everything worked perfectly."}
