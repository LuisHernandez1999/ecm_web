class GameException(Exception):
    pass

class GameAlreadyExists(GameException):
    pass

class InvalidPrice(GameException):
    pass

class GenreNotAllowed(GameException):
    pass
