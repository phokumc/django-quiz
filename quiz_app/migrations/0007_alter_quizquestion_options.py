# Generated by Django 4.2 on 2023-04-16 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0006_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizquestion',
            options={'ordering': ['-id']},
        ),
    ]