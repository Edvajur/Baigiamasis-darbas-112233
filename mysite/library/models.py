from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200, help_text="Write game genre")

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(verbose_name="Name", max_length=200)
    developer = models.ForeignKey('Developer', on_delete=models.SET_NULL, null=True, blank=True, related_name='games_developed')
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True, blank=True, related_name='games_published')
    summary = models.TextField(verbose_name="Summary", max_length=5000, help_text="Game summary", default="No summary available.")
    genre = models.ManyToManyField('Genre', verbose_name="Genre", help_text="Delete genre for this game")
    image = models.ImageField(upload_to='media/', default='default.jpg')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Comment(models.Model):
        game = models.ForeignKey('Game', on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        text = models.TextField()
        created_date = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.text[:300]

        # class Meta:
        #     ordering = ['title']
        #
        # def __str__(self):
        #     return f"{self.title} (Developer: {self.developer}, Publisher: {self.publisher})"


# I might delete this since it feels like this is duplication of my previews code.
# class Game(models.Model):
#      """Model representing a game."""
#      title = models.CharField(max_length=200)
#      developer_name = models.CharField(verbose_name='Developer Name', max_length=100)
#      publisher_name = models.CharField(verbose_name='Publisher Name', max_length=100)
#      # Add other game-specific fields if necessary, such as release_date, genre, platform, etc.
#
#      class Meta:
#          ordering = ['title', 'developer_name', 'publisher_name']
#
#      def __str__(self):
#          """String for representing the Model object."""
#          return f'{self.title} (Developer: {self.developer_name}, Publisher: {self.publisher_name})'