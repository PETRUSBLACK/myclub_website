# Generated by Django 4.1.5 on 2023-02-08 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyClubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, verbose_name='User Name')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=300)),
                ('zip_code', models.CharField(max_length=15, verbose_name='Zip Code')),
                ('phone', models.CharField(max_length=25, verbose_name='Contact Phone')),
                ('web', models.URLField(verbose_name='Website Address')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, to='events.myclubuser'),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue'),
        ),
    ]