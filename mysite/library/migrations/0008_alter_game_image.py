# Generated by Django 5.0.1 on 2024-02-29 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='game_images/'),
        ),
    ]
