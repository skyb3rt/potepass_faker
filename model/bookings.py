from __future__ import annotations

from pydantic import BaseModel


class Booking(BaseModel):
    id: int
    userId: int
    userDogId: int
    petSitterId: int
    fromDate: str
    toDate: str
    status: str
    message: str
    rating: None|int
    payed: None| bool
    created: str
    updated: str


class Model(BaseModel):
    bookings: list[Booking]
