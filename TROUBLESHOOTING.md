# 🔧 Guia de Solução de Problemas - ML Challenge

## ❌ Problemas Comuns e Soluções

### 1. **Erro de Compilação do NumPy no Windows**

**Problema:**
```
error: Microsoft Visual C++ 14.0 is required
```

**Solução:**
```bash
# Método 1: Use versões pré-compiladas
pip install --only-binary=all numpy scipy

# Método 2: Use conda
conda install numpy scipy matplotlib scikit-learn

# Método 3: Use Docker (recomendado)
docker-compose up ml-challenge
```

### 2. **Erro de Importação de Módulos**

**Problema:**
```
ModuleNotFoundError: No module named 'src'
```

**Solução:**
```bash
# Adicione o diretório ao PYTHONPATH
set PYTHONPATH=%PYTHONPATH%;%CD%

# Ou execute como módulo
python -m src.ml_challenge.main
```

### 3. **Problemas com Dependências**

**Problema:**
```
ERROR: Could not find a version that satisfies the requirement
```

**Solução:**
```bash
# Atualize pip primeiro
pip install --upgrade pip

# Use requirements-basic.txt
pip install -r requirements-basic.txt

# Ou instale individualmente
pip install numpy matplotlib scikit-learn
```

### 4. **Problemas com Docker**

**Problema:**
```
docker: command not found
```

**Solução:**
1. Instale o Docker Desktop
2. Reinicie o computador
3. Execute: `docker --version`

### 5. **Problemas de Permissão no Windows**

**Problema:**
```
Permission denied
```

**Solução:**
```bash
# Execute como administrador
# Ou use --user
pip install --user -r requirements-basic.txt
```

## 🚀 **Soluções Rápidas**

### **Opção 1: Docker (Mais Fácil)**
```bash
# Clone o projeto
git clone <seu-repo>
cd ml-challenge

# Execute com Docker
docker-compose up ml-challenge
```

### **Opção 2: Conda (Recomendado para Windows)**
```bash
# Instale Anaconda/Miniconda
# Crie ambiente
conda create -n ml-challenge python=3.10
conda activate ml-challenge

# Instale dependências
conda install numpy scipy matplotlib scikit-learn pandas
pip install loguru pyyaml plotly

# Execute
python -m src.ml_challenge.main
```

### **Opção 3: Instalação Mínima**
```bash
# Instale apenas o essencial
pip install numpy matplotlib scikit-learn

# Execute sem dependências extras
python src/ml_challenge/main.py
```

## 🔍 **Verificação de Problemas**

### **Teste Rápido:**
```bash
# Teste se Python está funcionando
python --version

# Teste se pip está funcionando
pip --version

# Teste instalação básica
python -c "import numpy; print('OK')"
```

### **Diagnóstico Completo:**
```bash
# Execute o script de teste
python scripts/test_installation.py

# Verifique logs
type logs\ml_challenge.log
```

## 📞 **Suporte**

Se os problemas persistirem:

1. **Verifique os logs** em `logs/ml_challenge.log`
2. **Execute o diagnóstico**: `python scripts/test_installation.py`
3. **Use Docker**: `docker-compose up ml-challenge`
4. **Contate**: dibarbieri21@gmail.com

## 🎯 **Configuração Ideal**

Para melhor performance:

```bash
# Windows com Anaconda
conda create -n ml-challenge python=3.10
conda activate ml-challenge
conda install numpy scipy matplotlib scikit-learn pandas
pip install loguru pyyaml plotly

# Linux/Mac
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🐳 **Docker (Sempre Funciona)**

Se nada mais funcionar, use Docker:

```bash
# Build e execute
docker-compose up ml-challenge

# Para desenvolvimento
docker-compose --profile dev up ml-challenge-dev

# Para testes
docker-compose --profile test up ml-challenge-test
```

---

**💡 Dica:** Docker é a opção mais confiável para evitar problemas de dependências!
