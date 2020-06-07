# Generated by Django 3.0.5 on 2020-06-06 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courier_branch', '0005_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particular', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account', models.CharField(choices=[('Expenses', 'Expenses'), ('Income', 'Income')], max_length=9)),
                ('Balance', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Branch', models.ForeignKey(default=None, editable=False, on_delete=django.db.models.deletion.CASCADE, to='courier_branch.Branch')),
            ],
        ),
    ]
