# Generated by Django 5.0.4 on 2024-04-30 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_alter_subtask_task_alter_task_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subtask",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="task",
                to="projects.task",
            ),
        ),
    ]
