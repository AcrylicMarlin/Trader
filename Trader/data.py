import typing
from dataclasses import dataclass, replace
import inspect
import random

@dataclass(order = True)
class User:
    user_id:int
    infrastructure:...
    value:float
    artifact_name:str
    artifact_value:float

# Generates 100 test users for data testing
def generate_test_users():

    users = []
    for i in range(100):
        users.append((
            f"Person{i}", 
            User(
                f"Person{i}",
                random.randint(1, 1000),
                random.randint(1,10),
                random.randint(1, 1000),
                f"Person{i}_Statue",
                random.randint(1, 1000))))


# for i in range(10):
#     look_for = f'Person{random.randint(1,99)}'
#     user = next(v for i, v in enumerate(users) if v[0] == look_for)
#     print(user)

class Infrastructure:
    ...

class Material:
    ...



    