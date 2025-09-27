#!/usr/bin/env python3
"""
Script para configurar o ambiente de desenvolvimento no Windows.
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(command: str, description: str) -> bool:
    """Executa um comando e retorna True se bem-sucedido."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Erro: {e}")
        if e.stdout:
            print(f"   Saída: {e.stdout}")
        if e.stderr:
            print(f"   Erro: {e.stderr}")
        return False


def install_package(package: str, description: str) -> bool:
    """Instala um pacote Python."""
    return run_command(f"pip install {package}", description)


def main():
    """Configura o ambiente de desenvolvimento no Windows."""
    print("🚀 Configurando ambiente de desenvolvimento para ML Challenge (Windows)...")
    
    # Verifica se estamos no diretório correto
    if not Path("src/ml_challenge").exists():
        print("❌ Execute este script na raiz do projeto!")
        sys.exit(1)
    
    # Cria diretórios necessários
    directories = [
        "logs",
        "results/plots",
        "results/models",
        "data/raw",
        "data/processed"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"📁 Diretório criado: {directory}")
    
    # Instala dependências básicas primeiro
    basic_packages = [
        ("pip install --upgrade pip", "Atualizando pip"),
        ("pip install wheel setuptools", "Instalando ferramentas básicas"),
    ]
    
    success_count = 0
    for command, description in basic_packages:
        if run_command(command, description):
            success_count += 1
    
    # Instala NumPy primeiro (versão pré-compilada)
    if install_package("numpy==1.24.3", "Instalando NumPy"):
        success_count += 1
    
    # Instala dependências principais
    main_packages = [
        "scikit-learn==1.3.0",
        "matplotlib==3.7.2", 
        "seaborn==0.12.2",
        "pandas==2.0.3",
        "scipy==1.11.1",
        "plotly==5.15.0",
        "pyyaml==6.0.1",
        "loguru==0.7.0"
    ]
    
    for package in main_packages:
        if install_package(package, f"Instalando {package.split('==')[0]}"):
            success_count += 1
    
    # Instala ferramentas de desenvolvimento (opcional)
    dev_packages = [
        "pytest==7.4.0",
        "pytest-cov==4.1.0", 
        "black==23.7.0",
        "flake8==6.0.0"
    ]
    
    print("\n🔧 Instalando ferramentas de desenvolvimento...")
    for package in dev_packages:
        install_package(package, f"Instalando {package.split('==')[0]}")
    
    # Testa instalação básica
    print("\n🧪 Testando instalação...")
    test_commands = [
        ("python -c \"import numpy; print('NumPy:', numpy.__version__)\"", "Testando NumPy"),
        ("python -c \"import sklearn; print('Scikit-learn:', sklearn.__version__)\"", "Testando Scikit-learn"),
        ("python -c \"import matplotlib; print('Matplotlib:', matplotlib.__version__)\"", "Testando Matplotlib"),
    ]
    
    for command, description in test_commands:
        if run_command(command, description):
            success_count += 1
    
    # Resumo
    print(f"\n📊 Resumo: {success_count}/{len(basic_packages) + len(main_packages) + len(test_commands)} tarefas concluídas")
    
    if success_count >= len(basic_packages) + len(main_packages):
        print("🎉 Ambiente configurado com sucesso!")
        print("\n📝 Próximos passos:")
        print("   1. Teste o projeto: python -m src.ml_challenge.main")
        print("   2. Ou use Docker: docker-compose up ml-challenge")
        print("\n💡 Dicas:")
        print("   - Se houver problemas, use: pip install --only-binary=all numpy scipy")
        print("   - Para desenvolvimento: pip install -r requirements.txt")
    else:
        print("⚠️  Algumas tarefas falharam. Tente:")
        print("   1. pip install --only-binary=all numpy scipy")
        print("   2. pip install -r requirements.txt")
        print("   3. Ou use Docker: docker-compose up ml-challenge")


if __name__ == "__main__":
    main()
