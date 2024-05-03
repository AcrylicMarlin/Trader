from .data import User

import os
import asqlite
import typing
from uuid import uuid4


class Game_Loop:
    users:typing.List[typing.Tuple[str, User]]
    schemas: typing.List[str]
    def __init__(self):
        with open("./Trader/schema.sql") as f:
            self.schemas = f.read().split(';')
            f.close()
        super().__init__()

    async def startup(self):
        async with self.connection.cursor() as cursor:
            data = await (await cursor.execute(self.schema[1].format("*"))).fetchall()
            for row in data:
                user_id, username, infrastructure, artifact_name, artifact_value, currency = row
                self.users.append((username, User(user_id, infrastructure, currency, artifact_name, artifact_value)))
                
                ...
    
    async def new_user(self, user_name):
        user = User(user_name, uuid4, 0, 1000.0, f"{user_name}_Statue", 1000.0)
        async with self.connection as cursor:
            await cursor.execute(self.schemas[2].format(user.user_id, user.infrastructure, user.artifact_name, user.artifact_value, user.value))
        
        self.user.append((user_name, user))
        ...
    
    
    async def __aenter__(self) -> asqlite.Connection:
        filename = "user_data.db"
        first_time = False
        if not os.path.isfile(f"./Trader/{filename}"):
            first_time = True
        async with asqlite.connect(f"./Trader/{filename}") as data:
            self.connection = data
            # This is purely for debugging
            # Will be removed once database is permanent
            if first_time:
                async with data.cursor() as cursor:
                    await cursor.execute(self.schemas[0])
        
        return data
    
    async def __aexit__(self, *args):
        return await self.connection.close()

