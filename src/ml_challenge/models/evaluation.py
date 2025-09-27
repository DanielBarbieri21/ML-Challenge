import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from ..utils.data_processing import load_data


def plot_roc_curve(X, y, k):
    """Gera e plota a curva ROC para KNN com distâncias Euclidiana e Cosseno."""

    # Binarizar labels para cálculo da AUC multi-classe
    classes = np.unique(y)
    y_bin = label_binarize(y, classes=classes)
    X_train, X_test, y_train, y_test = train_test_split(X, y_bin, test_size=0.2, random_state=42)

    knn_euclidean = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    knn_cosine = KNeighborsClassifier(n_neighbors=k, metric='cosine')

    knn_euclidean.fit(X_train, y_train)
    knn_cosine.fit(X_train, y_train)

    # Garantir que `predict_proba()` tenha saída para todas as classes
    classes_train = np.unique(y_train, axis=0)  # Classes presentes no treino
    classes_all = np.unique(y)  # Todas as classes possíveis

    def adjust_proba(model, X_test, classes_train, classes_all):
        """Garante que `predict_proba()` tenha saída para todas as classes possíveis"""
        probas = np.array(model.predict_proba(X_test))  # Converter para NumPy array
        full_probas = np.zeros((X_test.shape[0], len(classes_all)))

        for i, c in enumerate(classes_train):
            class_index = np.where(classes_all == c)[0]  # Encontrar índice da classe em `classes_all`
            if len(class_index) > 0:
                full_probas[:, class_index[0]] = probas[:, i]

        return full_probas

    y_score_euclidean = adjust_proba(knn_euclidean, X_test, classes_train, classes_all)
    y_score_cosine = adjust_proba(knn_cosine, X_test, classes_train, classes_all)

    # Calcular ROC para cada classe e tirar a média
    fpr_e, tpr_e, fpr_c, tpr_c = [], [], [], []
    for i in range(len(classes)):
        fpr_e_i, tpr_e_i, _ = roc_curve(y_test[:, i], y_score_euclidean[:, i])
        fpr_c_i, tpr_c_i, _ = roc_curve(y_test[:, i], y_score_cosine[:, i])
        fpr_e.append(fpr_e_i)
        tpr_e.append(tpr_e_i)
        fpr_c.append(fpr_c_i)
        tpr_c.append(tpr_c_i)

    # Média das curvas
    mean_fpr_e = np.linspace(0, 1, 100)
    mean_tpr_e = np.mean([np.interp(mean_fpr_e, f, t) for f, t in zip(fpr_e, tpr_e)], axis=0)
    mean_fpr_c = np.linspace(0, 1, 100)
    mean_tpr_c = np.mean([np.interp(mean_fpr_c, f, t) for f, t in zip(fpr_c, tpr_c)], axis=0)

    plt.figure(figsize=(8, 6))
    plt.plot(mean_fpr_e, mean_tpr_e, label=f'Euclidean AUC = {auc(mean_fpr_e, mean_tpr_e):.2f}', color='blue')
    plt.plot(mean_fpr_c, mean_tpr_c, label=f'Cosine AUC = {auc(mean_fpr_c, mean_tpr_c):.2f}', color='red')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'Curva ROC Média para K={k}')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    file_path = "mini_gm_public_v0.1.p"
    X, y = load_data(file_path)

    # Escolher um valor de K arbitrário para teste
    best_k = 5
    plot_roc_curve(X, y, best_k)
