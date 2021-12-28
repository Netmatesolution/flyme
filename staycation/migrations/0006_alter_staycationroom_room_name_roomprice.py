# Generated by Django 4.0 on 2021-12-25 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('staycation', '0005_remove_staycationroom_cancellationpolicy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staycationroom',
            name='room_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='RoomPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_nights', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('host_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('room_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staycation.staycationroom')),
                ('staycation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staycation.staycation')),
            ],
        ),
    ]
