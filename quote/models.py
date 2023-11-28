from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.phone}"

class Owner(models.Model):
    mobile_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.mobile_number} - ({self.email})"

class Subscriber(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"({self.email})"