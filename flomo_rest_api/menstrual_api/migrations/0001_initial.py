# Generated by Django 4.1.1 on 2022-09-15 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menstrual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloody', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('flow', models.TextField()),
                ('cramps', models.BooleanField(default=False)),
                ('migraine', models.BooleanField(default=False)),
                ('bloating', models.BooleanField(default=False)),
                ('emo', models.BooleanField(default=False)),
                ('anger', models.BooleanField(default=False)),
                ('food', models.BooleanField(default=False)),
                ('sex', models.BooleanField(default=False)),
                ('nausea', models.BooleanField(default=False)),
                ('sore', models.BooleanField(default=False)),
                ('fatigue', models.BooleanField(default=False)),
                ('aches', models.BooleanField(default=False)),
                ('patriarchy', models.BooleanField(default=False)),
            ],
        ),
    ]
