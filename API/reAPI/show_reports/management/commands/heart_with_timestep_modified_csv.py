# myapp/management/commands/import_csv.py
import csv
import os
from django.core.management.base import BaseCommand, CommandError
from .models import Result
from django.conf import settings

class Command(BaseCommand):
    help = 'Import records from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument(r'C:\Users\compu\Desktop\restAPI\API\heart_with_timestep_modified.csv', type=str, help=r'C:\Users\compu\Desktop\restAPI\API\heart_with_timestep_modified.csv')

    def handle(self, *args, **options):
        csv_filepath = options[r'C:\Users\compu\Desktop\restAPI\API\heart_with_timestep_modified.csv']

        if not os.path.exists(csv_filepath):
            raise CommandError(f"File '{csv_filepath}' does not exist.")

        with open(csv_filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            records_created = 0
            for row in reader:
                # Adjust the field names if necessary
                record, created = Result.objects.get_or_create(
                    sex=row['sex'],
                    chestpaintype=row['chestpaintype'],
                    restingbp=row['restingbp'],
                    defaults={
                        'age': int(row['age']),
                        'cholestrol': int(row['cholesterol']),
                        'maxhr': int(row['maxhr']),
                        'oldpeak': float(row['oldpeak'])
                        },
                    fastingbs=row['fastingbs'],
                    restingecg=row['restingecg'],
                    exerciseangina=row['exerciseangina'],
                    st_slope=row['st_slope'],
                    heartdisease=row['heartdisease'],
                    patientid=row['patientid'],
                    timestep=row['timestep'],
                    heartrate=row['heartrate'],
                    bloodpressure=row['bloodpressure'],
                    oxygensaturation=row['oxygensaturation'],
                )

                if created:
                    records_created += 1

            self.stdout.write(self.style.SUCCESS(f"Successfully imported {records_created} records."))
