from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from site_app.telegram_bot import bot


class Command(BaseCommand):
    help = 'Create default Django Admin user'

    def handle(self, *args, **options):
        self.stdout.write("Creating default admin user")
        try:
            admin_user = User.objects.create_superuser(
                'admin',
                'admin@mysite.ru',
                password='sS8zK5bG6sH8hB0p'
            )
            self.stdout.write(str(admin_user))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка: {str(e)}'))
