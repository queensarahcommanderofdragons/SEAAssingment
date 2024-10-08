# Generated by Django 5.1.1 on 2024-09-26 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_profile_id'),
        ('billing', '0003_rename_profile_bill_user_alter_bill_unique_together_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='user',
            new_name='profile',
        ),
        migrations.AlterUniqueTogether(
            name='bill',
            unique_together={('profile', 'address')},
        ),
    ]
