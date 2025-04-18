import pickle
import os

DATA_PATH = "data/user_face.pkl"

def save_face(face_encoding):
    os.makedirs("data", exist_ok=True)
    with open(DATA_PATH, "wb") as f:
        pickle.dump(face_encoding, f)

def load_face():
    with open(DATA_PATH, "rb") as f:
        return pickle.load(f)
