from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(openai_api_key=api_key)

results = model.predict("what is one plus one?")
print("results: ", results)
