#!/usr/bin/env python3
"""
Script para configurar o ambiente de desenvolvimento.
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
        print(f"   Saída: {e.stdout}")
        print(f"   Erro: {e.stderr}")
        return False


def main():
    """Configura o ambiente de desenvolvimento."""
    print("🚀 Configurando ambiente de desenvolvimento para ML Challenge...")
    
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
    
    # Instala dependências
    commands = [
        ("pip install --upgrade pip", "Atualizando pip"),
        ("pip install -r requirements.txt", "Instalando dependências"),
        ("pip install pre-commit", "Instalando pre-commit"),
        ("pre-commit install", "Configurando pre-commit hooks"),
    ]
    
    success_count = 0
    for command, description in commands:
        if run_command(command, description):
            success_count += 1
    
    # Executa testes
    print("\n🧪 Executando testes...")
    if run_command("pytest tests/ -v", "Executando testes"):
        success_count += 1
    
    # Executa linting
    print("\n🔍 Executando linting...")
    if run_command("flake8 src/ tests/", "Verificando código com flake8"):
        success_count += 1
    
    if run_command("black --check src/ tests/", "Verificando formatação com black"):
        success_count += 1
    
    # Resumo
    print(f"\n📊 Resumo: {success_count}/{len(commands) + 3} tarefas concluídas com sucesso")
    
    if success_count == len(commands) + 3:
        print("🎉 Ambiente configurado com sucesso!")
        print("\n📝 Próximos passos:")
        print("   1. Execute: python -m src.ml_challenge.main")
        print("   2. Ou use Docker: docker-compose up ml-challenge")
        print("   3. Para desenvolvimento: docker-compose --profile dev up ml-challenge-dev")
    else:
        print("⚠️  Algumas tarefas falharam. Verifique os erros acima.")
        sys.exit(1)


if __name__ == "__main__":
    main()
