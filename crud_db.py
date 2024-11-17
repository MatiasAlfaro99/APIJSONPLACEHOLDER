import sqlite3

class CRUDDB:
    DATABASE = "database.db"

    @staticmethod
    def initialize():
        """Inicializa la base de datos con una tabla."""
        conn = sqlite3.connect(CRUDDB.DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                body TEXT,
                userId INTEGER
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def insert_post(title, body, user_id):
        """Inserta un registro en la base de datos."""
        conn = sqlite3.connect(CRUDDB.DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO posts (title, body, userId) VALUES (?, ?, ?)
        ''', (title, body, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_posts():
        """Obtiene todos los registros de la base de datos."""
        conn = sqlite3.connect(CRUDDB.DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()
        conn.close()
        return posts

    @staticmethod
    def delete_post(post_id):
        """Elimina un registro de la base de datos."""
        conn = sqlite3.connect(CRUDDB.DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        conn.commit()
        conn.close()
