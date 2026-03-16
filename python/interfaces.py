from abc import ABC, abstractmethod

# Define an interface for UserRepository
class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: int):
        pass


# Define an interface for EmailService
class EmailService(ABC):
    @abstractmethod
    def send_email(self, email: str, subject: str, body: str):
        pass
