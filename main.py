from model import petsitters, users, bookings
from factory.user_factory import userFactory
from factory.petsitter_factory import petSitterFactory
from factory.booking_factory import bookingFactory
from utils.utils import read_json_file, write_json_file
from datetime import date 
import faker

def main():
    antall_users=10
    petSitters_antall=5
    bookings_antall=20

    bookings_list =bookings.Model(bookings=[booking for booking in read_json_file('data/bookings.json')])
    petSitters_list = petsitters.Model(petSitters=[petSitter for petSitter in read_json_file('data/petSitters.json')])
    users_list = users.Model(users=[user for user in read_json_file('data/users.json')])

    petSitter_start_id=max([petSitter.id for petSitter in petSitters_list.petSitters])+1
    users_start_id=max([user.id for user in users_list.users])+1
    booking_start_id=max([booking.id for booking in bookings_list.bookings])+1


    PetSitters = petsitters.Model(petSitters=petSitters_list.petSitters+[petSitterFactory().create_pet_sitter(i) for i in range(petSitter_start_id, petSitter_start_id+petSitters_antall)])
    Users = users.Model(users=users_list.users+[userFactory().create_user(i) for i in range(users_start_id, users_start_id+antall_users)])
    Bookings = bookings.Model(bookings=bookings_list.bookings)
    #print(potepass_api.model_dump_json(indent=4))

    if antall_users:
        write_json_file('output/users.json', Users.model_dump()["users"])
    if petSitters_antall:
        write_json_file('output/petSitters.json', PetSitters.model_dump()["petSitters"])
    if bookings_antall:
        antall_users=len(Users.users)
        antall_petSitters=len(PetSitters.petSitters)
        new_bookings = []
        for i in range(booking_start_id, booking_start_id+bookings_antall,1):
            user=Users.users[faker.Faker().random_int(min=0, max=antall_users-1)]
            petSitter=PetSitters.petSitters[faker.Faker().random_int(min=0, max=antall_petSitters-1)]
            new_bookings.append(bookingFactory().create_booking(i, user=user, petSitter=petSitter))
        Bookings = bookings.Model(bookings=bookings_list.bookings+new_bookings)
        write_json_file('output/bookings.json', Bookings.model_dump()["bookings"])
    write_json_file('output/potepass_api.json', {"users":Users.model_dump()["users"], "petSitters":PetSitters.model_dump()["petSitters"], "bookings":Bookings.model_dump()["bookings"]})

if __name__ == "__main__":

    main()