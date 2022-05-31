from typing import Union

import asyncpg
from asyncpg import Pool, Connection

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_films(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Films (
        id SERIAL PRIMARY KEY,
        link VARCHAR(255) NOT NULL,
        title VARCHAR(255) NULL,
        url VARCHAR(255) NULL,
        poster VARCHAR(255) NULL
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([f'{item} = ${num}' for num, item in enumerate(parameters.keys(), start=1)])
        return sql, tuple(parameters.values())

    async def add_film(self, link, title, url, poster):
        sql = "INSERT INTO Films(link, title, url, poster) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, link, title, url, poster, fetchrow=True)

    async def select_all_films(self):
        sql = "SELECT * FROM Films"
        return await self.execute(sql, fetch=True)

    async def select_film(self, **kwargs):
        sql = "SELECT * FROM Films WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def update_film_title_poster(self, title, poster, link):
        sql = "UPDATE Films SET title=$1, poster=$2 WHERE link=$3"
        return await self.execute(sql, title, poster, link, execute=True)

    async def update_film_url(self, url, link):
        sql = "UPDATE Films SET url=$1 WHERE link=$2"
        return await self.execute(sql, url, link, execute=True)
