class AppException(Exception):
    pass


class UserNotFoundException(AppException):
    def __init__(self, user_id: int):
        self.message = f"User with ID {user_id} not found"
        super().__init__(self.message)
