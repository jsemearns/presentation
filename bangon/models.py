from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Area(models.Model):
    ACCESSIBILITY_CHOICES = (
        ("Accessible", "Accessible"),
        ("Hard to access", "Hard to access"),
        ("Inaccessible", "Inaccessible"),
    )

    name = models.CharField(max_length=255)
    accessibility = models.CharField(max_length=30, choices=ACCESSIBILITY_CHOICES)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="areas")
    population = models.IntegerField()
    other_information = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Donation(models.Model):
    date = models.DateField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="donations")
    donated_by = models.CharField(max_length=255)


class Item(models.Model):
    name = models.CharField(max_length=255)
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, null=True, blank=True, related_name="items"
    )

    def __str__(self):
        return self.name


class DonationItem(models.Model):
    name = models.CharField(max_length=255)
    count = models.IntegerField(null=True, blank=True)
    unit = models.CharField(max_length=100, default="pcs")
    donation = models.ForeignKey(
        Donation, on_delete=models.CASCADE, null=True, blank=True, related_name="items"
    )
