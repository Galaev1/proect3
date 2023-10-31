from django.core.management import BaseCommand

from skystore.models import Student


class Command(BaseCommand):
    def handle(self,*args,**options):
        student_list = [
            {'last_name': 'danu','first_name':'bunov'},
            {'last_name': 'manu','first_name': 'gunov'}
        ]
        for s in student_list:
            Student.objects.create(**s)