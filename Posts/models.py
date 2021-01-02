from django.db import models

# Create your models here.


class Member(models.Model):
    memberName = models.CharField(
        verbose_name="Member Username", max_length=200)
    joinDate = models.DateTimeField(
        verbose_name="joinDate", auto_now_add=True)

    def __str__(self):
        return str(self.memberName)


class Group(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    createBy = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="group Name", unique=True, max_length=200)

    def __str__(self):
        return str(self.name)



class Like(models.Model):
    count = models.BigIntegerField(verbose_name=" Like Count",default = 0)
    group = models.ManyToManyField(Group)

    def __str__(self):
        return str(self.count)


            