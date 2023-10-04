from chatbot import process_message
from database import retrieve_chat_data, update_chat_history, insert_chat_data

# Sample history_list with dummy conversation history
initial_history_list = [
    {'input':"Hello."},
    {'output':"Hi, I'm a Coach designed to offer personalized guidance. Could you please provide your name so we can proceed? (Yes, No)"},
]

history_list=[]


def integration_db(user_id, chat_id,message, is_complete=1):
    chat_history = retrieve_chat_data(user_id, chat_id)


    if chat_history:

        print("Chat History is available:")
        result = process_message(chat_history, message, type='Coach')




        print(chat_history)

        input_msg={'input':message}
        out_msg={'output':result}

        chat_history.append(input_msg)
        chat_history.append(out_msg)

        # Call the function to update the chat history
        update_chat_history(user_id, chat_id, chat_history)
  
    
    else:
    
        print("Chat History is not available:")
        # Call the function with the provided values
        insert_chat_data(user_id, chat_id, initial_history_list)

        result = process_message(initial_history_list, message, type='Coach')

        input_msg={'input':message}
        out_msg={'output':result}

        initial_history_list.append(input_msg)
        initial_history_list.append(out_msg)

        # Call the function to update the chat history
        update_chat_history(user_id, chat_id, initial_history_list)



    return result



# user_id = 4
# chat_id = 1

# message="what's my name i prooivide you earliy?."


# print(result)
