
from django.db import models


class ToDo(models.Model):
	name = models.CharField(max_length=100, help_text="Task name", default="Untitled")
	description = models.CharField(max_length=255, blank=True, help_text="Task description")
	deadline = models.DateTimeField(null=True, blank=True, help_text="Deadline (optional)")
	is_complete = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	deleted_at = models.DateTimeField(null=True, blank=True, help_text="Time of deletion (for soft delete)")

	def __str__(self):
		return self.name
