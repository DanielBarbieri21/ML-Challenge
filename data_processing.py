import pickle
import numpy as np

def load_data(file_path):
    """Carrega os dados do arquivo pickle e os transforma em um formato adequado."""
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    
    X, y = [], []
    for syndrome_id, subjects in data.items():
        for subject_id, images in subjects.items():
            for image_id, embedding in images.items():
                X.append(embedding)
                y.append(syndrome_id)
    
    return np.array(X), np.array(y)

if __name__ == "__main__":
    file_path = "mini_gm_public_v0.1.p" 
    X, y = load_data(file_path)
    print(f"Dados carregados: {X.shape[0]} amostras, {X.shape[1]} features")