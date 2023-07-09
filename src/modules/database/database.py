import sqlite3
import const


class AutoCloseCursur(sqlite3.Cursor):
    # Auto close cursor
    def __init__(self, connection):
        super().__init__(connection)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def dict_factory(cursor, row):
    # Convert sqlite3.Row to dict
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Database:
    def __init__(self, db_path: str = const.DATABSE_PATH):
        self.db_path = db_path
        with sqlite3.connect(db_path) as conn:
            with AutoCloseCursur(conn) as cur:
                # Create tables if not exists
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS user_infos(username, email, name, password, image_path);"
                )
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS chat_logs(chat_id, username, name, message, sent_time);"
                )
            conn.commit()

    def insert_user_info(
        self,
        username: str,
        email: str,
        name: str,
        password: str,
        image_path: str = None,
    ):
        # Insert user info into database
        with sqlite3.connect(self.db_path) as conn:
            with AutoCloseCursur(conn) as cur:
                cur.execute(
                    "INSERT INTO user_infos VALUES (?, ?, ?, ?, ?);",
                    (username, email, name, password, image_path),
                )
            conn.commit()

    def insert_chat_log(
        self, chat_id: str, username: str, name: str, message: str, sent_time: str
    ):
        # Insert chat log into database
        with sqlite3.connect(self.db_path) as conn:
            with AutoCloseCursur(conn) as cur:
                cur.execute(
                    "INSERT INTO chat_logs VALUES (?, ?, ?, ?, ?);",
                    (chat_id, username, name, message, sent_time),
                )
            conn.commit()

    def get_user_info(self, username: str):
        # Get user info from database
        ret_row = None
        with sqlite3.connect(self.db_path) as conn:
            with AutoCloseCursur(conn) as cur:
                cur.execute(
                    "SELECT username, email, name, password, image_path FROM user_infos WHERE username = ?;",
                    (username,),
                )
                ret_row = cur.fetchone()
        return ret_row

    def get_all_user_infos(self):
        # Get all user infos from database
        ret_rows = None
        with sqlite3.connect(self.db_path) as conn:
            with AutoCloseCursur(conn) as cur:
                cur.execute(
                    "SELECT username, email, name, password, image_path FROM user_infos;"
                )
                ret_rows = cur.fetchall()
        return ret_rows

    def get_chat_log(self, chat_id: str, limit: int = None):
        # Get chat log from database
        ret_rows = None
        with sqlite3.connect(self.db_path) as conn:
            with AutoCloseCursur(conn) as cur:
                if limit is None:
                    cur.execute(
                        "SELECT chat_id, username, name, message, sent_time FROM chat_logs WHERE chat_id = ? ORDER BY sent_time ASC;",
                        (chat_id,),
                    )
                else:
                    cur.execute(
                        "SELECT chat_id, username, name, message, sent_time FROM chat_logs WHERE chat_id = ? ORDER BY sent_time ASC LIMIT ?;",
                        (chat_id, limit),
                    )
                ret_rows = cur.fetchall()
        return ret_rows

    def update_user_info_password(self, username: str, password: str):
        # Update user info password in database
        with sqlite3.connect(self.db_path) as conn:
            with AutoCloseCursur(conn) as cur:
                cur.execute(
                    "UPDATE user_infos SET password = ? WHERE username = ?;",
                    (password, username),
                )
            conn.commit()

    def update_user_info_image_path(self, username: str, image_path: str):
        # Update user info image path in database
        with sqlite3.connect(self.db_path) as conn:
            with AutoCloseCursur(conn) as cur:
                cur.execute(
                    "UPDATE user_infos SET image_path = ? WHERE username = ?;",
                    (image_path, username),
                )
            conn.commit()