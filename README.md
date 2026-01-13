# 🧬 ML Challenge - Genetic Syndrome Classification

[![CI/CD Pipeline](https://github.com/username/ml-challenge/actions/workflows/ci.yml/badge.svg)](https://github.com/username/ml-challenge/actions/workflows/ci.yml)
[![Code Coverage](https://codecov.io/gh/username/ml-challenge/branch/main/graph/badge.svg)](https://codecov.io/gh/username/ml-challenge)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Um pipeline completo e profissional para classificação de síndromes genéticas usando embeddings de imagens e algoritmos de machine learning.

## 📋 Índice

- [Características](#-características)
- [Instalação](#-instalação)
- [Uso Rápido](#-uso-rápido)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Documentação](#-documentação)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

## ✨ Características

- 🔬 **Classificação de Síndromes Genéticas**: Algoritmo KNN otimizado com múltiplas métricas
- 📊 **Visualização Avançada**: t-SNE e curvas ROC para análise de dados
- 🧪 **Validação Cruzada**: Otimização automática de hiperparâmetros
- 📈 **Métricas Completas**: Accuracy, F1-Score, AUC e Top-K Accuracy
- 🐳 **Containerização**: Docker e Docker Compose para deploy
- 🔄 **CI/CD**: Pipeline automatizado com GitHub Actions
- 📝 **Logging Profissional**: Sistema de logs estruturado
- 🧪 **Testes Unitários**: Cobertura completa de testes
- ⚙️ **Configuração Flexível**: Arquivos YAML para configuração

## 🚀 Instalação

### Pré-requisitos

- Python 3.8+
- pip ou conda

### Instalação Local

#### Windows (Recomendado)
```bash
# Clone o repositório
git clone https://github.com/username/ml-challenge.git
cd ml-challenge

# Crie um ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instale dependências (método 1 - automático)
python scripts/setup_windows.py

# OU instale manualmente (método 2)
pip install -r requirements-basic.txt

# Teste a instalação
python scripts/test_installation.py
```

#### Linux/Mac
```bash
# Clone o repositório
git clone https://github.com/username/ml-challenge.git
cd ml-challenge

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### Instalação com Docker

```bash
# Build da imagem
docker build -t ml-challenge .

# Executar com Docker Compose
docker-compose up ml-challenge
```

## 🎯 Uso Rápido

### Execução Básica

```bash
# Executar o pipeline completo
python -m src.ml_challenge.main

# Ou usando o script principal
python src/ml_challenge/main.py
```

### Execução com Docker

```bash
# Desenvolvimento
docker-compose --profile dev up ml-challenge-dev

# Testes
docker-compose --profile test up ml-challenge-test
```

### Jupyter Notebook

```bash
# Iniciar Jupyter
jupyter notebook

# Ou com Docker
docker-compose up ml-challenge
# Acesse http://localhost:8888
```

## 📁 Estrutura do Projeto

```
ML-Challenge/
├── 📁 src/
│   └── 📁 ml_challenge/
│       ├── 📁 config/          # Configurações
│       ├── 📁 models/          # Modelos ML
│       ├── 📁 utils/           # Utilitários
│       └── main.py             # Script principal
├── 📁 tests/                   # Testes unitários
├── 📁 docs/                    # Documentação
├── 📁 scripts/                 # Scripts auxiliares
├── 📁 data/                    # Dados
│   ├── 📁 raw/                 # Dados brutos
│   └── 📁 processed/           # Dados processados
├── 📁 results/                 # Resultados
│   ├── 📁 plots/               # Gráficos
│   └── 📁 models/              # Modelos salvos
├── 📁 .github/
│   └── 📁 workflows/           # CI/CD
├── 📄 requirements.txt         # Dependências
├── 📄 config.yaml              # Configuração
├── 📄 Dockerfile               # Container
├── 📄 docker-compose.yml       # Orquestração
└── 📄 README.md                # Este arquivo
```

## 📚 Documentação

### Configuração

O projeto usa arquivos YAML para configuração. Edite `src/ml_challenge/config/config.yaml`:

```yaml
# Configurações do modelo
model:
  algorithm: "knn"
  k_range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  metrics: ["euclidean", "cosine"]
  cv_folds: 10

# Configurações de dados
data:
  input_file: "mini_gm_public_v0.1.p"
  test_size: 0.2
  random_state: 42
```

### Logging

O sistema de logging é configurado automaticamente:

```python
from src.ml_challenge.utils.logger import get_logger

logger = get_logger(__name__)
logger.info("Mensagem de log")
```

### Testes

```bash
# Executar todos os testes
pytest tests/ -v

# Com cobertura
pytest tests/ --cov=src/ --cov-report=html

# Testes específicos
pytest tests/test_data_processing.py -v
```

### Linting e Formatação

```bash
# Formatação com Black
black src/ tests/

# Linting com Flake8
flake8 src/ tests/

# Type checking com MyPy
mypy src/
```

## 🔧 Desenvolvimento

### Setup do Ambiente de Desenvolvimento

```bash
# Instalar dependências de desenvolvimento
pip install -r requirements.txt

# Configurar pre-commit hooks
pre-commit install

# Executar testes
pytest tests/ -v --cov=src/
```

### Estrutura de Commits

Seguimos o padrão [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: adiciona nova funcionalidade
fix: corrige bug
docs: atualiza documentação
test: adiciona testes
refactor: refatora código
```

## 📊 Resultados

O pipeline gera automaticamente:

- 📈 **Gráficos t-SNE**: Visualização da distribuição dos dados
- 📊 **Curvas ROC**: Análise de performance do modelo
- 📋 **Métricas Detalhadas**: Accuracy, F1-Score, AUC
- 📁 **Modelos Salvos**: Para reutilização posterior

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'feat: add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de Código

- Use type hints em todas as funções
- Documente com docstrings seguindo o padrão Google
- Escreva testes para novas funcionalidades
- Mantenha cobertura de testes > 80%


---

🛠️ **Software desenvolvido por Daniel Barbieri**  
Engenheiro de Software | Full Stack Developer  

Código construído com foco em eficiência, organização, escalabilidade e boas práticas de desenvolvimento.

🌐 GitHub: https://github.com/DanielBarbieri21  
💼 LinkedIn: https://www.linkedin.com/in/daniel-barbieri-4990462a/

---


## 🙏 Agradecimentos

- Comunidade Python
- Scikit-learn
- Contribuidores do projeto

---

⭐ **Se este projeto foi útil, considere dar uma estrela!** ⭐

