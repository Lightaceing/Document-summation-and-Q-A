from text_transformation.text_extraction import *
from text_transformation.text_splitter import *
from sentence_transformers import SentenceTransformer
from UI.stream import *
import faiss


# text = read_pdf("../documents/AReviewOnDatabaseSecurity.pdf", 0)
text = read_all_pages("../documents/AReviewOnDatabaseSecurity.pdf")
chunks = split_text(text)

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

# print(len(embeddings))        # should match number of chunks
# print(len(embeddings[0]))     # vector size (e.g. 384)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

faiss.write_index(index, "my_index.bin")

# query = "Why has database security issues have been more complex ? "
# loaded_index = faiss.read_index("my_index.bin")

query = ask_query()
query_embedding = model.encode([query])

D, I = index.search(query_embedding, k=5)

retrieved_chunks = [chunks[i] for i in I[0]]


for chunk in retrieved_chunks:
    show_text(chunk)
