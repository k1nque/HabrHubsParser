import sqlite3
import aiosqlite


async def add_article(article_id: int, article_values: dict[str, str]) -> None:
    async with aiosqlite.connect('database.db') as db:
        await db.execute("INSERT INTO articles ("
                         "id, hub_name, title, author_name, author_link, datetime, link)"
                         "VALUES "
                         "(?, ?, ?, ?, ?, ?, ?)", (article_id, *article_values.values()))
        await db.commit()


async def is_article_in_table(article_id: int) -> bool:
    async with aiosqlite.connect('database.db') as db:
        async with db.execute('SELECT * FROM articles '
                              f'WHERE id = {article_id}', ) as cur:
            rows = await cur.fetchall()
            return len(rows) == 1


def select_all_hubs():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM hubs')
        hubs = cursor.fetchall()
        return [el[1] for el in hubs]


def create_tables() -> None:
    with sqlite3.connect('database.db') as db:
        db.execute("CREATE TABLE IF NOT EXISTS hubs ("
                   "id INT PRIMARY KEY,"
                   "hub_name VARCHAR(50)"
                   ")")

        db.execute("CREATE TABLE IF NOT EXISTS articles ("
                   "id INT PRIMARY KEY,"
                   "hub_name VARCHAR(50),"
                   "title VARCHAR(150),"
                   "author_name VARCHAR(50),"
                   "author_link VARCHAR(75),"
                   "datetime VARCHAR(25),"
                   "link VARCHAR(75)"
                   ")")
