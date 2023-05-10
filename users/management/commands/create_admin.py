from users.models import User
from departments.models import Department
from positions.models import Position
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--username", type=str)
        parser.add_argument("--password", type=str)

    def handle(self, *args, **kwargs):
        username = kwargs["username"]
        password = kwargs["password"]

        if not username:
            username = "admin"

        if not password:
            password = "admin1234"

        if User.objects.filter(username=username).first():
            raise CommandError(f"Username `{username}` already taken.")

        department = Department.objects.create(name="Administrativo")
        position = Position.objects.create(name="Administrador")
        department.positions.add(position)

        User.objects.create_superuser(
            username=username,
            password=password,
            role="Administrator",
            department=department,
            position=position,
        )

        self.stdout.write(
            self.style.SUCCESS(f"Admin `{username}` successfully created!"),
        )
