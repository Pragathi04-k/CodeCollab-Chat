from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "AIzaSyBoGyn0GpP-DdznFSVg8Bow8EDRHKdg1yE"))

# ---- Gemini Chatbot Function ----
def ask_gemini(query):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"Gemini error: {e}"


# ---- Flask Routes ----
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"]) 
def get_bot_response():
    user_input = request.form["msg"]
    response = ask_gemini(user_input)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
    

