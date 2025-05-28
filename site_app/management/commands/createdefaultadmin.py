from django.core.management.base import BaseCommand

from site_app.models import CustomUser


class Command(BaseCommand):
    help = 'Create default Django Admin user'

    def handle(self, *args, **options):
        self.stdout.write("Creating default admin user")
        try:
            admin_user = CustomUser.objects.create_superuser(
                'admin',
                'admin@mysite.ru',
                password='sS8zK5bG6sH8hB0p'
            )
            self.stdout.write(str(admin_user))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка: {str(e)}'))
