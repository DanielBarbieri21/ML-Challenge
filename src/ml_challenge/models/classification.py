import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score, roc_auc_score, top_k_accuracy_score
from ..utils.data_processing import load_data

def evaluate_knn(X, y, k_range=range(1, 16)):
    """Avalia o KNN usando cross-validation e diferentes métricas."""
    results = []
    for k in k_range:
        knn_euclidean = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
        knn_cosine = KNeighborsClassifier(n_neighbors=k, metric='cosine')
        
        scores_euclidean = cross_val_score(knn_euclidean, X, y, cv=10, scoring='accuracy')
        scores_cosine = cross_val_score(knn_cosine, X, y, cv=10, scoring='accuracy')
        
        results.append({
            'k': k,
            'accuracy_euclidean': np.mean(scores_euclidean),
            'accuracy_cosine': np.mean(scores_cosine)
        })
    
    return results

if __name__ == "__main__":
    file_path = "mini_gm_public_v0.1.p"  
    X, y = load_data(file_path)
    results = evaluate_knn(X, y)
    for res in results:
        print(f"k={res['k']}: Euclidean={res['accuracy_euclidean']:.4f}, Cosine={res['accuracy_cosine']:.4f}")
