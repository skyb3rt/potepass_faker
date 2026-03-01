from model import petsitters, users, bookings
from factory.user_factory import UserFactory
from factory.petsitter_factory import PetSitterFactory
from factory.booking_factory import BookingFactory
from utils.utils import read_json_file, write_json_file
from datetime import date 
import faker
import sys
import os

def main():
    # Ta inn variabler fra miljøvariabler eller kommandolinje med standardverdier
    antall_users = int(os.getenv('ANTALL_USERS', sys.argv[1] if len(sys.argv) > 1 else 5))
    pet_sitters_antall = int(os.getenv('PETSITTERS_ANTALL', sys.argv[2] if len(sys.argv) > 2 else 5))
    bookings_antall = int(os.getenv('BOOKINGS_ANTALL', sys.argv[3] if len(sys.argv) > 3 else 50))

    bookings_list =bookings.Model(bookings=[booking for booking in read_json_file('data/bookings.json')])
    pet_sitters_list = petsitters.Model(petSitters=[petSitter for petSitter in read_json_file('data/pet_sitters.json')])
    users_list = users.Model(users=[user for user in read_json_file('data/users.json')])

    pet_sitter_start_id=max([petSitter.id for petSitter in pet_sitters_list.petSitters])+1
    users_start_id=max([user.id for user in users_list.users])+1
    booking_start_id=max([booking.id for booking in bookings_list.bookings])+1


    pet_sitters = petsitters.Model(petSitters=pet_sitters_list.petSitters+[PetSitterFactory().create_pet_sitter(i) for i in range(pet_sitter_start_id, pet_sitter_start_id+pet_sitters_antall)])
    users_obj = users.Model(users=users_list.users+[UserFactory().create_user(i) for i in range(users_start_id, users_start_id+antall_users)])
    bookings_obj = bookings.Model(bookings=bookings_list.bookings)
    #print(potepass_api.model_dump_json(indent=4))

    if antall_users:
        write_json_file('output/users.json', users_obj.model_dump()["users"])
    if pet_sitters_antall:
        write_json_file('output/pet_sitters.json', pet_sitters.model_dump()["petSitters"])
    if bookings_antall:
        antall_users=len(users_obj.users)
        antall_pet_sitters=len(pet_sitters.petSitters)
        new_bookings = []
        for i in range(booking_start_id, booking_start_id+bookings_antall,1):
            user=users_obj.users[faker.Faker().random_int(min=0, max=antall_users-1)]
            pet_sitter=pet_sitters.petSitters[faker.Faker().random_int(min=0, max=antall_pet_sitters-1)]
            new_bookings.append(BookingFactory().create_booking(i, user=user, petSitter=pet_sitter))
        bookings_obj = bookings.Model(bookings=bookings_list.bookings+new_bookings)
        write_json_file('output/bookings.json', bookings_obj.model_dump()["bookings"])
    write_json_file('output/potepass.json', {"users":users_obj.model_dump()["users"], "petSitters":pet_sitters.model_dump()["petSitters"], "bookings":bookings_obj.model_dump()["bookings"]})

if __name__ == "__main__":

    main()