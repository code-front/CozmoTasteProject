from abc import ABC, abstractmethod

# Constants of the taste types so a small typo doesn't cause
# Use these and not raw strings
sour = "sour"
salty = "salty"
bitter = "bitter"
umami = "umami"
savory = "umami"
sweet = "sweet"


class FoodProp:
    def __init__(self):
        pass

    # Output: return the name of the food as a string
    @abstractmethod
    def to_string(cls):
        pass

    # Output: return a tuple with strings of the suitable taste types
    # Possible strings: ("sweet", "sour", "salty", "bitter", "umami")
    @abstractmethod
    def tastes(self):
        pass


class Apple(FoodProp):
    def __init__(self):
        pass

    @classmethod
    def to_string(cls):
        return "apple"

    @classmethod
    def tastes(cls):
        return (sweet)

    def __str__(self):
        return self.to_string()


class Orange(FoodProp):
    def __init__(self):
        pass

    @classmethod
    def to_string(cls):
        return "orange"

    @classmethod
    def tastes(cls):
        return (sweet, sour)

    def __str__(self):
        return self.to_string()


def getFood(foodType: str):
    """
    Factory function
    :param foodType: String representing what food to return
    :return: Reference to the suitable static food object
    Exceptions: KeyError if foodType isn't in dictionary
    """
    foodType = foodType.lower()
    return {
        "apple": Apple(),
        "orange": Orange()
    }[foodType]