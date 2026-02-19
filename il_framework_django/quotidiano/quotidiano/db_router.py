class NewsRouter:
    app_label = {"news"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.app_label:
            return "oracle_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.app_label:
            return "oracle_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # Permette relazioni solo se almeno uno dei due è nell'app "quotidiano"
        if (
            obj1._meta.app_label in self.app_label or
            obj2._meta.app_label in self.app_label
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Le migration dell'app "quotidiano" vanno solo sul MySQL
        if app_label in self.app_label:
            return db == "oracle_db"
        # Tutto il resto resta sul database di default
        return db == "default"

