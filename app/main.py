class Animal:
    flag = False

    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True):

        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        Animal.flag = False

    def print_name(self):
        print(f"Hello, I'm {self.name}")

    def feed(self):
        if Animal.flag or self.appetite == 0:
            self.appetite = 0
            return self.appetite
        else:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry, Animal.flag = False, True
            return self.appetite


class Cat(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 3,
                 is_hungry: bool = True):

        super().__init__(name, is_hungry)
        self.appetite = appetite
        if not self.appetite:
            self.appetite = 0

    @staticmethod
    def catch_mouse():
        print("The hunt began!")


class Dog(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 7,
                 is_hungry: bool = True):

        super().__init__(name, is_hungry)
        self.appetite = appetite
        if not self.appetite:
            self.appetite = 0

    @staticmethod
    def bring_slippers():
        print("The slippers delivered!")



