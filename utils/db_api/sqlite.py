import sqlite3


class Database:
    def __init__(self, path_to_db="test.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            full_name varchar(255) NOT NULL,
            username varchar(255),
            user_type varchar(50),
            fakultet varchar(50),
            guruh varchar(50),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, full_name: str, username: str, user_type: str = None, fakultet: str = None,  guruh: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, full_name, username, user_type, fakultet, guruh) VALUES(?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, full_name, username, user_type, fakultet, guruh), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_type(self, user_type, id):
        sql = f"UPDATE Users SET user_type=? WHERE id=?"
        return self.execute(sql, parameters=(user_type, id), commit=True)

    def update_fakultet(self, fakultet, id):
        sql = f"UPDATE Users SET fakultet=? WHERE id=?"
        return self.execute(sql, parameters=(fakultet, id), commit=True)

    def update_guruh(self, guruh, id):
        sql = f"UPDATE Users SET guruh=? WHERE id=?"
        return self.execute(sql, parameters=(guruh, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    pass
#     print(f"""
# _____________________________________________________        
# Executing: 
# {statement}
# _____________________________________________________
# """)
