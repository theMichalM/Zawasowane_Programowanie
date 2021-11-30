class Movie:
    def __init__(self, movieId, title, genere) -> None:
        self._movieId = movieId
        self._title = title
        self._genere = genere

    def __str__(self) -> str:
        return f'działa'