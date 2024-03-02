from django.core.management.base import BaseCommand
from ...models import Kitten


class Command(BaseCommand):
    help = 'seed database for development'

    def handle(self, *args, **options):
        # execute seed command
        self.stdout.write('deleting data...')
        self.delete_all()
        self.stdout.write('done')
        self.stdout.write('seeding data...')
        self.seed()
        self.stdout.write('done')

    def delete_all(self):
        """delete all events in database"""
        Kitten.objects.all().delete()

    def seed(self):
        """Seeds the database"""
        for i in range(99):
            Kitten.objects.create(name=f'Kitten_{i+1}', age=i%10+1, cuteness=i, softness=i)
