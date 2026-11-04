import os
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from .models import Result

class Command(BaseCommand):
    help = 'Saves a joblib model file to the Django MLModel model.'

    def add_arguments(self, parser):
        parser.add_argument('model_filepath', type=str, help='The file path of the joblib model file.')

    def handle(self, *args, **options):
        model_filepath = options['model_filepath']
        
        if not os.path.exists(model_filepath):
            raise CommandError(f"File '{model_filepath}' does not exist.")

        with open(model_filepath, 'rb') as f:
            django_file = File(f)
            ml_model_instance = Result(name="Random Forest Model", model_file=django_file)
            ml_model_instance.save()

        self.stdout.write(self.style.SUCCESS("Joblib model file saved to the Django model."))
