from flask import Flask, request, jsonify,render_template


from chatbot import process_message
from integration import integration_db
import os

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

# Dummy data storage (You should use a database in a real application)
chat_data = {}

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_id_str = data.get('user_id')
        message = data.get('message')
        print(message)

        print(user_id_str)

        chat_id_str=1

        # Check if user_id and chat_id can be converted to integers
        try:
            user_id = int(user_id_str)
            chat_id = int(chat_id_str)
        except ValueError:
            return jsonify({'error': 'user_id and chat_id must be valid integers'}), 400



        # Message you want to use for generating a response


        # Call the function
        result=integration_db(user_id, chat_id,message)


        # Return a response with just the message
        return jsonify({'message': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/key', methods=['GET'])
def get_openai_api_key():
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    
    if openai_api_key is None:
        # Handle the case where the environment variable is not set
        return jsonify({'error': 'OpenAI API Key is not set in environment variables'}), 400

    return jsonify({'openai_api_key': openai_api_key})

if __name__ == '__main__':
    app.run(debug=True)
