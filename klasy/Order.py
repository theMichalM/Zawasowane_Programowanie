import klasy.Employee as Employee
import klasy.Student as Student


class Order:
    def __init__(self, employee: Employee, student: Student,
                 books: list, order_date: str) -> None:
        self.employee: Employee = employee
        self.student: Student = student
        self.books: list = books
        self.order_date = order_date

    def __str__(self) -> str:
        bookstr: str = ''
        for b in self.books:
            bookstr += str(b)+'\n'
        return f'Zamówienie: \nEmployee: \n{str(self.employee)}\nStudent: '\
            + f'\n{str(self.student)}\nBooks: \n{bookstr}'\
            + f'Order date: {self.order_date}\n'
