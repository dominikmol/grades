import json


class Student:
    def __init__(self, name="Jan", lastname="Kowalski"):
        self.student = {
            'name': name,
            'lastname': lastname,
            'subjects': {
                'polski': [],
                'matematyka': [],
                'angielski': [],
                'informatyka': [],
                'chemia': []
            }
        }

    def show_grades(self):
        print("---------------------------")
        print(f"oceny {self.student['name']} {self.student['lastname']}:")
        for subject in self.student['subjects']:
            grades = self.student['subjects'][subject]
            print(f"{subject}: {grades}")

    def add_grades(self):
        while True:
            print("---------------------------")
            for subject in self.student['subjects']:
                print(subject)

            sub = input("do ktrego przedmiotu doda ocene? ")
            if sub in self.student['subjects'].keys():
                grade = int(input("podaj ocene: "))
                self.student['subjects'][sub].append(grade)
            elif sub == "":
                break
            else:
                print("nie mozna dodac nie ma takiego przedmiotu")

    def edit_grades(self):
        while True:
            print("---------------------------")
            for subject in self.student['subjects']:
                print(subject)

            sub = input("do ktrego przedmiotu poprawic ocene? ")
            if sub in self.student['subjects'].keys():
                grades = self.student['subjects'][sub]

                for i in range(len(grades)):
                    print(f"[{i}: {grades[i]}]")
                index = int(
                    input("podaj podaj numer w [] ktora ocene chcesz zedytowac? "))
                grade = int(input("podaj ocene: "))
                self.student['subjects'][sub][index] = grade
            elif sub == "":
                break
            else:
                print("nie mozna dodac nie ma takiego przedmiotu")

    def delete_grades(self):
        while True:
            print("---------------------------")
            for subject in self.student['subjects']:
                print(subject)

            sub = input("z ktrego przedmiotu usunac ocene? ")
            if sub in self.student['subjects'].keys():
                grades = self.student['subjects'][sub]

                for i in range(len(grades)):
                    print(f"[{i}: {grades[i]}]")
                index = int(
                    input("podaj podaj numer w [] ktora ocene chcesz usunac? "))
                self.student['subjects'][sub].pop(index)
            elif sub == "":
                break
            else:
                print("nie mozna dodac nie ma takiego przedmiotu")

    def add_subject(self, subject_name):
        print("---------------------------")
        if subject_name in self.student['subjects'].keys():
            print("już jest taki przedmiot")
        else:
            self.student['subjects'][subject_name] = []

    def delete_subject(self, subject_name):
        print("---------------------------")
        if subject_name in self.student['subjects'].keys():
            self.student['subjects'].pop(subject_name)
        else:
            print("nie ma takiego przedmiotu")

    def save(self):
        with open(f"{self.student['name']}_{self.student['lastname']}.json", "w") as file:
            json.dump(self.student, file)
        print(
            f"zapisano do pliku ./{self.student['name']}_{self.student['lastname']}.json")

    def load(self, file_name):
        with open(file_name) as file:
            self.student = json.load(file)

    def change_name(self, name):
        self.student['name'] = name

    def change_lastname(self, lastname):
        self.student['lastname'] = lastname


while True:
    print("---------------------------")
    print("""Czy chcesz dodac nowego studenta czy wczytac stuydenta z pliku? (podaj numer)
          1. nowy
          2. wczytaj
          3. zakończ
    """)
    action = int(input())
    student = Student()

    if action == 1:
        name = input("podaj imie studenta: ")
        lastname = input("podaj nazwisko studenta: ")
        student.change_name(name)
        student.change_lastname(lastname)
    elif action == 2:
        file_name = input("podaj nazwe pliku wraz z .json: ")
        student.load(file_name)
    elif action == 3:
        break

    while True:
        print("---------------------------")
        print("""wybierz numer operacji:
              1. wyswietl oceny
              2 dodaj ocene
              3. edytuj ocene
              4. usun ocene
              5. dodaj przedmiot
              6. usun przedmiot
              7. zapisz oceny do piku
              8. wczytaj oceny z pliku
              9. zmien imie studenta
              10. zmien nazwisko studenta
              11. powrtót do poprzedniego wyboru 
              """)
        action = int(input())

        if action == 1:
            student.show_grades()
        elif action == 2:
            student.add_grades()
        elif action == 3:
            student.edit_grades()
        elif action == 4:
            student.delete_grades()
        elif action == 5:
            subject_name = input("Podaj nazwe przedmiotu który chcesz dodać: ")
            student.add_subject(subject_name)
        elif action == 6:
            subject_name = input(
                "Podaj nazwe przedmiotu który chcesz usunąć: ")
            student.delete_subject(subject_name)
        elif action == 7:
            student.save()
        elif action == 8:
            file_name = input("podaj nazwe pliku wraz z .json: ")
            student.load(file_name)
        elif action == 9:
            name = input("podaj nowe imie studenta: ")
            student.change_name(name)
        elif action == 10:
            lastname = input("podaj nowe nazwisko studenta: ")
            student.change_lastname(lastname)
        elif action == 11:
            break
