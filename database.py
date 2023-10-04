import sqlite3
import json



def create_db():
    
    # Connect to or create a SQLite database (if it doesn't exist)
    conn = sqlite3.connect('mydatabase.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Define an SQL command to create a table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS user_chat (
        user_id INTEGER PRIMARY KEY,
        chat_id INTEGER,
        chatbot_history JSON,
        is_complete INTEGER DEFAULT 1
    )
    '''

    # Execute the SQL command to create the table
    cursor.execute(create_table_query)

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

    print("Database and table created successfully.")

# create_db()


def insert_chat_data(user_id, chat_id, chatbot_history_data, is_complete=1):
    # Convert chatbot history data to a JSON string
    chatbot_history_json = json.dumps(chatbot_history_data)
    
    # Connect to the SQLite database
    conn = sqlite3.connect('mydatabase.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Define an SQL command to insert data into the table
    insert_data_query = '''
    INSERT INTO user_chat (user_id, chat_id, chatbot_history, is_complete)
    VALUES (?, ?, ?, ?)
    '''

    # Execute the SQL command to insert the data
    cursor.execute(insert_data_query, (user_id, chat_id, chatbot_history_json, is_complete))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

    print("Data inserted successfully.")


def retrieve_chat_data(user_id, chat_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('mydatabase.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Define an SQL command to retrieve chat data for the given user_id and chat_id
    retrieve_data_query = '''
    SELECT chatbot_history
    FROM user_chat
    WHERE user_id = ? AND chat_id = ?
    '''

    # Execute the SQL command to retrieve the chat history
    cursor.execute(retrieve_data_query, (user_id, chat_id))

    # Fetch the result (chatbot_history JSON string)
    result = cursor.fetchone()

    if result:
        # Convert the JSON string back to a Python list
        chatbot_history_data = json.loads(result[0])
        return chatbot_history_data
    else:
        return None

def update_chat_history(user_id, chat_id, new_history):
    # Convert the new chat history data to a JSON string
    new_history_json = json.dumps(new_history)
    
    # Connect to the SQLite database
    conn = sqlite3.connect('mydatabase.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Define an SQL command to update the chatbot_history column
    update_data_query = '''
    UPDATE user_chat
    SET chatbot_history = ?
    WHERE user_id = ? AND chat_id = ?
    '''

    # Execute the SQL command to update the chat history
    cursor.execute(update_data_query, (new_history_json, user_id, chat_id))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

    print("Chat history updated successfully.")


# # Usage example:
# user_id = 1
# chat_id = 1
# chatbot_history_data = [
#     {'input': 'Hello.'},
#     {'output': "Hi, I'm a Coach designed to offer personalized guidance. Could you please provide your name so we can proceed? (Yes, No)"},
#     {'input': 'Thanks'},
#     {'output': "Hi, I'm a Coach designed to offer personalized guidance. Could you please provide your name so we can proceed? (Yes, No)"},
#     {'input': 'Thanks'},

# ]



# # # Call the function with the provided values
# # insert_chat_data(user_id, chat_id, chatbot_history_data)

# # # Call the function to retrieve chat data
# chat_history = retrieve_chat_data(user_id, chat_id)

# if chat_history:
#     print("Chat History:")
#     for item in chat_history:
#         print(item)
# else:
#     print("Chat data not found.")




# new_chat_history = [
#     {'input': 'Hello, again!'},
#     {'output': "Welcome back! How can I assist you today?"}
# ]

# Call the function to update the chat history
# update_chat_history(user_id, chat_id, new_chat_history)