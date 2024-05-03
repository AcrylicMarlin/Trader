import typing
import asyncio
import Trader







async def main():
    # users = Trader.generate_test_users()
    # for user in users:
    #     print(user)
    with open("./Trader/schema.sql") as f:
        schemas = []
        for line in f.read().split(";"):
            line = line.replace('\n', '')
            line = line.split(':')
            schemas.append((line[0], line[1]))
            # schemas = [(command, schema) for command, schema in line]
        # schemas = [(command, schema) for command, schema in [pair.split(':') for pair in [line for line in f.read().split(';')]]]
        f.close()
        for pair in schemas:
            print(pair[0], pair[1], "\n")
    ...
if __name__ == '__main__':
    asyncio.run(main())