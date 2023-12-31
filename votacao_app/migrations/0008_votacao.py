# Generated by Django 4.1.1 on 2023-07-02 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("votacao_app", "0007_alter_aluno_grupo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Votacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="votacao_app.aluno",
                        unique=True,
                    ),
                ),
                (
                    "grupo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="votacao_app.grupo",
                    ),
                ),
            ],
        ),
    ]
