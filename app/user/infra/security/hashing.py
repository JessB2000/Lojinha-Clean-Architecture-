from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashUser:
    @staticmethod
    def bcrypt(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify(password_hashed: str, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, password_hashed)
