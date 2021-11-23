class Link:
    def __init__(self, movieId, imdbId, tmdbId) -> None:
        self._movieId = movieId
        self._imdbId = imdbId
        self._tmdbId = tmdbId

    def __str__(self) -> str:
        return f'działa'