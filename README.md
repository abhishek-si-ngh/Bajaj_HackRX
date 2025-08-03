
# 🚀 HackRx 6.0 – Policy-Aware Insurance Q&A API

This project is a **FastAPI-based** solution designed for the **Bajaj HackRx 6.0 hackathon**, providing a production-grade API to answer insurance-related questions based on built-in policy knowledge and optionally user-provided policy documents.

🔗 **Live Demo**: [https://bajaj-hackrx-api.onrender.com](https://bajaj-hackrx-api.onrender.com)  
📄 **Swagger UI**: [https://bajaj-hackrx-api.onrender.com/docs](https://bajaj-hackrx-api.onrender.com/docs)  
📘 **Code2Tutorial Link**: [Code2Tutorial - Project Guide](https://code2tutorial.com/tutorial/60a9df96-2a79-4ff8-8939-5290fe787e39/index.md)

---

## ✨ Features

- ✅ 80%+ accuracy using a built-in insurance knowledge base
- 📄 Accepts policy documents via URL
- 🛡️ Secured with Bearer Token Authentication
- 🚀 Dockerized & deployable on Render
- 🧠 Handles up to 10 questions in a single request
- ⚙️ Graceful error handling and logging
- 🌐 Fully documented via OpenAPI at `/docs`

---

## 🧪 Sample API Usage

### ▶️ POST `/hackrx/run`

**Headers:**
```http
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json
```

**Request Body:**
```json
{
  "documents": "https://example.com/sample_policy.pdf",
  "questions": [
    "What is the waiting period for cataract surgery?",
    "Does the policy cover AYUSH treatments?"
  ]
}
```

**Sample Response:**
```json
{
  "answers": [
    "The policy has a specific waiting period of two (2) years for cataract surgery...",
    "Yes, the policy covers medical expenses under AYUSH systems of medicine..."
  ]
}
```

---

## 🛠️ Local Development Setup

```bash
git clone https://github.com/abhishek-si-ngh/Bajaj_HackRX.git
cd Bajaj_HackRX

# Optional but recommended
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate

pip install -r requirements.txt

# Run the API
uvicorn hackrx_final_robust_api_cleaned:app --reload
```

Access API at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker Deployment

```bash
docker build -t hackrx-api .
docker run -d -p 8000:8000 --env HACKRX_TOKEN=your_token_here hackrx-api
```

---

## 📦 Render Deployment

- Connect GitHub repo
- Choose Docker environment
- Set `HACKRX_TOKEN` as an environment variable
- Expose port `8000`
- Auto-deploy supported

---

## 🔐 Environment Variables

| Variable       | Required | Description                          |
|----------------|----------|--------------------------------------|
| `HACKRX_TOKEN` | ✅        | Bearer token for securing endpoints  |

---

## 👥 Contributors

- **Abhishek Singh**  
- **Abhiyanshu Anand**  
- **Sanskar Singh**  
- **Siddharth Tripathi**  
- Team: HackerXHacker

---

## 📄 License

This project is for educational/demo purposes for HackRx 6.0.

---
