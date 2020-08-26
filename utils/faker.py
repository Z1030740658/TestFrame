"""
Faker initialization.
"""
from random import shuffle
from faker import Faker
from faker.providers import BaseProvider


class CustomProvider(BaseProvider):
    """Custom provider with custom fake data generation methods"""

    def id(self):
        """Generate ID"""
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        letters = self.random_letters(20)
        symbols = self.random_sample(digits, 15)
        symbols.extend(self.random_sample(letters, 10))
        shuffle(symbols)
        return "".join(symbols)


fake = Faker()
fake.add_provider(CustomProvider)
