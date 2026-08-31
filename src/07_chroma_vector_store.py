chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.create_collection(name="my_collections")

ids = []

for i in range(len(chunks)):
    ids.append(str(i))

collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings.tolist()
)

print(collection.count())
