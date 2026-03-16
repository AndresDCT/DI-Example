from interfaces import EmailService, UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository, email_service: EmailService):
        # Dependency Injection via constructor
        self.user_repository = user_repository
        self.email_service = email_service

    def authenticate_and_notify(self, user_id: int):
        user = self.user_repository.get_user(user_id)
        
        if user:
            self.email_service.send_email(user['email'], "Authentication Success", f"Hello {user['name']}, you have been authenticated successfully!")
            return True
        return False
