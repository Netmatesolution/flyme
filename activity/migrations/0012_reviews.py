# Generated by Django 4.0 on 2022-04-09 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('activity', '0011_rename_video_link_activity_video_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('firstname', models.CharField(default='', max_length=500)),
                ('lastname', models.CharField(default='', max_length=500)),
                ('message', models.TextField(blank=True, null=True)),
                ('activity_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.activity')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
