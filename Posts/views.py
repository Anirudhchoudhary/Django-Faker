from django.shortcuts import render
from .decorator import query_debugger
# Create your views here.
from .models import Group , Like


"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all_group_list():


Function : all_group_list
Number of Queries : 501
Finished in : 0.43s
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

group_list():

Function : group_list
Number of Queries : 1
Finished in : 0.04s
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


Like_count():


Function : Like_count
Number of Queries : 501
Finished in : 0.73s


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Function : like_list_prefetch_related
Number of Queries : 2
Finished in : 0.20s


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""

@query_debugger
def group_list():
    queryset = Group.objects.select_related("member").all() 
    group = []
    for g in queryset:
        group.append({'id':g.id , 'group_name':g.name , "member":g.member.memberName})
    return group

@query_debugger
def all_group_list():
    queryset = Group.objects.all() 
    group = []
    for g in queryset:
        group.append({'id':g.id , 'group_name':g.name , "member":g.member.memberName})
    return group

@query_debugger
def Like_count():
    queryset = Like.objects.all()

    l = []

    for s in queryset:
        bo = [b.name for b in s.group.all()]
        l.append({'id':s.id , 'count':s.count , 'group':bo})
    
    return l


@query_debugger
def like_list_prefetch_related():
  
    queryset = Like.objects.prefetch_related('group')

    stores = []

    for s in queryset:
        books = [book.name for book in s.group.all()]
        stores.append({'id': s.id, 'count': s.count, 'books': books})

    return stores

