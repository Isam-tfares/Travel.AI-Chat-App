from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Flask app initialization
app = Flask(__name__)

# Load API token and Hugging Face model details
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
task = "text-generation"

# Step 1: Load and index the corpus (data.pdf)
loader = PyPDFLoader("data.pdf")
documents = loader.load()

# Step 2: Convert documents to vectors
embedding_model = HuggingFaceEmbeddings()
vector_store = FAISS.from_documents(documents, embedding_model)
retriever = vector_store.as_retriever()

# Step 3: Prepare prompt and QA chain
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are Travel.AI, a helpful travel assistant that answers questions based only on the following context:

{context}

Question: {question}
Answer as helpfully as possible:
"""
)

llm = HuggingFaceEndpoint(
    huggingfacehub_api_token=api_token,
    repo_id=repo_id,
    task=task
)

rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt_template}
)

# Flask route to handle the get_response API
@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        data = request.get_json()

        if "user_query" not in data:
            return jsonify({"error": "Missing 'user_query' in request"}), 400

        user_query = data["user_query"]

        # Get response from RAG pipeline
        response = rag_chain.run(user_query)
        response = response.strip()

        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
