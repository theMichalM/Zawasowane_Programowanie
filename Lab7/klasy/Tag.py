class Tag:
    def __init__(self, userId, movieId, tag, timestamp) -> None:
        self._userId = userId
        self._movieId = movieId
        self._tag = tag
        self._timestamp = timestamp

    def __str__(self) -> str:
        return f'działa'