# Generated by Django 4.2.7 on 2023-12-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_student_levels_alter_student_date_ofj'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Course name')),
                ('coden', models.CharField(blank=True, max_length=255, null=True, verbose_name='Code name')),
            ],
        ),
    ]