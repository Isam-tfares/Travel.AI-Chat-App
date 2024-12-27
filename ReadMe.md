# Travel.AI Chat Application

Travel.AI is a conversational AI-based mobile application that allows users to interact with a chatbot for travel-related queries. The project is structured into two main parts: a backend powered by Flask and a frontend built with React Native.

---

## Project Structure

```
TravelChatApp/
├── backend/
│   ├── app/
│   │   ├── .env          # Environment variables for Flask
│   │   ├── env/          # Virtual environment folder
│   │   ├── app.py        # Main Flask application
│   │   ├── requirements.txt # Python dependencies
│   └── README.md         # Documentation for the backend
├── frontend/
│   ├── TravelChatapp/
│   │   ├── app/          # React Native application folder
│   └── README.md         # Documentation for the frontend
└── README.md             # Documentation for the entire project
```

---

## Prerequisites

- **Backend:**
  - Python 3.x
  - Flask
  - Virtual environment (`venv`)

- **Frontend:**
  - Node.js
  - React Native CLI
  - Expo (if using Expo)

---

## Setup Instructions

### Backend Setup

1. Navigate to the `backend/app` directory:
   ```bash
   cd backend/app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv env
   source env/bin/activate   # For Linux/MacOS
   env\Scripts\activate      # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the `.env` file:
   - Add your environment-specific variables such as the API keys and other configurations. Example:
     ```
     FLASK_APP=app.py
     FLASK_ENV=development
     ```

5. Start the Flask backend:
   ```bash
   flask run
   ```

   By default, the backend runs on `http://127.0.0.1:5000`.

---

### Frontend Setup

1. Navigate to the `frontend/TravelChatapp` directory:
   ```bash
   cd frontend/TravelChatapp
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React Native app:
   - If using Expo:
     ```bash
     npm start
     ```
   - If using a React Native CLI:
     ```bash
     npx react-native run-android   # For Android
     npx react-native run-ios       # For iOS
     ```

4. Make sure the backend is running and the API URL in the frontend code points to the correct address (e.g., `http://127.0.0.1:5000`).

---

## Usage

1. Open the React Native application on your device or emulator.
2. Begin a conversation with the AI assistant.
3. The AI communicates with the Flask backend to provide intelligent responses.

---

## File Descriptions

### Backend (`backend/app`)
- **`app.py`**: The main Flask application handling requests and responses.
- **`.env`**: Configuration file containing environment-specific variables.
- **`requirements.txt`**: List of Python dependencies required for the backend.

### Frontend (`frontend/TravelChatapp`)
- **`app/`**: Contains the React Native application files.

---

## Dependencies

### Backend
- Flask
- Flask-Cors
- Other dependencies as listed in `requirements.txt`

### Frontend
- React Native
- Gifted Chat
- Expo (if used)
- Other dependencies in `package.json`

---



