from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    url="https://81bf84cf-5327-4933-b43c-ae7b20e89a9b.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.AfnKl_B35LNySbG_DIuAXVPS5oumhrwHBIVP_g0GU9E",
)

print(qdrant_client.get_collections())