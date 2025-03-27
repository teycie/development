from django.db import models

class Chat(models.Model):
	username = models.CharField(max_length=100)
	chat_message = models. TextField()
	date = models.DateTimeField(auto_now_add=True)

	def _str_(self):
		return f"{self.username}: {self.chat_message[:50]}"
