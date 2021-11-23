class Rating:
    def __init__(self, userId, movieId, rating, timestamp) -> None:
        self._userId = userId
        self._movieId = movieId
        self._rating = rating
        self._timestamp = timestamp

    def __str__(self) -> str:
        return f'działa'