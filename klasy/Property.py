class Property:
    def __init__(self, area: str, rooms: int,
                 price: str, address: str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f'Area: {self.area}, rooms: {str(self.rooms)}, '\
            + f'price: {str(self.price)}, address: {self.address}'
