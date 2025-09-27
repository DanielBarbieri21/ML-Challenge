#!/usr/bin/env python3
"""
Script para testar se a instalação está funcionando corretamente.
"""

import sys
import importlib
from pathlib import Path


def test_import(module_name: str, package_name: str = None) -> bool:
    """Testa se um módulo pode ser importado."""
    try:
        if package_name:
            module = importlib.import_module(module_name)
            version = getattr(module, '__version__', 'Unknown')
            print(f"✅ {package_name}: {version}")
        else:
            importlib.import_module(module_name)
            print(f"✅ {module_name}: OK")
        return True
    except ImportError as e:
        print(f"❌ {module_name}: FALHOU - {e}")
        return False


def main():
    """Testa todas as dependências do projeto."""
    print("🧪 Testando instalação do ML Challenge...")
    print("=" * 50)
    
    # Testa dependências básicas
    print("\n📦 Testando dependências básicas:")
    basic_modules = [
        ("numpy", "NumPy"),
        ("scipy", "SciPy"),
        ("pandas", "Pandas"),
        ("matplotlib", "Matplotlib"),
        ("seaborn", "Seaborn"),
        ("sklearn", "Scikit-learn"),
        ("plotly", "Plotly"),
        ("yaml", "PyYAML"),
        ("loguru", "Loguru"),
    ]
    
    success_count = 0
    for module, name in basic_modules:
        if test_import(module, name):
            success_count += 1
    
    # Testa módulos do projeto
    print("\n🔧 Testando módulos do projeto:")
    project_modules = [
        "src.ml_challenge",
        "src.ml_challenge.utils.data_processing",
        "src.ml_challenge.models.classification",
        "src.ml_challenge.utils.visualization",
    ]
    
    for module in project_modules:
        if test_import(module):
            success_count += 1
    
    # Testa ferramentas de desenvolvimento (opcional)
    print("\n🛠️ Testando ferramentas de desenvolvimento:")
    dev_modules = [
        ("pytest", "Pytest"),
        ("black", "Black"),
        ("flake8", "Flake8"),
    ]
    
    for module, name in dev_modules:
        test_import(module, name)
    
    # Resumo
    print("\n" + "=" * 50)
    print(f"📊 Resumo: {success_count}/{len(basic_modules) + len(project_modules)} módulos funcionando")
    
    if success_count >= len(basic_modules) + len(project_modules):
        print("🎉 Instalação funcionando perfeitamente!")
        print("\n🚀 Próximos passos:")
        print("   1. python -m src.ml_challenge.main")
        print("   2. docker-compose up ml-challenge")
    else:
        print("⚠️  Alguns módulos falharam. Tente:")
        print("   1. pip install -r requirements-basic.txt")
        print("   2. python scripts/setup_windows.py")
        print("   3. docker-compose up ml-challenge")


if __name__ == "__main__":
    main()
