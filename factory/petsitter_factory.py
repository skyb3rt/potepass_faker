from model import petsitters
import faker
from datetime import timedelta, date, datetime

today = date.today()



class PetSitterFactory:
    def __init__(self):
        self.faker = faker.Faker()

    def create_pet_sitter(self, id: int) -> petsitters.PetSitter:
        created = self.faker.date_between(start_date=date(2026, 1, 1), end_date=today)
        updated = created + timedelta(days=self.faker.random_int(min=0, max=5))
        return petsitters.PetSitter(
            id=id,
            name=self.faker.name(),
            email=self.faker.email(),
            location=self.location(),
            pricePerDay=self.faker.random_int(min=100, max=400),
            rating=self.faker.pyfloat(min_value=1, max_value=5, right_digits=1),
            reviewCount=self.faker.random_int(min=0, max=25),
            maxDogs=self.faker.random_int(min=1, max=5),
            acceptsPuppies=self.faker.boolean(),
            acceptsLargeDogs=self.faker.boolean(),
            yearsOfExperience=self.faker.random_int(min=0, max=20),
            experienceDescription=self.description(),
            available=self.faker.boolean(),
            created=str(created),
            updated=str(updated),
        )
    
    def description(self) -> str:
        text_list=["valper", "store hunder", "små hunder", "alle typer hunder", "hunder med spesielle behov", "hunder som trenger ekstra omsorg", "hunder som trenger ekstra mosjon", "hunder som trenger ekstra sosialisering", "hunder som trenger ekstra trening", "hunder som trenger ekstra oppmerksomhet"]
        return "Erfaring med " + self.faker.random_element(elements=text_list)
    
    def location(self) -> str:
        location_list=["Oslo", "Bergen", "Trondheim", "Stavanger", "Kristiansand", "Tromsø", "Drammen", "Fredrikstad", "Porsgrunn", "Skien"]
        return self.faker.random_element(elements=location_list)
    