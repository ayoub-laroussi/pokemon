from random import *





class Pokemon:
    def __init__(self, nom):
        self.__nom = nom
        self.__point_de_vie = randint(100, 200)
        self.__point_d_attaque = randint(0, 50)
        self.__point_de_defense = randint(50, 100)
        self.__point_de_vitesse = randint(20, 80)
        self.__ko = False

    def get_nom(self):
        return self.__nom

    def get_point_de_vie(self):
        return self.__point_de_vie

    def get_point_d_attaque(self):
        return self.__point_d_attaque

    def get_point_de_defense(self):
        return self.__point_de_defense

    def get_point_de_vitesse(self):
        return self.__point_de_vitesse

    def set_point_de_vie(self, new_point_de_vie: int):
        self.__point_de_vie = new_point_de_vie

    def set_ko(self):
        if self.__point_de_vie <= 0:
            self.__ko = True

    def affiche_statistiques(self):
        return self.__nom, self.__point_de_vie, self.__point_d_attaque, self.__point_de_defense, self.__point_de_vitesse, self.__ko

    def augmente_attaque(self, bonus: int):
        self.__point_d_attaque = self.__point_d_attaque + 20

    def augmente_point_de_vie(self, bonus: int):
        self.__point_de_vie = self.__point_de_vie + 25

    def augmente_vitesse(self, bonus: int):
        self.__point_de_vitesse = self.__point_de_vitesse + 10

    def attaque(self, pokemon_adverse) -> int:
        if self.get_point_d_attaque() < self.get_point_de_defense():
            degats = 0
        else:
            damage = self.get_point_d_attaque() - self.get_point_de_defense()
            print(degats)




pikachu = Pokemon("Pikachu")