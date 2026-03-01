from model import bookings, users, petsitters
import faker
from datetime import timedelta, date, datetime

today = date.today()



class BookingFactory:
    def __init__(self):
        self.faker = faker.Faker()

    def create_booking(self, id: int, user: users.User, petSitter: petsitters.PetSitter) -> bookings.Booking:
        fromDate = self.faker.date_between(start_date=date(2026, 2, 20), end_date=date(2026, 2, 21))
        toDate = fromDate + timedelta(days=self.faker.random_int(min=1, max=7))
        created = self.faker.date_between(start_date=date(2026, 1, 1), end_date=today)
        updated = created + timedelta(days=self.faker.random_int(min=0, max=5))
        status=self.faker.random_element(elements=('pending', 'confirmed', 'cancelled', 'completed'))
        payed=False
        if status == 'completed':
             payed=self.faker.boolean(chance_of_getting_true=80)
             
        if updated > today:
            updated = today

        if toDate < today and status == 'completed':
            rating_random=self.faker.pyfloat(min_value=1, max_value=5, right_digits=0)
            rating = self.faker.random_element(elements=[rating_random, None])
        else:
                rating = None

        
        self.dog=user.dogs[faker.Faker().random_int(min=0, max=len(user.dogs)-1)]


        return bookings.Booking(
            id=id,
            userId=user.id,
            userDogId=self.dog.id,
            petSitterId=petSitter.id,
            fromDate=str(fromDate),
            toDate=str(toDate),
            status=status,
            message=self.message(),
            created=str(created),
            updated=str(updated),
            rating=rating,
            payed=payed,
        )
    

    def message(self) -> str:
        text_list=["redd andre hunder","glad", "sosial", "rolig", "leken", "snill", "vant til andre hunder", "vant til barn", "vant til katter", "vant til andre dyr"]
        dog_allergies="Allergisk mot " +', '.join(self.dog.allergies)+"." if self.dog.allergies else "Ingen allergier"
        message=f"Hei! {self.dog.name} er {self.faker.random_element(elements=text_list)}. {dog_allergies}"

        return message

