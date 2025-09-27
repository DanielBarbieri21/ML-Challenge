"""
Testes unitários para o módulo de processamento de dados.
"""

import pytest
import numpy as np
import tempfile
import pickle
from pathlib import Path
from unittest.mock import patch, mock_open

from src.ml_challenge.utils.data_processing import load_data


class TestDataProcessing:
    """Testes para funções de processamento de dados."""
    
    def test_load_data_success(self):
        """Testa carregamento bem-sucedido de dados."""
        # Dados de teste simulados
        test_data = {
            'syndrome_1': {
                'subject_1': {
                    'image_1': [1, 2, 3, 4, 5],
                    'image_2': [6, 7, 8, 9, 10]
                },
                'subject_2': {
                    'image_1': [11, 12, 13, 14, 15]
                }
            },
            'syndrome_2': {
                'subject_3': {
                    'image_1': [16, 17, 18, 19, 20]
                }
            }
        }
        
        # Cria arquivo temporário
        with tempfile.NamedTemporaryFile(suffix='.p', delete=False) as tmp_file:
            with open(tmp_file.name, 'wb') as f:
                pickle.dump(test_data, f)
            
            # Testa carregamento
            X, y = load_data(tmp_file.name)
            
            # Verifica resultados
            assert X.shape[0] == 4  # 4 amostras
            assert X.shape[1] == 5  # 5 features
            assert len(y) == 4
            assert len(np.unique(y)) == 2  # 2 síndromes
            
            # Limpa arquivo temporário
            Path(tmp_file.name).unlink()
    
    def test_load_data_file_not_found(self):
        """Testa erro quando arquivo não existe."""
        with pytest.raises(FileNotFoundError):
            load_data("arquivo_inexistente.p")
    
    def test_load_data_invalid_format(self):
        """Testa erro com formato inválido."""
        invalid_data = "dados_inválidos"
        
        with tempfile.NamedTemporaryFile(suffix='.p', delete=False) as tmp_file:
            with open(tmp_file.name, 'wb') as f:
                pickle.dump(invalid_data, f)
            
            with pytest.raises(ValueError, match="Arquivo pickle deve conter um dicionário"):
                load_data(tmp_file.name)
            
            Path(tmp_file.name).unlink()
    
    def test_load_data_empty_data(self):
        """Testa erro com dados vazios."""
        empty_data = {}
        
        with tempfile.NamedTemporaryFile(suffix='.p', delete=False) as tmp_file:
            with open(tmp_file.name, 'wb') as f:
                pickle.dump(empty_data, f)
            
            with pytest.raises(ValueError, match="Nenhum dado válido encontrado"):
                load_data(tmp_file.name)
            
            Path(tmp_file.name).unlink()
    
    def test_load_data_malformed_embeddings(self):
        """Testa carregamento com embeddings malformados."""
        malformed_data = {
            'syndrome_1': {
                'subject_1': {
                    'image_1': "não_é_lista",  # Embedding inválido
                    'image_2': [1, 2, 3, 4, 5]  # Embedding válido
                }
            }
        }
        
        with tempfile.NamedTemporaryFile(suffix='.p', delete=False) as tmp_file:
            with open(tmp_file.name, 'wb') as f:
                pickle.dump(malformed_data, f)
            
            # Deve carregar apenas o embedding válido
            X, y = load_data(tmp_file.name)
            
            assert X.shape[0] == 1  # Apenas 1 amostra válida
            assert X.shape[1] == 5
            assert len(y) == 1
            
            Path(tmp_file.name).unlink()


if __name__ == "__main__":
    pytest.main([__file__])
