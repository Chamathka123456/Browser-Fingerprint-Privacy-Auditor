from fastapi import FastAPI, Request

app = FastAPI(title="Browser Fingerprint Privacy Auditor")

@app.get("/analyze")
async def analyze(request: Request):
    headers = dict(request.headers)
    score = len(headers)
    return {
        "fingerprint_headers": list(headers.keys()),
        "risk_score": score,
        "note": "Higher score means more unique fingerprint surface"
    }
