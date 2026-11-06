from django.db.backends.mysql.base import DatabaseWrapper as MySQLDatabaseWrapper
from .features import DatabaseFeatures


class DatabaseWrapper(MySQLDatabaseWrapper):
    features_class = DatabaseFeatures

    def check_database_version_supported(self):
        pass  # Salta la validación de versión de MariaDB 10.4