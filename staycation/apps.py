from django.apps import AppConfig


class StaycationConfig(AppConfig):
    name = 'staycation'
    def ready(self):
        import staycation.signals
