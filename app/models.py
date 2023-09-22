from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from django.contrib.auth import get_user_model

User = get_user_model()


def get_podcast_image_path(instance, filename):
    podcast_id = str(instance.pk).replace("-", "")
    return f"uploads/podcast/{podcast_id}/{filename}"


def get_episode_audio_path(instance, filename):
    podcast_id = ""
    episode_id = str(instance.pk).replace("-", "")
    ext = filename.split(".")[-1]
    if instance.podcast:
        podcast_id = str(instance.podcast.pk).replace("-", "")
    return f"uploads/podcast/{podcast_id}/episodes/epi_{episode_id}.{ext}"


class Podcast(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid4)
    name = models.TextField(null=True)
    slug = models.SlugField()
    description = models.TextField(null=True)
    attachment = models.FileField(upload_to=get_podcast_image_path)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'podcast'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def create(self, request, *args, **kwargs):
        data = request.data

        obj = Podcast()
        for key, val in data.items():
            if hasattr(obj, key):
                setattr(obj, key, val)
        obj.uploader = request.user
        obj.save()
        return {"message": "Created successfully"}

    def list(self):
        queryset = Podcast.objects.all()
        return queryset


class Episode(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid4)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    audio = models.FileField(upload_to=get_episode_audio_path, max_length=500)
    slug = models.SlugField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'episode'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def create(self, request, *args, **kwargs):
        podcast_id = kwargs.get("podcastId")
        data = request.data
        obj = Episode()
        for key, val in data.items():
            if hasattr(obj, key):
                setattr(obj, key, val)
        obj.uploader = request.user
        obj.podcast_id = podcast_id
        obj.save()
        return {"message": "Created successfully"}

    def list(self,**kwargs):
        queryset = {}
        if kwargs.get("podcastId"):
            queryset = Episode.objects.filter(podcast_id=kwargs.get("podcastId"))
        return queryset


class UpVotes(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'upvotes'
