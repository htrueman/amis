# Generated by Django 3.0.1 on 2019-12-23 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='lecture',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='teachersubject',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='teachersubject',
            name='user',
        ),
        migrations.AddField(
            model_name='group',
            name='lectures',
            field=models.ManyToManyField(to='vcs.Lecture'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='name',
            field=models.CharField(default='test', max_length=150),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='GroupSubject',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='TeacherSubject',
        ),
    ]
