# Generated by Django 3.1.5 on 2021-08-05 17:43

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('school_type', models.CharField(max_length=250)),
                ('logo', models.ImageField(default='media/school_logos', upload_to='')),
                ('primary_color', models.CharField(default='#005522', max_length=250)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.form')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('student_image', models.ImageField(blank=True, upload_to='media/student_images')),
                ('admission_number', models.IntegerField()),
                ('guardian', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.guardian')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
        ),
        migrations.CreateModel(
            name='TermYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.term')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('phone_number', models.CharField(max_length=250)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('subject_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.subjectgroup')),
            ],
        ),
        migrations.CreateModel(
            name='StudentTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
                ('term_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.termyear')),
            ],
        ),
        migrations.CreateModel(
            name='StudentStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.stream')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentFormSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.form')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.subject')),
            ],
        ),
        migrations.CreateModel(
            name='StudentForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_current', models.BooleanField(default=False)),
                ('year', models.CharField(max_length=250)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.form')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=65)),
                ('date_paid', models.DateField(null=True)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.form')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
                ('term_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.termyear')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolAdmin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('phone_number', models.CharField(max_length=250)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FormYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(auto_now_add=True)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.form')),
            ],
        ),
        migrations.CreateModel(
            name='FormSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.form')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.subject')),
            ],
        ),
        migrations.AddField(
            model_name='form',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school'),
        ),
        migrations.CreateModel(
            name='FeeBreakDown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('term_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.termyear')),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.DecimalField(decimal_places=2, max_digits=65)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.form')),
                ('term_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.termyear')),
            ],
        ),
        migrations.CreateModel(
            name='ExamStudentSubjectScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=65)),
                ('grade', models.CharField(max_length=2)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.subject')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.form'),
        ),
        migrations.AddField(
            model_name='exam',
            name='term_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.termyear'),
        ),
    ]
