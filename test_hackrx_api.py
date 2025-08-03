import requests

# 🔁 Replace with your actual deployed URL
API_URL = "http://localhost:8000/hackrx/run"

# 🔐 Replace with your actual token (from .env or platform)
HEADERS = {
    "Authorization": "Bearer 71bb650c7118766ab68c3df4923475c4cddb449b7332aa8cefb2d48aa3554e4b",
    "Content-Type": "application/json"
}

# 📄 Example document & questions
payload = {
    "documents": "https://hackrx.blob.core.windows.net/assets/Arogya%20Sanjeevani%20Policy%20-%20CIN%20-%20U10200WB1906GOI001713%201.pdf?sv=2023-01-03&st=2025-07-21T08%3A29%3A02Z&se=2025-09-22T08%3A29%3A00Z&sr=b&sp=r&sig=nzrz1K9Iurt%2BBXom%2FB%2BMPTFMFP3PRnIvEsipAX10Ig4%3D",
    "questions": [
        "What is the waiting period for cataract surgery?",
        "Does the policy cover AYUSH treatments?",
        "What is the No Claim Discount benefit?"
    ]
}

response = requests.post(API_URL, json=payload, headers=HEADERS)

print("Status:", response.status_code)
print("Response JSON:\n", response.json())
