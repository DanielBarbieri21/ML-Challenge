"""
Módulo para processamento e carregamento de dados.
"""

import pickle
from pathlib import Path
from typing import Tuple, Dict, Any, List
import numpy as np
from loguru import logger


def load_data(file_path: str) -> Tuple[np.ndarray, np.ndarray]:
    """
    Carrega os dados do arquivo pickle e os transforma em um formato adequado.
    
    Args:
        file_path: Caminho para o arquivo pickle contendo os dados
        
    Returns:
        Tuple contendo:
            - X: Array numpy com os embeddings (n_samples, n_features)
            - y: Array numpy com os labels das síndromes (n_samples,)
            
    Raises:
        FileNotFoundError: Se o arquivo não for encontrado
        ValueError: Se o arquivo não contém dados válidos
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    
    try:
        logger.info(f"Carregando dados de: {file_path}")
        
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
        
        if not isinstance(data, dict):
            raise ValueError("Arquivo pickle deve conter um dicionário")
        
        X, y = [], []
        total_samples = 0
        
        for syndrome_id, subjects in data.items():
            if not isinstance(subjects, dict):
                logger.warning(f"Formato inválido para síndrome {syndrome_id}")
                continue
                
            for subject_id, images in subjects.items():
                if not isinstance(images, dict):
                    logger.warning(f"Formato inválido para sujeito {subject_id}")
                    continue
                    
                for image_id, embedding in images.items():
                    if isinstance(embedding, (list, np.ndarray)):
                        X.append(embedding)
                        y.append(syndrome_id)
                        total_samples += 1
                    else:
                        logger.warning(f"Embedding inválido para imagem {image_id}")
        
        if total_samples == 0:
            raise ValueError("Nenhum dado válido encontrado no arquivo")
        
        X_array = np.array(X)
        y_array = np.array(y)
        
        logger.info(f"Dados carregados com sucesso: {X_array.shape[0]} amostras, {X_array.shape[1]} features")
        logger.info(f"Número de classes únicas: {len(np.unique(y_array))}")
        
        return X_array, y_array
        
    except Exception as e:
        logger.error(f"Erro ao carregar dados: {e}")
        raise

if __name__ == "__main__":
    file_path = "mini_gm_public_v0.1.p" 
    X, y = load_data(file_path)
    print(f"Dados carregados: {X.shape[0]} amostras, {X.shape[1]} features")