# Generated by Django 4.1.3 on 2023-01-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udyamHelper', '0002_rename_eventname_event_event_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(unique=True)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('link', models.TextField()),
                ('event', models.CharField(choices=[('Mashal', 'Mashal'), ('Udgam', 'Udgam'), ('Udyam', 'Udyam')], max_length=20)),
            ],
        ),
    ]