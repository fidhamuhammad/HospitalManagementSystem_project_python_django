# Generated by Django 4.2 on 2023-04-09 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(max_length=50)),
                ('admin_password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'admin_tb',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=2000)),
                ('pic', models.ImageField(upload_to='department/')),
            ],
            options={
                'db_table': 'dept_tb',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('pic', models.ImageField(upload_to='staff/')),
                ('status', models.CharField(default='active', max_length=20)),
            ],
            options={
                'db_table': 'staff_tb',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('doctor_email', models.CharField(max_length=50)),
                ('doctor_contact', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=50)),
                ('fee', models.CharField(max_length=50)),
                ('pic', models.ImageField(upload_to='doctor/')),
                ('username', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('status', models.CharField(default='active', max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_admin.department')),
            ],
            options={
                'db_table': 'doctr_tb',
            },
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('status', models.CharField(default='available', max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_admin.doctor')),
            ],
            options={
                'db_table': 'consult_tb',
            },
        ),
    ]
