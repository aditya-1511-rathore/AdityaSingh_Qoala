# Generated by Django 4.2.6 on 2023-12-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_ocrresult_dob_ocrresult_doi_ocrresult_id_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ocrresult',
            old_name='dob',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='ocrresult',
            old_name='doi',
            new_name='date_of_expiry',
        ),
        migrations.AddField(
            model_name='ocrresult',
            name='date_of_issue',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
