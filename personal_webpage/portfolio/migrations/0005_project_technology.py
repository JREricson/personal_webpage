# Generated by Django 4.1 on 2022-10-07 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0004_project_concepts"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="technology",
            field=models.TextField(max_length=1000, null=True),
        ),
    ]