from django.db import models

class Room(models.Model):
    IS_LIT =        [('L', 'Lit'), ('D', 'Dark')]
    name =          models.CharField(max_length = 100)
    wall_texture =  models.CharField(max_length = 100)
    floor_texture = models.CharField(max_length = 100)
    description =   models.TextField()
    width =         models.IntegerField()
    length =        models.IntegerField()
    lit =           models.CharField(max_length=1, choices=IS_LIT)
    create_date =   models.DateTimeField()
    doors =         models.ManyToManyField('Door')

class Door(models.Model):
    WALL = [('N', 'North'), ('E', 'East'), ('S', 'South'), ('W', 'West')]
    location =  models.CharField(max_length=1, choices=WALL)
    position =  models.IntegerField() 