class Library:
    def __init__(self, city: str, street: str,
                 zip_code: str, open_hours: str, phone) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f'City: {self.city}, Street: {self.street}, Zip code:'\
         + f'{self.zip_code}, Open hours: {self.open_hours},'\
         + f' Phone: {str(self.phone)}'
