
#Class Methods

class classmethod:
    species = "whiteDog"

    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

classmethod.change_species("blackDog")
print(classmethod.species)        



