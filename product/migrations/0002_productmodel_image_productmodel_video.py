# Generated by Django 5.0.6 on 2024-08-27 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='video',
            field=models.FileField(default='path/to/default/video.mp4', upload_to='videos/'),
        ),
    ]
