import typing
from dataclasses import dataclass, replace, field
import uuid
import sqlite3
import json

"""
User_Data Columns
user
user_name
artifact_name
artifact_value
currency

User_Infrastructure
coal_mines

User_Materials
coal

"""
with open("./Trader/values.json") as file:
    values_table = json.load(file)

infrastructure = values_table["infrastructure"]
materials = values_table["materials"]

def generate_user(user_row:sqlite3.Row, material_row:sqlite3.Row, infrastructure_row:sqlite3.Row):
    user_id, user_name, artifact_name, artifact_value, currency = user_row
    return (user_name,
            User(
                user_id,
                [(k, v) for k, v in infrastructure_row].pop(0),
                [(k,v) for k,v in material_row].pop(0),
                currency,
                artifact_name,
                artifact_value
        )
    )

def generate_new_user(user_name):
    return (
        user_name,
        User(
            artifact_name = f"{user_name}_Statue",
            infrastructure=[
                ("coal_plant",
                    Infrastructure("coal_plant",
                        infrastructure["coal_plant"]["cost"],
                        tuple(infrastructure["coal_plant"]["produces"].split(" "))
                    )
                )
            ]
        )
    )


@dataclass(order = True)
class Material:
    name:str = field(default="Unknown")
    value:float = field(default=1)
    produced_in:str = field(default_factory=list)
@dataclass(order = True)
class Infrastructure:
    name:str = field(default="Unknown")
    costs:typing.Dict[str, typing.Any] = field(default_factory=dict)
    produces:typing.Tuple[Material, int] = field(default_factory=tuple)

@dataclass(order = True)
class User:
    user_id:str = field(default=uuid.uuid4())
    infrastructure: typing.List[typing.Tuple] = field(default_factory=list)
    materials:typing.List[typing.Tuple] = field(default_factory=list)
    value:float = field(default=1000.0)
    artifact_name:str = field(default="Default_User_Statue")
    artifact_value:float = field(default=1000.0)


# Generates 100 test users for data testing
def generate_test_users():
    users = []
    for i in range(100):
        users.append(
            generate_new_user(f"Person{i}")
        )
    return users

# for i in range(10):
#     look_for = f'Person{random.randint(1,99)}'
#     user = next(v for i, v in enumerate(users) if v[0] == look_for)
#     print(user)
