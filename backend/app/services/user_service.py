from app.auth.hashing import Hash
from app.models.user import User
from app.services.database_service import DatabaseService


class UserService:

    @staticmethod
    def register(full_name, email, password, role="Operator"):

        existing = DatabaseService.get_user_by_email(email)

        if existing:
            return None

        user = User(
            full_name=full_name,
            email=email,
            password=Hash.hash(password),
            role=role,
        )

        return DatabaseService.save_user(user)

    @staticmethod
    def login(email, password):

        user = DatabaseService.get_user_by_email(email)

        if not user:
            return None

        if not Hash.verify(user.password, password):
            return None

        return user