from django.core.management.base import BaseCommand
import json
from blog.models import DismissalArticle,Employees,Document,Deliveries,Books,PublishingHouse,Book,Author

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('/home/fle4a/Django_Project/books.json', type=str)

    def handle(self, *args, **options):
        file_path = options['/home/fle4a/Django_Project/books.json']
        with open(file_path) as f:
            data = json.load(f)
            for obj in data:
                Book.objects.create(**obj)
