from dotenv import load_dotenv
import os
load_dotenv()

from agno.knowledge.agent import AgentKnowledge
from agno.vectordb.qdrant.qdrant import Qdrant
from agno.embedder.ollama import OllamaEmbedder

# Embed sentence in database
embedder = OllamaEmbedder(id="nomic-embed-text:latest", dimensions=768)

url=os.getenv("QDRANT_URL")
api_key=os.getenv("QDRANT_API_KEY")
collection_name="azure-data-factory"

qdrant = Qdrant(url=url, api_key=api_key, collection=collection_name, embedder=embedder)

knowledge_base = AgentKnowledge(vector_db=qdrant)