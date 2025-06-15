# Travel.AI Chat Application

Travel.AI is a conversational AI-powered mobile application designed to assist users with travel-related queries using a chatbot. It combines a React Native frontend with a Flask-based RAG (Retrieval-Augmented Generation) backend that processes travel questions using a custom knowledge base (`data.pdf`).

---

## 🗂️ Project Structure

```
TravelChatApp/
├── backend/
│   ├── app/
│   │   ├── .env              # Environment variables for HuggingFace & Flask
│   │   ├── data.pdf          # Custom travel knowledge base (RAG)
│   │   ├── app.py            # Main Flask application using LangChain RAG
│   │   ├── requirements.txt  # Python dependencies
│   └── README.md             # Backend documentation
├── frontend/
│   ├── TravelChatapp/
│   │   ├── app/              # React Native source code
│   └── README.md             # Frontend documentation
└── README.md                 # Global documentation (this file)
```

---

## ✅ Features

- RAG-based QA system powered by `data.pdf`
- Natural language queries handled by HuggingFace LLM (Mistral)
- Real-time responses in a mobile interface
- Custom travel corpus with FAISS vector search

---

## ⚙️ Prerequisites

### Backend
- Python 3.x
- Flask
- Virtualenv
- `data.pdf` (must be placed inside `backend/app`)

### Frontend
- Node.js
- React Native CLI
- Expo (optional)

---

## 🚀 Setup Instructions

### 🔧 Backend Setup

```bash
cd backend/app
python3 -m venv env
source env/bin/activate     # Linux/MacOS
# OR
env\Scripts\activate        # Windows

pip install -r requirements.txt
```

Create a `.env` file with your Hugging Face token:
```bash
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

Run the Flask server:
```bash
python app.py
```
Access: `http://127.0.0.1:5000/get_response`

---

### 📱 Frontend Setup

```bash
cd frontend/TravelChatapp
npm install
```

Run the app:
```bash
npm start
# or
npx react-native run-android
npx react-native run-ios
```

Update the API URL inside the frontend app to point to `http://127.0.0.1:5000` or your deployed backend.

---

## 🧠 How It Works

1. User types a question in the mobile app
2. The query is sent to the Flask backend
3. The backend:
   - Loads `data.pdf`
   - Uses FAISS to retrieve relevant context
   - Sends query + context to Mistral (via HuggingFace)
   - Returns answer
4. The frontend displays the AI-generated answer

---

## 📸 App Screenshots

Images are located in the `frontend/assets/` folder.

### Home (Suggestions)
![Home](./frontend/assets/home.png)

### New Chat Screen
![New Chat](./frontend/assets/new_conv.png)

### Typing Response
![Typing](./frontend/assets/example_chat.png)

### Empty Chats
![Empty Chats](./frontend/assets/empty_chats.png)

### Profile View
![Profile](./frontend/assets/profile.png)

---

## 📦 Dependencies

### Backend
- Flask, Flask-Cors
- langchain, langchain-community
- FAISS
- HuggingFace Hub

### Frontend
- React Native
- Gifted Chat
- Axios
- Expo (if used)

---

## 📬 API Endpoint

### POST `/get_response`
```json
{
  "user_query": "Quelle est la meilleure saison pour visiter Marrakech ?"
}
```

Response:
```json
{
  "response": "La meilleure saison pour visiter Marrakech est le printemps (mars à mai)..."
}
```

---

## ✨ Future Improvements
- Add support for multiple document RAG
- Multilingual support
- Voice interface
- Live weather/API integrations

---

## 👤 Author
**Tfares Isam** – Engineering student in AI & Computer Science. Passionate about LLMs, conversational agents, and real-world AI applications.
