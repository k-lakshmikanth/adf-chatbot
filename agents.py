from dotenv import load_dotenv
import os
from agno.agent import Agent
from knowledge_base import knowledge_base
from agno.models.ollama import Ollama
from agno.storage.yaml import YamlStorage
from agno.playground import Playground, serve_playground_app

load_dotenv()
os.environ.pop("ENV", None)

agent = Agent(
    name="Azure Data Factory Assistant",
    description="An assistant to help me with Azure Data Factory and related tasks.",
    knowledge=knowledge_base,
    model=Ollama("qwen2.5:14b"),
    storage=YamlStorage(dir_path="sessions/agent_sessions_yaml"),
    markdown=True,
    add_history_to_messages=True,
    search_knowledge=True,
)

app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("agents:app", reload=True)
