from klasy.Property import Property


class Flat(Property):
    def __init__(self, area: str, rooms: int, price: str,
                 address: str, floor: int) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return super().__str__() + ', floor: ' + str(self.floor)
