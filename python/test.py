import unittest
from unittest.mock import MagicMock

from interfaces import EmailService, UserRepository
from service import UserService

# Assuming previous code (UserService, UserRepository, EmailService) is already defined

class TestUserService(unittest.TestCase):

    def test_authenticate_and_notify_user_found(self):
        # Create mock objects for dependencies
        mock_user_repo = MagicMock(spec=UserRepository)
        mock_email_service = MagicMock(spec=EmailService)

        # Set up the mock behavior: return a mock user when get_user is called
        mock_user_repo.get_user.return_value = {"name": "Alice", "email": "alice@example.com"}

        # Instantiate UserService with mocked dependencies
        user_service = UserService(mock_user_repo, mock_email_service)

        # Call the method under test
        result = user_service.authenticate_and_notify(1)

        # Assertions to verify behavior
        self.assertTrue(result)  # The result should be True because the user exists
        mock_email_service.send_email.assert_called_once_with("alice@example.com", "Authentication Success", "Hello Alice, you have been authenticated successfully!")

    def test_authenticate_and_notify_user_not_found(self):
        # Create mock objects for dependencies
        mock_user_repo = MagicMock(spec=UserRepository)
        mock_email_service = MagicMock(spec=EmailService)

        # Set up the mock behavior: return None when get_user is called (user not found)
        mock_user_repo.get_user.return_value = None

        # Instantiate UserService with mocked dependencies
        user_service = UserService(mock_user_repo, mock_email_service)

        # Call the method under test
        result = user_service.authenticate_and_notify(3)  # User with ID 3 does not exist

        # Assertions to verify behavior
        self.assertFalse(result)  # The result should be False because the user does not exist
        mock_email_service.send_email.assert_not_called()  # No email should be sent

if __name__ == "__main__":
    unittest.main()