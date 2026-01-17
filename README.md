# Browser Fingerprint Privacy Auditor

An ethical hacking tool that analyzes browser fingerprinting signals (headers, JS APIs, TLS hints)
to estimate user trackability and privacy exposure. Built for privacy research and blue-team defense.

How to run
pip install -r requirements.txt
uvicorn app.main:app --reload

Open in browser:
http://127.0.0.1:8000/analyze
