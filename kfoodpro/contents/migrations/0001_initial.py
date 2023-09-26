# Generated by Django 4.2.5 on 2023-09-22 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Food",
            fields=[
                ("num", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("efficacy", models.CharField(max_length=100)),
                ("origin", models.CharField(max_length=300)),
                ("count", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                ("num", models.BigAutoField(primary_key=True, serialize=False)),
                ("answer", models.IntegerField(default=0)),
                ("image1", models.CharField(max_length=300)),
                ("regdate", models.DateTimeField(auto_now_add=True)),
                (
                    "fnum",
                    models.ForeignKey(
                        db_column="fnum",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="food",
                        to="contents.food",
                    ),
                ),
            ],
        ),
    ]