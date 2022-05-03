from django.db import models
from authentication.models import User
from projects.models import Project

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField()
    priority = models.BooleanField()
    type = models.BooleanField(default=True)
    description = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    # Next time do not create VVV with _id at the end. The database automatically adds id to the end
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_posted = models.DateField()
    ticket_author = models.ForeignKey(User, related_name='ticket_author',on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User, related_name='assigned_to')