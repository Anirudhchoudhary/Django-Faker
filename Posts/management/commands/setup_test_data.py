import random

from django.db import transaction
from django.core.management.base import BaseCommand

from Posts.models import Member

from Posts.factories import MemberFactory,GroupFactory,LikeFactory

class Command(BaseCommand):
    help = "Genrate Test Data"

    @transaction.atomic
    def handle(self , *args , **kwargs):
        self.stdout.write("Deleting Old Data")
        Member.objects.all().delete()
        self.stdout.write("Creating new Data")
        people = []
        for _ in range(500):
            person = MemberFactory()
            people.append(person)


        group_data = []
        for _ in range(500):
            group = GroupFactory()
            m = random.choice(people)
            group.member = m
            group_data.append(group)


        for _ in range(500):
            _like = LikeFactory()
            group_choice = random.choices(group_data)
            
            _like.group.set(group_choice)
        
        
        