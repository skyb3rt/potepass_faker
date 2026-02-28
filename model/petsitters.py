from __future__ import annotations

from pydantic import BaseModel


class PetSitter(BaseModel):
    id: int
    name: str
    location: str
    pricePerDay: int
    rating: None|float
    reviewCount: int
    maxDogs: int
    acceptsPuppies: bool
    acceptsLargeDogs: bool
    yearsOfExperience: int
    experienceDescription: str
    available: bool
    created: str
    updated: str


class Model(BaseModel):
    petSitters: list[PetSitter]
