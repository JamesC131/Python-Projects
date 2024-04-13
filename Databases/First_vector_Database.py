import chromadb
chroma_client = chromadb.Client()


collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=["Document_1", "Document_2"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)

# results = collection.query(
#     query_texts=["This is a query document"],
#     n_results=2
# )