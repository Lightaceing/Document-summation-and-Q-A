# A RAG for Document summation and answering queries from those documents

## Features

### Text_Transformation Directory

-Extracts text from a file.
-Splits the text into various chunks for indexing and further processing.

### UI

-Uses _streamlit_ to prompt for queries and provides answers.

## Pipeline

Extracts text -> Splits into chunks -> Encodes the chunks -> Does L2 indexing -> Prompts query -> Gives best ranked chunk.

## Status

🚧 This project is currently a work in progress.  
Several features and improvements are yet to be implemented.

Stay tuned for updates
