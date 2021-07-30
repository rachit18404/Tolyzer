# Generated by Django 3.1.7 on 2021-04-08 16:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sumissions',
            fields=[
                ('submission_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('uploaded_file', models.FileField(upload_to='upload/')),
                ('status', models.BooleanField()),
            ],
        ),
    ]