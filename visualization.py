import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from data_processing import load_data

def plot_tsne(X, y):
    """Reduz a dimensionalidade dos embeddings para 2D usando t-SNE e plota o gráfico."""
    tsne = TSNE(n_components=2, random_state=42)
    X_embedded = tsne.fit_transform(X)
    
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=y, cmap='tab10', alpha=0.6)
    plt.colorbar(scatter, label='Syndrome ID')
    plt.title('Visualização dos Embeddings com t-SNE')
    plt.xlabel('Componente 1')
    plt.ylabel('Componente 2')
    plt.show()

if __name__ == "__main__":
    file_path = "mini_gm_public_v0.1.p" 
    X, y = load_data(file_path)
    plot_tsne(X, y)
