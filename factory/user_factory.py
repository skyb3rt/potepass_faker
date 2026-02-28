from model import users
import faker
from datetime import timedelta, date, datetime
today = date.today()


class UserFactory:
    def __init__(self):
        self.faker = faker.Faker()

    def create_user(self, id: int) -> users.User:
        created = self.faker.date_between(start_date=date(2026, 1, 1), end_date=today)
        updated = created + timedelta(days=self.faker.random_int(min=0, max=5))
        return users.User(
            id=id,
            userName=self.faker.name(),
            password=self.faker.password(),
            email=self.faker.email(),
            description=self.description(),
            dogs=self.create_dogs(),
            created=str(created),
            updated=str(updated),
        )
    
    def description(self) -> str:
        text_list=["i helger", "i helger og ferier","på søndager", "i helger", "i ukedager", "på kveldstid", "på dagtid"]
        return "Trenger hundepass " + self.faker.random_element(elements=text_list)
    
    def allergies(self) -> list[str]:
        allergies_list=["ost", "kylling", "parfyme", "skinke","pollen","støv" ]
        return self.faker.random_elements(elements=allergies_list, length=self.faker.random_int(min=0, max=5), unique=True)
    
    def breed(self) -> str:
        breed_list=["labrador", "golden retriever", "beagle", "bulldog", "poodle", "rottweiler", "yorkshire terrier", "boxer", "dachshund", "siberian husky"]
        return self.faker.random_element(elements=breed_list)
    
    def dog_name(self) -> str:
        dog_name_list=["Bella", "Charlie", "Max", "Luna", "Rocky", "Lucy", "Cooper", "Daisy", "Milo", "Sadie"]
        return self.faker.random_element(elements=dog_name_list)

    def create_dogs(self) -> list[users.Dog]:
        dogs = []
        for i in range(self.faker.random_int(min=1, max=3)):
            dogs.append(users.Dog(
                id=i+1,
                name=self.dog_name(),
                breed=self.breed(),
                age=self.faker.random_int(min=1, max=15),
                allergies=self.allergies()
            ))
        return dogs
    