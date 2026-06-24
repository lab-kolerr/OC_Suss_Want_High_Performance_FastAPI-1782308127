from pydantic import BaseModel
import bcrypt

class User(BaseModel):
    username: str
    password: str

    def hash_password(self):
        self.password = bcrypt.hash(self.password)

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))