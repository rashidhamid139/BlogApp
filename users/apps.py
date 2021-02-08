from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = 'user_proifiles'
    
    def ready(self):
        import users
