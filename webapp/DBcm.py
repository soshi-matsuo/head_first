import mysql.connector

class UseDatabase:

    def __init__(self, config: dict):
        self.configuration = config

    def __enter__(self):
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.DatabaseError as err:
            raise NoDBError(err)
        except mysql.connector.ProgrammingError as err:
            raise CredentialError(err)

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mysql.connector.ProgrammingError:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)


class NoDBError(Exception):
    pass

class CredentialError(Exception):
    pass

class SQLError(Exception):
    pass