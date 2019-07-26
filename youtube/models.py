from django.db import models


class YoutubeFile(models.Model):
    link = models.URLField()
    uploaded = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return self.link
