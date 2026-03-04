import os
from dotenv import load_dotenv
load_dotenv()

# ── Neo4j credentials ──────────────────────────────────────────────
NEO4J_URL  = "neo4j+s://4c4b3423.databases.neo4j.io"
NEO4J_USER = "4c4b3423"
NEO4J_PASS = "Z6vdj_x_TidjsEi4exhDUVMwQBjElFiYL5ql3Qw5kbk"
NEO4J_DB   = "4c4b3423"

# Set ALL possible env var names langchain_neo4j might read
os.environ["NEO4J_URI"]      = NEO4J_URL
os.environ["NEO4J_URL"]      = NEO4J_URL
os.environ["NEO4J_USERNAME"] = NEO4J_USER
os.environ["NEO4J_PASSWORD"] = NEO4J_PASS
os.environ["NEO4J_DATABASE"] = NEO4J_DB

# ── Monkey-patch Neo4jGraph BEFORE mem0 imports it ─────────────────
import langchain_neo4j.graphs.neo4j_graph as _ng

_orig_init = _ng.Neo4jGraph.__init__

def _patched_init(self, url=None, username=None, password=None, database=None, **kwargs):
    print(f"[PATCH] Connecting to Neo4j: {NEO4J_URL} | db={NEO4J_DB}")
    _orig_init(
        self,
        url=NEO4J_URL,
        username=NEO4J_USER,
        password=NEO4J_PASS,
        database=NEO4J_DB,
        **kwargs
    )

_ng.Neo4jGraph.__init__ = _patched_init

# ── Now safe to import mem0 ────────────────────────────────────────
from mem0 import Memory
from openai import OpenAI

client = OpenAI()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "text-embedding-3-small"
        }
    },
    "llm": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "gpt-4.1"
        }
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url":      NEO4J_URL,
            "username": NEO4J_USER,
            "password": NEO4J_PASS,
            "database": NEO4J_DB,
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        }
    }
}

print("Initializing memory client...")
mem_client = Memory.from_config(config)
print("✅ Memory client ready!\n")

while True:
    user_query = input("You: ").strip()
    if not user_query:
        continue
    if user_query.lower() in ("exit", "quit"):
        print("Goodbye!")
        break

    # Search existing memories
    search_memory = mem_client.search(query=user_query, user_id="manjeet")
    results = search_memory.get("results", [])
    memories = [f"- {mem.get('memory')}" for mem in results]

    if memories:
        print(f"\n🧠 Found {len(memories)} relevant memories")

    SYSTEM_PROMPT = f"""You are an AI assistant with long-term memory.

Here are past memories about the user:
{chr(10).join(memories) if memories else "No past memories yet."}

Use this information naturally when answering the user."""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )

    ai_response = response.choices[0].message.content
    print(f"\nAI: {ai_response}\n")

    mem_client.add(
        user_id="manjeet",
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response}
        ]
    )
    print("💾 Memory saved.\n")