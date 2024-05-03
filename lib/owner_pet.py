class Pet:
    all =[]
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name, type, owner=None):
        self.name = name
        self.pet_type = type #call the setter and getter function
        Pet.all.append(self)
        # if pet_type in Pet.PET_TYPES: //not here, because it only applies first time you initialise, after that it won't apply again. completely mutable with out the rule.
        #     self.pet_type = pet_type 
        # else:
        #     raise Exception
        self.owner = owner

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self,value):
        if not value in Pet.PET_TYPES:
            raise Exception
        self._pet_type = value

class Owner:

    def __init__(self, name):
        self.name = name
        # Owner.add_pet(pet)

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance (pet, Pet):
            pet.owner = self
            # self.pets.append(pet)
        else:
            raise Exception
        
    def get_sorted_pets(self):
        pets = self.pets()
        sorted_pets = sorted(pets,key = lambda pet: pet.name)
        return sorted_pets
