import typing
import asyncio
from Trader import User_Data







async def main():
    data_class = User_Data()
    async with data_class as database:
        print(database)

if __name__ == '__main__':
    asyncio.run(main())