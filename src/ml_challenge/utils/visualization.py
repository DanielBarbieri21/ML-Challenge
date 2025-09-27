import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.preprocessing import LabelEncoder
from .data_processing import load_data

def plot_tsne(X, y):
    """Reduz a dimensionalidade dos embeddings para 2D usando t-SNE e plota o gráfico."""
    tsne = TSNE(n_components=2, random_state=42)
    X_embedded = tsne.fit_transform(X)

    # Converter syndrome_id para valores numéricos
    label_encoder = LabelEncoder()
    y_numeric = label_encoder.fit_transform(y)

    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=y_numeric, cmap='tab10', alpha=0.6)
    plt.colorbar(scatter, label='Syndrome ID')
    plt.title('Visualização dos Embeddings com t-SNE')
    plt.xlabel('Componente 1')
    plt.ylabel('Componente 2')
    plt.show()

if __name__ == "__main__":
    file_path = "mini_gm_public_v0.1.p"
    X, y = load_data(file_path)
    plot_tsne(X, y)
