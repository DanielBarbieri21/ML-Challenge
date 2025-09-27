#!/usr/bin/env python3
"""
Script para instalação mínima e funcional do ML Challenge.
Funciona com Python 3.13 e resolve problemas de compatibilidade.
"""

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


def main():
    """Instala dependências mínimas funcionais."""
    print("🚀 Instalação Mínima do ML Challenge (Python 3.13)...")
    print("=" * 60)
    
    # Verifica Python
    python_version = sys.version_info
    print(f"🐍 Python: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major == 3 and python_version.minor >= 13:
        print("⚠️  Python 3.13 detectado - usando versões compatíveis")
    
    # Cria diretórios
    directories = ["logs", "results/plots", "results/models", "data/raw", "data/processed"]
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"📁 Diretório criado: {directory}")
    
    # Atualiza pip
    run_command("pip install --upgrade pip", "Atualizando pip")
    
    # Instala dependências básicas (versões compatíveis com Python 3.13)
    packages = [
        # Core ML (versões mais recentes compatíveis)
        ("pip install numpy", "NumPy (versão mais recente)"),
        ("pip install matplotlib", "Matplotlib (versão mais recente)"),
        ("pip install scikit-learn", "Scikit-learn (versão mais recente)"),
        
        # Dados
        ("pip install pandas", "Pandas (versão mais recente)"),
        ("pip install scipy", "SciPy (versão mais recente)"),
        
        # Visualização
        ("pip install seaborn", "Seaborn"),
        ("pip install plotly", "Plotly"),
        
        # Configuração
        ("pip install pyyaml", "PyYAML"),
        ("pip install loguru", "Loguru"),
    ]
    
    success_count = 0
    for command, description in packages:
        if run_command(command, description):
            success_count += 1
    
    # Testa instalação
    print("\n🧪 Testando instalação...")
    test_commands = [
        ("python -c \"import numpy; print('NumPy:', numpy.__version__)\"", "Testando NumPy"),
        ("python -c \"import matplotlib; print('Matplotlib:', matplotlib.__version__)\"", "Testando Matplotlib"),
        ("python -c \"import sklearn; print('Scikit-learn:', sklearn.__version__)\"", "Testando Scikit-learn"),
        ("python -c \"import pandas; print('Pandas:', pandas.__version__)\"", "Testando Pandas"),
    ]
    
    for command, description in test_commands:
        if run_command(command, description):
            success_count += 1
    
    # Resumo
    print(f"\n📊 Resumo: {success_count}/{len(packages) + len(test_commands)} tarefas concluídas")
    
    if success_count >= len(packages):
        print("🎉 Instalação concluída com sucesso!")
        print("\n🚀 Próximos passos:")
        print("   1. Teste: python scripts/test_installation.py")
        print("   2. Execute: python -m src.ml_challenge.main")
        print("   3. Ou use Docker: docker-compose up ml-challenge")
    else:
        print("⚠️  Algumas dependências falharam.")
        print("💡 Soluções alternativas:")
        print("   1. Use Docker: docker-compose up ml-challenge")
        print("   2. Use Anaconda: conda install numpy matplotlib scikit-learn pandas")
        print("   3. Use Python 3.11: pyenv install 3.11.0")


if __name__ == "__main__":
    main()
