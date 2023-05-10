from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Material:
    def __init__(self, title: str, creator: str, identifier: int):
        self.title = title
        self.creator = creator
        self.identifier = identifier
        self.checked_out_by = None
        self.due_date = None

    def checkout(self, user_id: str) -> None:
        if self.checked_out_by:
            print(f"{self.title} is already checked out.")
        else:
            self.checked_out_by = user_id
            self.due_date = datetime.now() + timedelta(days=7)
            print(f"{self.title} has been checked out by {self.checked_out_by}.")

    def return_material(self) -> None:
        if self.checked_out_by is None:
            print(f"{self.title} is not checked out.")
        else:
            self.checked_out_by = None
            self.due_date = None
            print(f"{self.title} has been returned.")

    def __str__(self):
        return f"{self.__class__.__name__}: {self.title} ({self.creator}), ID: {self.identifier}"


class Book(Material):
    def __init__(self, title: str, creator: str, identifier: int, num_pages: int):
        super().__init__(title, creator, identifier)
        self.num_pages = num_pages

    def __str__(self):
        return super().__str__() + f", {self.num_pages} pages"


class Magazine(Material):
    def __init__(self, title: str, creator: str, identifier: int, publication_date: str):
        super().__init__(title, creator, identifier)
        self.publication_date = publication_date

    def __str__(self):
        return super().__str__() + f", published on {self.publication_date}"


class DVD(Material):
    def __init__(self, title: str, creator: str, identifier: int, video_length: int):
        super().__init__(title, creator, identifier)
        self.video_length = video_length
        self.late_fee = 0

    def checkout(self, user_id: str) -> None:
        super().checkout(user_id)
        self.due_date = datetime.now() + timedelta(days=2)

    def return_material(self) -> None:
        if datetime.now() > self.due_date:
            self.late_fee = (datetime.now() - self.due_date).days
        super().return_material()

    def __str__(self):
        return super().__str__() + f", {self.video_length} minutes, Late fee: {self.late_fee}"


class User(ABC):
    @abstractmethod
    def check_material(self, material: Material) -> None:
        if material.checked_out_by is None:
            material.checkout(self.user_id)
        else:
            print(f"{material.title} is already checked out.")

    @abstractmethod
    def return_material(self, material: Material) -> None:
        if material.checked_out_by == self.user_id:
            material.return_material()
        else:
            print(f"You didn't check out {material.title}.")


class Student(User):
    def __init__(self, student_id: str):
        self.user_id = student_id


class Faculty(User):
    def __init__(self, department: str):
        self.user_id = department

    def check_material(self, material: Material) -> None:
        super().check_material(material)
        material.due_date += timedelta(days=7)


class Library:
    def __init__(self):
        self.materials = []
        self.users = []

    def add_material(self, material: Material) -> None:
        self.materials.append(material)

    def remove_material(self, material: Material) -> None:
        if material in self.materials:
            self.materials.remove(material)

    def search_by_title(self, title: str) -> list:
        return [material for material in self.materials if material.title == title]

    def search_by_identifier(self, identifier: int) -> list:
        return [material for material in self.materials if material.identifier == identifier]

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def remove_user(self, user: User) -> None:
        if user in self.users:
            self.users.remove(user)

    def __str__(self):
        material_str = "Materials:\n"
        for material in self.materials:
            material_str += str(material) + "\n"

        user_str = "Users:\n"
        for user in self.users:
            user_str += str(user) + "\n"

        return material_str + user_str
