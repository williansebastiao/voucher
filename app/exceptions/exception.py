class IntegrityErrorException(Exception):
    def __init__(self, message: str = "Erro de integridade."):
        super().__init__(message)
        self.message = message


class NotFoundException(Exception):
    def __init__(self, message: str = "Registro não encontrado."):
        super().__init__(message)
        self.message = message
