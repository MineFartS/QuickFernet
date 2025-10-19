
class Token:

    def __init__(self, key:'Key', token:str):
        self.token = token
        self.key = key

    def decrypt(self):
        return self.key.fernet.decrypt(self.token).decode()

class Key:

    def __init__(self,
        key: str = None
    ):
        from cryptography.fernet import Fernet

        if isinstance(key, str):
            self.key = key
            self.fernet = Fernet(key)

        elif key is None:
            self.key = Fernet.generate_key()
            self.fernet = Fernet(self.key)
        
    def encrypt(self, data:str):
        return Token(
            key = self,
            token = self.fernet.encrypt(data.encode())
        )