import factory
from factory.django import DjangoModelFactory

from Posts.models import Member , Group , Like


class MemberFactory(DjangoModelFactory):
    class Meta:
        model = Member
    

    memberName = factory.Faker("first_name")


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group
    
    name = factory.Faker("sentence")
    member = factory.SubFactory(MemberFactory)


class LikeFactory(DjangoModelFactory):
    class Meta:
        model = Like

    count = factory.Faker("numerify")
    

    