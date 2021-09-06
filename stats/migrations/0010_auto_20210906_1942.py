# Generated by Django 3.2.6 on 2021-09-06 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0009_auto_20210905_2327'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlayerDetailsModel',
            new_name='PlayerModel',
        ),
        migrations.AddField(
            model_name='gamemodel',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_player', to='stats.playermodel'),
        ),
        migrations.AddField(
            model_name='gamemodel',
            name='table_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='GamesByPlayerModel',
        ),
    ]