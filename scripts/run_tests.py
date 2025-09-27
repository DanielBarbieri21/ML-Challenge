#!/usr/bin/env python3
"""
Script para executar todos os testes do projeto.
"""

import subprocess
import sys
from pathlib import Path


def run_command(command: str, description: str) -> bool:
    """Executa um comando e retorna True se bem-sucedido."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Sucesso!")
        if result.stdout:
            print(f"   Saída: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Erro: {e}")
        if e.stdout:
            print(f"   Saída: {e.stdout}")
        if e.stderr:
            print(f"   Erro: {e.stderr}")
        return False


def main():
    """Executa todos os testes do projeto."""
    print("🧪 Executando suite completa de testes...")
    
    # Verifica se estamos no diretório correto
    if not Path("src/ml_challenge").exists():
        print("❌ Execute este script na raiz do projeto!")
        sys.exit(1)
    
    # Comandos de teste
    test_commands = [
        ("pytest tests/ -v", "Testes unitários"),
        ("pytest tests/ --cov=src/ --cov-report=html --cov-report=xml", "Testes com cobertura"),
        ("flake8 src/ tests/", "Linting com flake8"),
        ("black --check src/ tests/", "Verificação de formatação"),
        ("mypy src/", "Verificação de tipos"),
    ]
    
    success_count = 0
    total_commands = len(test_commands)
    
    for command, description in test_commands:
        if run_command(command, description):
            success_count += 1
        print()  # Linha em branco entre comandos
    
    # Resumo
    print(f"📊 Resumo: {success_count}/{total_commands} testes passaram")
    
    if success_count == total_commands:
        print("🎉 Todos os testes passaram!")
        print("📁 Relatório de cobertura salvo em: htmlcov/index.html")
        sys.exit(0)
    else:
        print("⚠️  Alguns testes falharam. Verifique os erros acima.")
        sys.exit(1)


if __name__ == "__main__":
    main()
