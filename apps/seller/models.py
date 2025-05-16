from django.db import models


class UserSessionModel(models.Model):
    user_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    context_data = models.JSONField(default=list)
    version = models.CharField(max_length=15)

    class Meta:
        unique_together =(
            ('user_id', 'version')
        )
