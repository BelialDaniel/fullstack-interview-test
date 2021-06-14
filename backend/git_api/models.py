from django.db import models

class Author(models.Model):
    class Meta:
        db_table='authors'

    name = models.TextField(max_length=30, null=False)
    last_name = models.TextField(max_length=30, null=False)
    email = models.EmailField(max_length=400)

class PullRequest(models.Model):
    class Meta:
        db_table = 'pull_requests'

    class Status(models.TextChoices):
        OPEN = 'open', 'Open'
        CLOSE = 'closed', 'Closed'
        MERGED = 'merged', 'Merged'
    
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    title = models.TextField(max_length=150, null=False)
    description = models.TextField(max_length=5000, null=False, default='')
    status = models.CharField(max_length=20,
                              choices=Status.choices,
                              default=Status.OPEN)
