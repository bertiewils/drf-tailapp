from django.db import models
from django_countries.fields import CountryField


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Stadium(BaseModel):
    name = models.CharField(max_length=64, unique=True)
    capacity = models.PositiveIntegerField()


class League(BaseModel):
    name = models.CharField(max_length=64, unique=True)


class FootballTeam(BaseModel):
    name = models.CharField(max_length=64, unique=True)
    country = CountryField(db_index=True)
    year_founded = models.DateField()
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, blank=True, null=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, blank=True, null=True)
