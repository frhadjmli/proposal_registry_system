# Generated by Django 4.0 on 2022-02-07 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_dprtadmin_options_alter_hod_options'),
        ('document', '0002_remove_message_receiver_remove_proposal_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='status',
            field=models.CharField(choices=[('aadm', 'accepted by admin'), ('rsup', 'rejected by supervisor'), ('radm', 'rejected by admin'), ('ahod', 'accepted by HOD'), ('pen', 'pending'), ('asup', 'accepted by supervisor'), ('rhod', 'rejected by HOD')], default='pen', max_length=4),
        ),
        migrations.RemoveField(
            model_name='proposal',
            name='supervisor',
        ),
        migrations.AddField(
            model_name='proposal',
            name='supervisor',
            field=models.ManyToManyField(to='account.Supervisor'),
        ),
    ]
