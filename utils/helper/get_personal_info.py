import chromadb
from chromadb.utils import embedding_functions

def get_personal_info(query:str):
    COLLECTION_NAME = "syll_12"

    client = chromadb.PersistentClient(path="./data")
    client.heartbeat()
    # client.delete_collection(name=COLLECTION_NAME)
    # collection = client.create_collection(name= COLLECTION_NAME, embedding_function=embedding_functions.DefaultEmbeddingFunction())
    collection = client.get_collection(name=COLLECTION_NAME)

    # para = text.split('\n')

    # for index, para in enumerate(para):
    #     if index >= 3:
    #         collection.add(documents=[para], ids = [str(index)])
    q = collection.query(query_texts= [query], n_results=  3)

    results = q["documents"][0]
    return q["documents"][0]