# Generated by Django 5.1 on 2024-09-13 17:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheShowcase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('current_location', models.CharField(blank=True, max_length=255, null=True)),
                ('organization_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('TheShowcase.user',),
        ),
    ]