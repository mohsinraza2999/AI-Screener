from sentence_transformers import SentenceTransformer

def get_embedding(resume, model_name='all-MiniLM-L6-v2'):
    """
    Generates and adds a text embedding for each resume's content in the DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing a 'Text Content' column.
        model_name (str): The name of the sentence-transformer model to use.

    Returns:
        pandas.DataFrame: The DataFrame with a new 'Embedding' column.
    """
    if resume:
           
        try:
            # Load the pre-trained model
            model = SentenceTransformer(model_name)
            print(f"Model '{model_name}' loaded successfully.")
            
            # Generate embeddings for the 'Text Content' column
            embeddings = model.encode(resume, show_progress_bar=True)
            
            # Add the embeddings as a new column
            
            
            return embeddings
        except Exception as e:
            print(f"Error generating embeddings: {e}")
            return None
    else:
        print("Error: DataFrame is empty or missing 'Text Content' column.")
        return resume