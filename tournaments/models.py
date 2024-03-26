import uuid
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Tournament(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    name = models.CharField(db_index=True)
    description = models.TextField()
    date_start = models.DateField(db_index=True)
    date_end = models.DateField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.utcnow()
        self.modified = datetime.now()
        return super().save(*args, **kwargs)
