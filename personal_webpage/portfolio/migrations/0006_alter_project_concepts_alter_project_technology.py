# Generated by Django 4.1 on 2022-10-07 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0005_project_technology"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="concepts",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="technology",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
