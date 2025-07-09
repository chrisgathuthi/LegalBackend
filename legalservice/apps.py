from django.apps import AppConfig


class LegalserviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'legalservice'
    
    def ready(self):
        import legalservice.signals
