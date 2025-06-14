from django.db import models
import uuid

class NewsCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
