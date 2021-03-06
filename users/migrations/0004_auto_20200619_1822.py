# Generated by Django 3.0.7 on 2020-06-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200619_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='current_city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
