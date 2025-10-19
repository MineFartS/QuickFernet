
class Token:

    def __init__(self, key:'Key', token:str):
        self.token = token
        self.key = key

    def decrypt(self):
        return self.key.__fernet.decrypt(self.token)

    def __str__(self):
        return self.token

class Key:

    def __init__(self,
        key: str = None
    ):
        from cryptography.fernet import Fernet

        if isinstance(key, str):
            self.key = key
            self.__fernet = Fernet(key)

        elif key is None:
            self.key = Fernet.generate_key()
            self.__fernet = Fernet(self.key)
        
    def encrypt(self, data):
        return Token(
            key = self,
            token = self.__fernet.encrypt(data)
        )