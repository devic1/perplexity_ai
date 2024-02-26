import ollama
from qdrant_client import models, QdrantClient
from tqdm import tqdm


qdrant = QdrantClient(":memory:")
class RAG:
    def __init__(self):
        self.collection_name = "temp_collection"
        None
    def initialize_db(self):
        qdrant.recreate_collection(
        collection_name=self.collection_name,
        vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE,
            )
        )
    def delete_db(self):
        qdrant.delete_collection(collection_name=self.collection_name)


    def rag_embeddings(self,context: str):
        start_res = []
        chunk_size = 1000
        for i in range(0,len(context),chunk_size):
            start_res.append(context[i:i+chunk_size])
        qdrant.upload_records(
            collection_name=self.collection_name,
            records=[
                models.Record(
                    id=idx, vector=ollama.embeddings(model='nomic-embed-text:137m-v1.5-fp16', prompt=doc,keep_alive=True)["embedding"], payload={"para":doc}
                )
                for idx, doc in enumerate(tqdm(start_res))
                ],
            )

    def rag_search(self,query: str) -> str:
        hits = qdrant.search(
            collection_name=self.collection_name,
            query_vector=ollama.embeddings(model='nomic-embed-text:137m-v1.5-fp16', prompt=query,keep_alive=True)["embedding"],
        limit=8,
        )
        final_result = ""
        for hit in hits:
            final_result += hit.payload["para"]
        return final_result
