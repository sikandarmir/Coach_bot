import os
import openai
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.prompt import PromptTemplate

os.environ['OPENAI_API_KEY'] = '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'

def template_fn(type):
    template_dict={
        "Coach": """
            You are an AI coaching chatbot designed to provide personalized guidance, support, and feedback to individuals aiming to enhance specific skills, achieve goals, or make positive changes in their life and work. Your interactions should always be friendly and welcoming.

            To get started, introduce yourself to the user and ask for their name. Afterward, provide them with options to choose from as the initial response. Keep your responses concise.

            For Example:
            user: Hi
            coaching guide: Hi, I'm a Coach designed to offer personalized guidance. Could you please provide your name so we can proceed? (Yes, No)

            user: Yes
            coaching guide: What's your first name?

            user: 'user_name'

            coaching guide: Hello 'user_name', welcome to the coaching session! How can I assist you today? You can choose from the following options:
            1. Set a new goal.
            2. Improve existing skills.
            3. Make positive changes in your life or work.
            Please enter the number corresponding to your choice.

            {history}
            user: {input}
            coaching guide:
        """
    }
    template=template_dict[type]
    return template

def process_message(history_list, message, type='Coach'):
    # Get the Template
    template=template_fn(type)
    PROMPT = PromptTemplate(
        input_variables=["history", "input"], template=template
    )
    llm = ChatOpenAI(temperature=0.0)
    memory = ConversationBufferMemory()
    conversation = ConversationChain(
        prompt=PROMPT,
        llm=llm,
        memory=memory,
        verbose=True
    )
    for i in range(0, len(history_list), 2):
        dict1 = history_list[i]
        dict2 = history_list[i+1]
        print('\n')
        memory.save_context(dict1, dict2)
        memory.load_memory_variables({})
    res=conversation.predict(input=message)
    return res

# # Sample history_list with dummy conversation history
# history_list = [
#     {'input':"Hello."},
#     {'output':"Hi, I'm a Coach designed to offer personalized guidance. Could you please provide your name so we can proceed? (Yes, No)"},
# ]
# Message you want to use for generating a response
# message = "Thanks"

# Call the function
# result = process_message(history_list, message, type='Coach')

# print(result)