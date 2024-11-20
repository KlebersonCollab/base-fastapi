import logging
import os

# Configurações básicas de logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()  # Define o nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_FILE = "app.log"  # Nome do arquivo de log

# Configuração do logger
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),  # Define o nível de log
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato da mensagem de log
    filename=LOG_FILE,  # Nome do arquivo de log
    filemode="a"  # Modo de escrita (append), adicionando logs ao arquivo existente
)

# Crie um logger para uso em diferentes partes do projeto
app_logger = logging.getLogger(__name__)

#Exemplo de uso do logger
'''
app_logger.info("Informational message")
app_logger.warning("Warning message")
app_logger.error("Error message")
para inclur o Traceback Completo:
app_logger.error("Error message", exc_info=True)

'''