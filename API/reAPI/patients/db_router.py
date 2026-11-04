class dbrouter:

    def db_for_read(self, model, **hints):
        if model._meta.apps_label == 'patients':
            return "gradproject"
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.apps_label == 'patients':
            return "gradproject"
        return None
        