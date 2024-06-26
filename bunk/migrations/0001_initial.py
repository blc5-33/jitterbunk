# Generated by Django 3.2 on 2024-06-12 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('photo', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Bunk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='Time')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='bunk.user')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='bunk.user')),
            ],
        ),
    ]
