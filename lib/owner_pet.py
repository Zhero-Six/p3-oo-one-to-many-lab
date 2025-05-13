class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of all pets associated with this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to the owner after validating it is a Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a sorted list of the owner's pets by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise Exception("Pet type must be one of: " + ", ".join(self.PET_TYPES))
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)