import asyncio
from bot.postgres_database.storage_postgres import StoragePostgres


async def main():
    await StoragePostgres().recreate_db()


if __name__ == "__main__":
    asyncio.run(main())
