#!/usr/bin/env python3
import sys
import fitz          # PyMuPDF
import faiss
import numpy as np
from transformers import AutoTokenizer

def load_and_chunk(pdf_paths, tokenizer, chunk_size=600):
    texts = []
    for path in pdf_paths:
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        tokens = tokenizer.tokenize(text)
        # dela i chunk_size-tokenbitar
        for i in range(0, len(tokens), chunk_size):
            chunk = tokens[i:i+chunk_size]
            texts.append(tokenizer.convert_tokens_to_string(chunk))
    return texts

def embed_chunks(chunks, tokenizer):
    # Dummy-embedding: One-hot eller slumpmässigt för test
    # Här bör du använda en riktig embedder
    return np.random.rand(len(chunks), 768).astype('float32')

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("pdfs", nargs="+", help="PDF-filer att processa")
    parser.add_argument("--chunk-size", type=int, default=600)
    parser.add_argument("--output", type=str, default="faiss_index.bin")
    args = parser.parse_args()

    print("⏳ Laddar tokenizer…")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

    print(f"⏳ Chunkar {len(args.pdfs)} PDF:er…")
    chunks = load_and_chunk(args.pdfs, tokenizer, args.chunk_size)
    print(f"✅ Skapade {len(chunks)} text-chunks")

    print("⏳ Embeddar chunks…")
    vectors = embed_chunks(chunks, tokenizer)
    dim = vectors.shape[1]

    print("⏳ Skapar FAISS-index…")
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)

    print(f"⏳ Sparar index till {args.output}…")
    faiss.write_index(index, args.output)
    print("✅ FAISS-index sparat")

if __name__ == "__main__":
    main()



