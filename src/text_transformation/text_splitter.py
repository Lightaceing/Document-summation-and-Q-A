from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter_config = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
)


# text = "LangChain is a powerful framework for developing applications powered by language models. It enables developers to chain together components like LLMs, prompts, and memory to create advanced conversational AI systems."




def split_text(text):
    """
    returns list with each chunk in each index
    
    """
    chunks = text_splitter_config.split_text(text)
    return chunks


