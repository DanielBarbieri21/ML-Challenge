import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc, f1_score, top_k_accuracy_score
from classification import evaluate_knn
from data_processing import load_data

def plot_roc_curve(X, y, k):
    """Gera e plota a curva ROC para KNN com distâncias Euclidiana e Cosseno."""
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import label_binarize
    
    # Binarizar labels para cálculo da AUC multi-classe
    y_bin = label_binarize(y, classes=np.unique(y))
    X_train, X_test, y_train, y_test = train_test_split(X, y_bin, test_size=0.2, random_state=42)
    
    knn_euclidean = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    knn_cosine = KNeighborsClassifier(n_neighbors=k, metric='cosine')
    
    knn_euclidean.fit(X_train, y_train)
    knn_cosine.fit(X_train, y_train)
    
    y_score_euclidean = knn_euclidean.predict_proba(X_test)
    y_score_cosine = knn_cosine.predict_proba(X_test)
    
    fpr_e, tpr_e, _ = roc_curve(y_test.ravel(), y_score_euclidean.ravel())
    fpr_c, tpr_c, _ = roc_curve(y_test.ravel(), y_score_cosine.ravel())
    
    plt.figure(figsize=(8, 6))
    plt.plot(fpr_e, tpr_e, label=f'Euclidean AUC = {auc(fpr_e, tpr_e):.2f}', color='blue')
    plt.plot(fpr_c, tpr_c, label=f'Cosine AUC = {auc(fpr_c, tpr_c):.2f}', color='red')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'Curva ROC para K={k}')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    file_path = "mini_gm_public_v0.1.p" 
    X, y = load_data(file_path)
    results = evaluate_knn(X, y)
    
    # Escolher o melhor K com base na acurácia
    best_k = max(results, key=lambda x: x['accuracy_euclidean'])['k']
    print(f'Melhor K encontrado: {best_k}')
    
    plot_roc_curve(X, y, best_k)
