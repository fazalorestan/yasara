import logging
class LoggingService:
    def get_logger(self,name): return logging.getLogger(name)
logging_service=LoggingService()
