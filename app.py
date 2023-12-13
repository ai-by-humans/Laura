from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# Define the character's name
character = "Laura"

# Define the system message content with the character's name
system_message = f"""
#instructions for model to behave as {character} in a conversation.
Text transcript of a never-ending conversation between the user and {character}. 
In the transcript, gestures and other non-verbal actions are written between asterisks (for example, *waves hello* or *moves closer*).
"""

def chat_with_model(messages, temperature=0.7):
    """
    Send a chat message to the model and maintain history for context.

    :param messages: List of message dictionaries representing the chat history.
    :param temperature: The randomness of the response.
    :return: The model's response as a string.
    """
    completion = client.chat.completions.create(
        model="local-model",  # Replace with your specific model
        messages=messages,
        temperature=temperature,
    )
    return completion.choices[0].message

# Initialize an empty chat history
chat_history = []

# Adding the system message to the chat history
chat_history.append({"role": "system", "content": system_message})

# Function to print the conversation in a formatted way
def print_conversation(user_message, model_response, character_name):
    print("\n----- Conversation -----")
    print("User: " + user_message)
    print(f"Model ({character_name}): " + model_response)
    print("------------------------\n")

# Start an interactive chat session
while True:
    # User input
    user_input = input("User: ")
    chat_history.append({"role": "user", "content": user_input})

    # Get the model's response
    model_response = chat_with_model(chat_history)

    # Format and print the conversation
    print_conversation(user_input, model_response.content, character)

    # Update chat history with the model's response
    chat_history.append({"role": "assistant", "content": model_response.content})
