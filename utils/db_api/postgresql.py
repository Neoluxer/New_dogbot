# -*- coding: utf-8 -*-
from typing import Union
import asyncpg
from asyncpg.pool import Pool
from data import config


class Database:
    def __init__(self):
        """Создается база данных без подключения в loader"""

        self.pool: Union[Pool, None] = None

    async def create(self):
        """В этой функции создается подключение к базе"""

        pool = await asyncpg.create_pool(
            user=config.PGUSER,  # Пользователь базы (postgres или ваше имя), для которой была создана роль
            password=config.PGPASSWORD,  # Пароль к пользователю
            host=config.ip,  # Ip адрес базы данных. Если локальный компьютер - localhost, если докер - название сервиса
            database='dogs'
        )
        self.pool = pool

    async def create_table_dogs(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Dogs (
        naming VARCHAR (255) NOT NULL,
        breed VARCHAR (255),
        weight DOUBLE PRECISION ,
        birthday VARCHAR (255),
        id INTEGER=NEXTVAL('dogs_id_seq'::regclass) ,
        link TEXT NOT NULL ,
        picture_path TEXT,
        picture_link TEXT,  
        date_now varchar (100),                         
        PRIMARY KEY (name) 
        );
"""
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num + 1}" for num, item in enumerate(parameters)
        ])
        return sql, tuple(parameters.values())
        # id INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,

    async def add_dogs(self, naming: str = 'noname', breed: str = 'no email', weight: float = 0.5,
                       birthday: str = '01.01.01',
                       link: str = '0', picture_path: str = 'no description', picture_link: str = 'unknown'):

        sql = """
        INSERT INTO Dogs(naming,breed,weight,birthday,link,picture_path,picture_link) VALUES($1, $2, $3,$4, $5, $6,$7)
        """
        await self.pool.execute(sql, naming, breed, weight, birthday, link, picture_path, picture_link)

    async def select_all_dogs(self):
        sql = """
        SELECT * FROM Dogs 
        """
        return await self.pool.fetch(sql)

        # return await self.pool.fetch(sql)

    async def select_dog(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = f"""
        SELECT * FROM Dogs WHERE 
        """
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.pool.fetchrow(sql, *parameters)

    async def count_dogs(self):
        return await self.pool.fetchval("SELECT COUNT(*) FROM Dogs")

    async def update_dog_weight(self, weight, name):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET weight=$1 WHERE name=$2
        """
        return await self.pool.execute(sql, weight, name)

    async def delete_dog(self):
        await self.pool.execute("DELETE FROM Dogs WHERE TRUE")

    async def add_to_dictionary_left(self, left: str):
        sql = """
        INSERT INTO Dictionary(left) VALUES($1)
        """
        await self.pool.execute(sql, left)

    async def add_to_dictionary_right(self, right: str):
        sql = """
        INSERT INTO Dictionary(right) VALUES($1)
        """
        await self.pool.execute(sql, right)

    async def add_to_dictionary_forward(self, forward: str):
        sql = """
        INSERT INTO Dictionary(forward) VALUES($1)
        """
        await self.pool.execute(sql, forward)

    async def select_all_dictionary(self):
        sql = """
        SELECT * FROM Dictionary 
        """
        return await self.pool.fetch(sql)