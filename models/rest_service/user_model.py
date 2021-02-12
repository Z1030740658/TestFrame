from utils.faker import fake
from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, name=None, job=None, id_=None, createdAt=None, gender='female'):
        if id_ is not None:
            self.id = id_
        if createdAt is not None:
            self.createdAt = createdAt  # creating datetime? convert to iso format always!
            # example: fake.past_datetime(start_date='-30d').replace(microsecond=0).isoformat()
        self.name = name or self.generate_name(gender)
        self.job = job or fake.job()

    @staticmethod
    def generate_name(gender):
        if gender == 'female':
            full_name = f"{fake.first_name_female()} {fake.last_name_female()}"
        else:
            full_name = f"{fake.first_name_male()} {fake.last_name_male()}"
        return full_name
