from django.db import models

# Create your models here.
class Election(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Voter(models.Model):
    email = models.CharField(max_length=255)
    one_time_password = models.CharField(max_length=255)
    election = models.ForeignKey("Election", on_delete=models.CASCADE, blank=True, null=True, related_name="voters")
    claimed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} - {self.election.name}"

class Token(models.Model):
    token = models.CharField(max_length=255, unique=True)
    election = models.ForeignKey("Election", on_delete=models.CASCADE, blank=True, null=True, related_name="tokens")

    def __str__(self):
        return f"{self.token} - {self.election.name}"
