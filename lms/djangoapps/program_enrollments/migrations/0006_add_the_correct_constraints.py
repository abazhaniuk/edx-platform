# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-23 15:37


from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('program_enrollments', '0005_canceled_not_withdrawn'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='programenrollment',
            unique_together=set([('user', 'program_uuid', 'curriculum_uuid'), ('external_user_key', 'program_uuid', 'curriculum_uuid')]),
        ),
    ]
