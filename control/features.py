from django.db.backends.mysql.features import DatabaseFeatures as MySQLDatabaseFeatures


class DatabaseFeatures(MySQLDatabaseFeatures):
    # Desactiva el soporte de RETURNING para evitar el error de sintaxis en MariaDB 10.4
    can_return_rows_from_bulk_insert = False
    uses_savepoints = True