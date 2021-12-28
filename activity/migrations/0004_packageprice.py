# Generated by Django 4.0 on 2021-12-26 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('activity', '0003_rename_activity_id_package_activity_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packageprice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('minimumCount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('activity_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.activity')),
                ('host_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.package')),
            ],
        ),
    ]
