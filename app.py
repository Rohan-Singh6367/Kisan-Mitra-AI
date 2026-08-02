from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

client = genai.Client(
    api_key="AQ.Ab8RN6J6JpCkNw5kLVOEXk9elFy9GX5MP_brput_UBKe3pGhrw"
)

def get_response(message):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            You are an Agriculture Expert AI.

            Answer in both Hindi and English.

            Give:
            1. Problem Analysis
            2. Recommended Action
            3. Precautions

            Farmer Question:
            {message}
            """
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_response = get_response(user_message)

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)