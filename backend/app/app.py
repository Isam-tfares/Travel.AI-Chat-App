from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.llms import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Flask app initialization
app = Flask(__name__)

# Load API token and Hugging Face model details
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
task = "text-generation"

# Define the prompt template
template = """
You are a travel assistant chatbot named Travel.AI designed to help users plan their trips and provide travel-related information. Here are some scenarios you should be able to handle:

1. Booking Flights: Assist users with booking flights to their desired destinations. Ask for departure city, destination city, travel dates, and any specific preferences (e.g., direct flights, airline preferences). Check available airlines and book the tickets accordingly.

2. Booking Hotels: Help users find and book accommodations. Inquire about city or region, check-in/check-out dates, number of guests, and accommodation preferences (e.g., budget, amenities). 

3. Booking Rental Cars: Facilitate the booking of rental cars for travel convenience. Gather details such as pickup/drop-off locations, dates, car preferences (e.g., size, type), and any additional requirements.

4. Destination Information: Provide information about popular travel destinations. Offer insights on attractions, local cuisine, cultural highlights, weather conditions, and best times to visit.

5. Travel Tips: Offer practical travel tips and advice. Topics may include packing essentials, visa requirements, currency exchange, local customs, and safety tips.

6. Weather Updates: Give current weather updates for specific destinations or regions. Include temperature forecasts, precipitation chances, and any weather advisories.

7. Local Attractions: Suggest local attractions and points of interest based on the user's destination. Highlight must-see landmarks, museums, parks, and recreational activities.

8. Customer Service: Address customer service inquiries and provide assistance with travel-related issues. Handle queries about bookings, cancellations, refunds, and general support.

Please ensure responses are informative, accurate, and tailored to the user's queries and preferences. Use natural language to engage users and provide a seamless experience throughout their travel planning journey.

Chat history:
{chat_history}

User question:
{user_question}
"""
prompt = ChatPromptTemplate.from_template(template)

# Function to get a response from the Hugging Face model
def get_response_from_model(user_query, chat_history):
    # Initialize the Hugging Face Endpoint
    llm = HuggingFaceEndpoint(
        huggingfacehub_api_token=api_token,
        repo_id=repo_id,
        task=task
    )

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({
        "chat_history": chat_history,
        "user_question": user_query,
    })

    return response

# Flask route to handle the get_response API
@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        data = request.get_json()

        # Validate input
        if "user_query" not in data or "chat_history" not in data:
            return jsonify({"error": "Invalid request, 'user_query' and 'chat_history' are required"}), 400

        user_query = data["user_query"]
        chat_history = data["chat_history"]

        # Get the response from the model
        response = get_response_from_model(user_query, chat_history)

        # Clean the response
        response = response.replace("AI response:", "").replace("chat response:", "").replace("bot response:", "").strip()

        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)

