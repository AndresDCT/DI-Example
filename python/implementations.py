# Concrete class implementing UserRepository
from interfaces import EmailService, UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {1: {"name": "Alice", "email": "alice@example.com"},
                      2: {"name": "Bob", "email": "bob@example.com"}}

    def get_user(self, user_id: int):
        return self.users.get(user_id, None)


# Concrete class implementing EmailService
class SMTPEmailService(EmailService):
    def send_email(self, email: str, subject: str, body: str):
        print(f"Sending email to {email}\nSubject: {subject}\nBody: {body}")
