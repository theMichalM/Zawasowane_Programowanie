from klasy.Property import Property


class House(Property):
    def __init__(self, area: str, rooms: int, price: str,
                 address: str, plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return super().__str__() + ', plot: ' + str(self.plot)
