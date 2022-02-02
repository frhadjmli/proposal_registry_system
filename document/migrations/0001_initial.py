# Generated by Django 4.0 on 2022-01-29 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('text', models.TextField(help_text='پیام خود را وارد کنید.', null=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.student')),
                ('sender', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='account.supervisor')),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=3)),
                ('academic_year', models.CharField(max_length=4)),
                ('summary', models.TextField(help_text='مختصر اطلاعاتی درباره پروپزال')),
                ('status', models.CharField(choices=[('rsup', 'rejected by supervisor'), ('ahod', 'accepted by HOD'), ('radm', 'rejected by admin'), ('asup', 'accepted by supervisor'), ('pen', 'pending'), ('rhod', 'rejected by HOD'), ('aadm', 'accepted by admin')], default='pen', max_length=4)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='document.message')),
                ('student', models.ManyToManyField(to='account.Student')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.supervisor')),
            ],
        ),
    ]