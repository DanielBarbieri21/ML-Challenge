# ML Challenge - Genetic Syndrome Classification


Este projeto implementa um pipeline para classificar síndromes genéticas com base em embeddings de imagens.

## Estrutura do Projeto

ML_Challenge/
│── main.py                # Script principal
│── data_processing.py      # Carregamento e pré-processamento dos dados
│── visualization.py        # Visualização com t-SNE
│── classification.py       # Implementação do KNN e métricas
│── evaluation.py           # Avaliação do modelo e geração de gráficos
│── requirements.txt        # Dependências do projeto
│── README.md               # Instruções de uso


Uso

Carregar e visualizar os dados:

python visualization.py

Treinar e avaliar o modelo:

python evaluation.py

Resultados

Utiliza KNN com distâncias Euclidiana e Cosseno.

Aplica cross-validation para encontrar o melhor valor de K.

Gera gráficos de t-SNE e Curva ROC para análise.

Contato

Para dúvidas, envie um e-mail para dibarbieri21@gmail.com

