class SecondaryDatabaseRouter:
    """
    Enrutador para redirigir el modelo de usuario personalizado a la base de datos secundaria.
    """

    def db_for_read(self, model, **hints):
        """
        Indica a Django a qué base de datos enviar las consultas de lectura para el modelo especificado.
        """
        if model._meta.app_label == 'Web_app' and model._meta.model_name == 'usuario':
            return 'secondary'
        return None

    def db_for_write(self, model, **hints):
        """
        Indica a Django a qué base de datos enviar las consultas de escritura para el modelo especificado.
        """
        if model._meta.app_label == 'Web_app' and model._meta.model_name == 'usuario':
            return 'secondary'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permite relaciones si ambos objetos están en la misma base de datos.
        """
        if obj1._meta.app_label == 'Web_app' and obj2._meta.app_label == 'Web_app':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Permite la migración si la app es la de usuarios personalizados y la base de datos es la secundaria.
        """
        if app_label == 'Web_app' and model_name == 'usuario' and db == 'secondary':
            return True
        return None