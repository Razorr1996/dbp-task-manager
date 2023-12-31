# Generated by Django 4.2.5 on 2023-10-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_rename_due_to_task_deadline_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="tag",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
