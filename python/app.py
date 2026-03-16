from implementations import InMemoryUserRepository, SMTPEmailService
from service import UserService


def main():
    # Create instances of the concrete implementations
    user_repository = InMemoryUserRepository()
    email_service = SMTPEmailService()
    
    # Inject dependencies into UserService
    user_service = UserService(user_repository, email_service)
    
    # Call the method to authenticate and notify user
    user_service.authenticate_and_notify(1)  # Should succeed for user 1 (Alice)
    user_service.authenticate_and_notify(3)  # Should fail (no user with id 3)

if __name__ == "__main__":
    main()
