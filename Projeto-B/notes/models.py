from django.db import models


DEFAULT_EXAM_ID = 1

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
      return f"{self.name}"

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    tag_id = models.ForeignKey(Tag, default=DEFAULT_EXAM_ID, on_delete=models.CASCADE)

    def __str__(self):
      return f"{self.id}. {self.title}"
