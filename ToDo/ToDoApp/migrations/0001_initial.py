# Generated by Django 3.2.6 on 2021-08-16 18:44

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ToDoApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Title')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
                ('isComplated', models.BooleanField(verbose_name='isCompleted')),
            ],
        ),
    ]
