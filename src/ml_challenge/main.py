"""
Script principal do ML Challenge.
"""

import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from ml_challenge.utils.data_processing import load_data
from ml_challenge.utils.visualization import plot_tsne
from ml_challenge.models.classification import evaluate_knn
from ml_challenge.models.evaluation import plot_roc_curve

if __name__ == "__main__":
    file_path = "mini_gm_public_v0.1.p"
    
    print("Carregando os dados...")
    X, y = load_data(file_path)
    print(f"Dados carregados: {X.shape[0]} amostras, {X.shape[1]} features")
    
    print("Gerando visualização t-SNE...")
    plot_tsne(X, y)
    
    print("Avaliando KNN...")
    results = evaluate_knn(X, y)
    
    best_k = max(results, key=lambda x: x['accuracy_euclidean'])['k']
    print(f"Melhor K encontrado: {best_k}")
    
    print("Gerando Curva ROC...")
    plot_roc_curve(X, y, best_k)
    
    print("Processo concluído!")
