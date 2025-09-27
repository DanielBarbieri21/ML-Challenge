"""
Sistema de logging profissional para o ML Challenge.
"""

import os
from pathlib import Path
from typing import Optional
from loguru import logger
import yaml


def setup_logger(
    config_path: Optional[str] = None,
    log_level: str = "INFO",
    log_file: Optional[str] = None
) -> None:
    """
    Configura o sistema de logging do projeto.
    
    Args:
        config_path: Caminho para o arquivo de configuração YAML
        log_level: Nível de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Caminho para o arquivo de log
    """
    # Remove handlers padrão do loguru
    logger.remove()
    
    # Configuração padrão
    log_format = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}"
    
    # Carrega configurações do arquivo YAML se fornecido
    if config_path and os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            
            log_config = config.get('logging', {})
            log_level = log_config.get('level', log_level)
            log_format = log_config.get('format', log_format)
            log_file = log_config.get('file', log_file)
            
        except Exception as e:
            logger.warning(f"Erro ao carregar configuração de log: {e}")
    
    # Cria diretório de logs se necessário
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Adiciona handler para console
    logger.add(
        sink=lambda msg: print(msg, end=""),
        level=log_level,
        format=log_format,
        colorize=True
    )
    
    # Adiciona handler para arquivo se especificado
    if log_file:
        logger.add(
            sink=log_file,
            level=log_level,
            format=log_format,
            rotation="10 MB",
            retention="30 days",
            compression="zip"
        )
    
    logger.info("Sistema de logging configurado com sucesso")


def get_logger(name: str = None):
    """
    Retorna uma instância do logger configurado.
    
    Args:
        name: Nome do logger (opcional)
        
    Returns:
        Instância do logger
    """
    if name:
        return logger.bind(name=name)
    return logger
