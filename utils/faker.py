"""
Faker initialization.
"""
from random import shuffle
from uuid import uuid4

from faker import Faker
from faker.providers import BaseProvider


class CustomProvider(BaseProvider):
    """Custom provider with custom fake data generation methods"""

    def hr_id(self):
        """Generate HR ID"""
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        letters = self.random_letters(16)
        symbols = self.random_sample(digits, 5)
        symbols.extend(self.random_sample(letters, 5))
        shuffle(symbols)
        return "".join(symbols)

    @staticmethod
    def uuid():
        """Generate random UUID"""
        return str(uuid4())


fake = Faker()
fake.add_provider(CustomProvider)
