from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Qdrant

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

class Embedding:
    def __init__(self, config):
        self.vectorstore = None
        self.QDRANT_KEY = config.QDRANT_API_KEY
        self.QDRANT_URL = config.QDRANT_URL
        self.logger = config.logger

    def embed(self, pdf_path):
        # Load and chunk PDF
        loader = PyPDFLoader(pdf_path)
        pages = loader.load()
        self.logger.info(f"@embedding.py: Loaded {len(pages)} pages from PDF.")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = text_splitter.split_documents(pages)

        # Embedding model
        embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        # Instantiate Qdrant client
        qdrant = QdrantClient(
            url=self.QDRANT_URL, 
            api_key=self.QDRANT_KEY
        )
        self.logger.info(f"@embedding.py: Succesfully Instantiated Qdrant client.")

        # Create collection if not existent
        qdrant.recreate_collection(
            collection_name="harvard_guide",
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

        # Create vectorstore
        vectorstore = Qdrant(
            client=qdrant,
            collection_name="harvard_guide",
            embeddings=embedding,
        )
        # Add documents to vectorstore
        vectorstore.add_documents(docs)
        self.vectorstore = vectorstore
        self.logger.info(f"@embedding.py: Succesfully added documents to vectorstore.")

    def search(self, query):
        if not self.vectorstore:
            self.logger.warning(f"@embedding.py: Vectorstore not initialized. Please call embed() first.")
            return ""
        retrieved_docs = self.vectorstore.similarity_search(query, k=3)
        self.logger.info(f"@embedding.py: Succesfully retrieved documents.")
        context = "\n".join([doc.page_content for doc in retrieved_docs])
        return context