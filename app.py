from flask import Flask, request, jsonify,render_template


from chatbot import process_message
from integration import integration_db

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

# Dummy data storage (You should use a database in a real application)
chat_data = {}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_id_str = data.get('user_id')
    message = data.get('message')

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

if __name__ == '__main__':
    app.run(debug=True)
