# Generated by Django 5.0.3 on 2024-03-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cluster",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=64)),
                ("version", models.CharField(max_length=5)),
                ("kubeconfig", models.TextField()),
            ],
        ),
    ]