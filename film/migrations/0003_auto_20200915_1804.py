# Generated by Django 3.1.1 on 2020-09-15 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_auto_20200915_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geenre',
            old_name='title',
            new_name='geenre_title',
        ),
        migrations.AddField(
            model_name='film',
            name='cover',
            field=models.FileField(default='1', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='status',
            field=models.CharField(choices=[('Coming Soon', 'Coming Soon'), ('Now', 'Now')], default='1', max_length=20),
            preserve_default=False,
        ),
    ]
