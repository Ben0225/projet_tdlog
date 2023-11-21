from weapon.weapon import Weapon


class Lance_missiles_anti_surface(Weapon):
    def __init__(self):
        super().__init__(munitions = 50, range = 100)

    def fire_at(self, x: int, y: int, z: int):
        if z != 0:
            super().fire_at(x, y, z)# On fait appel à cette méthode pour dimunier les ammunitions
            raise OutOfRangeError("la cible n'est pas admissible")
        else:
            print("la cible est atteignable")
