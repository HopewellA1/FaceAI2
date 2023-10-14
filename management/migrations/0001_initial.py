# Generated by Django 4.1.7 on 2023-10-06 07:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('GroupId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('GroupCode', models.CharField(max_length=5)),
                ('numStudents', models.IntegerField(default=1)),
                ('status', models.CharField(default='Active', max_length=30)),
                ('DateCreated', models.DateTimeField(default=datetime.datetime(2023, 10, 6, 9, 46, 24, 147847))),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('LectureId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('numGroups', models.IntegerField(default=1)),
                ('PhoneNumber', models.CharField(default='+27', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('ModuleId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('ModuleName', models.CharField(max_length=150)),
                ('ModuleCode', models.CharField(max_length=20)),
                ('numGroups', models.IntegerField(default=0)),
                ('Status', models.CharField(default='OnCreate', max_length=20)),
                ('DateCreated', models.DateTimeField(default=datetime.datetime(2023, 10, 6, 9, 46, 24, 147847))),
                ('AddedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ModuleGroup',
            fields=[
                ('ModuleGroupId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.group')),
                ('Lecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.lecture')),
                ('Module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.module')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('ProgramId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('ProgramName', models.CharField(max_length=150)),
                ('ProgramCode', models.CharField(max_length=20)),
                ('numGroups', models.IntegerField(default=0)),
                ('numModules', models.IntegerField(default=1)),
                ('DateCreated', models.DateTimeField(default=datetime.datetime(2023, 10, 6, 9, 46, 24, 147847))),
                ('Status', models.CharField(default='Available', max_length=30)),
                ('AddedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudentId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('StudentNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('PhoneNumber', models.CharField(default='+27', max_length=15)),
                ('StudentIamge', models.FileField(blank=True, null=True, upload_to='streamApp/images')),
                ('TempLink', models.CharField(blank=True, max_length=500, null=True)),
                ('numModules', models.IntegerField(blank=True, null=True)),
                ('AttendanceRate', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Status', models.CharField(default='Oncreate', max_length=20)),
                ('Group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.group')),
                ('Program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.program')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimetableSlot',
            fields=[
                ('SlotId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('weekdayNum', models.IntegerField()),
                ('Time', models.TimeField()),
                ('weekday', models.TextField()),
                ('Venue', models.TextField()),
                ('Lecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.lecture')),
                ('ModuleGroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.modulegroup')),
            ],
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('StudentGroupId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('numClasses', models.IntegerField(blank=True, null=True)),
                ('numClassAttended', models.IntegerField(blank=True, null=True)),
                ('Group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.group')),
                ('Student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.student')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='Program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.program'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='Program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.program'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='Program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.program'),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('ClassId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.group')),
                ('TimetableSlot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.timetableslot')),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('AttendeeId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.class')),
                ('Student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.student')),
            ],
        ),
    ]