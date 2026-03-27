from sqlalchemy import create_engine
from sqlalchemy.sql import text


class StudentTable:
    scripts = {
        "select": text("SELECT * FROM student"),
        "select_by_id": text("SELECT * FROM student WHERE user_id = :user_id"),
        "select_max_id": text("SELECT MAX(user_id) FROM student"),
        "insert": text("INSERT INTO student (user_id) VALUES (:user_id)"),
        "update": text("UPDATE student SET level = :level"
                       " WHERE user_id = :user_id"),
        "delete": text("DELETE FROM student WHERE user_id = :user_id"),
    }

    def __init__(self, connection_string: str):
        self._db = create_engine(connection_string)

    def get_all(self):
        with self._db.connect() as conn:
            result = conn.execute(self.scripts["select"])
            return result.fetchall()

    def get_by_id(self, user_id: int):
        with self._db.connect() as conn:
            result = conn.execute(
                self.scripts["select_by_id"], {"user_id": user_id}
            )
            return result.fetchall()

    def get_max_id(self):
        with self._db.connect() as conn:
            result = conn.execute(self.scripts["select_max_id"])
            row = result.fetchone()
            return row[0] if row and row[0] is not None else 0

    def insert(self, user_id: int):
        with self._db.connect() as conn:
            conn.execute(self.scripts["insert"], {"user_id": user_id})
            conn.commit()

    def update(self, user_id: int, level: str):
        with self._db.connect() as conn:
            conn.execute(
                self.scripts["update"],
                {"user_id": user_id, "level": level}
            )
            conn.commit()

    def delete(self, user_id: int):
        with self._db.connect() as conn:
            conn.execute(self.scripts["delete"], {"user_id": user_id})
            conn.commit()
