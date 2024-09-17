# Generated by Django 5.1.1 on 2024-09-16 04:04

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('university_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('num_students', models.IntegerField()),
                ('website', models.URLField()),
            ],
        ),
        migrations.RenameField(
            model_name='mentor',
            old_name='company_name',
            new_name='organization_name',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='current_location',
        ),
        migrations.AddField(
            model_name='user',
            name='current_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='registrationapp.user')),
                ('company_name', models.CharField(max_length=255)),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='registrationapp.university')),
            ],
            options={
                'abstract': False,
            },
            bases=('registrationapp.user',),
        ),
    ]
