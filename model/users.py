from __future__ import annotations

from pydantic import BaseModel


class Dog(BaseModel):
    id: int
    name: str
    breed: str
    age: int
    allergies: list[str]


class User(BaseModel):
    id: int
    userName: str
    password: str
    email: str
    description: str
    dogs: list[Dog]
    created: str
    updated: str


class Model(BaseModel):
    users: list[User]
