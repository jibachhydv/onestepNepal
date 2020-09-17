# Generated by Django 3.0 on 2020-09-16 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20200912_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(max_length=400),
        ),
        migrations.AlterField(
            model_name='note',
            name='subject',
            field=models.CharField(choices=[('physic', 'Physic'), ('chemistry', 'Chemistry'), ('botany', 'Botany'), ('zoology', 'Zoology'), ('math', 'Math'), ('english', 'English'), ('nepali', 'Nepali'), ('science', 'science'), ('social', 'Social'), ('eph', 'Environement,Population and Health'), ('Opt', 'Optional Math'), ('cs', 'Computer Science'), ('account', 'Account'), ('business', 'Business'), ('marketing', 'Marketing'), ('general', 'General')], max_length=25),
        ),
    ]