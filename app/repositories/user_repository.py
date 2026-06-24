from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_create: UserCreate) -> User:
        db_user = User(email=user_create.email, hashed_password=user_create.password)  # Hashing should be done here
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id, User.isDeleted == False).first()

    def delete_user(self, user_id: int):
        user = self.get_user(user_id)
        if user:
            user.isDeleted = True
            self.db.commit()