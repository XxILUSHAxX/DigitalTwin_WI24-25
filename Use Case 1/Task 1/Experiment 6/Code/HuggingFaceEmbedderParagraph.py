from transformers import AutoTokenizer, AutoModel
import torch

"""
HugginFaceEmbedder is an embeding model which focuses on meaning and is not very optimized for
token matching.
"""
class HuggingFaceEmbedder:
    """Wrapper class for Hugging Face transformer embedding generation."""
    def __init__(self, model_name="distilroberta-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def encode(self, texts):
        if isinstance(texts, str):
            texts = [texts]
        inputs = self.tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        # Return CLS token embeddings for simplicity
        return outputs.last_hidden_state[:, 0, :].numpy()

