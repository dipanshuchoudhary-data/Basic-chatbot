## MY CODE 
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Load API token securely
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not api_token:
    raise ValueError("Missing Hugging Face API token in environment variables.")

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-small",
    huggingfacehub_api_token="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",
    model_kwargs={"temperature": 0.7, "max_length": 256}
)

# Start the conversation
chat_history = [SystemMessage(content="You are a roaster AI assistant.")]

while True:
    user_input = input("You : ")
    if user_input.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=user_input))
    result = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI : ", result.content)

# Final history log
print("\nChat History:")
for msg in chat_history:
    print(f"{msg.type.capitalize()} - {msg.content}")