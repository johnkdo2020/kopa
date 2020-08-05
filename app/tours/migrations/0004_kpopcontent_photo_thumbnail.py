# Generated by Django 2.2.13 on 2020-08-05 04:25

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_auto_20200804_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='kpopcontent',
            name='photo_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default='', upload_to='content/thumbnail'),
            preserve_default=False,
        ),
    ]
