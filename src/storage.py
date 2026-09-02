import pickle

def save_chunks(chunks,path):
    with open(path,"wb") as f:
        pickle.dump(chunks,f)


def load_chunks(path):
    with open(path,"rb") as f:
        chunks= pickle.load(f)

    return chunks
