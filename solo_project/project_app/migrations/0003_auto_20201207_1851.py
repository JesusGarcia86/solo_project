# Generated by Django 2.2 on 2020-12-07 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0002_forum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='description',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='item',
        ),
        migrations.AlterField(
            model_name='forum',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='project_app.User'),
        ),
    ]
