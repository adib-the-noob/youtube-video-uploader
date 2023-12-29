from passlib.context import CryptContext
from db import db_dependency
from authentication.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(
    db: db_dependency, phone_number: str = None, password: str = None
) -> User:
    user_obj = db.query(User).filter(User.phone_number == phone_number).first()

    if user_obj is None:
        return False

    if not verify_password(password, user_obj.password):
        return False
    return user_obj
