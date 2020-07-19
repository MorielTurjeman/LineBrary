# Generated by Django 3.0.4 on 2020-07-19 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0015_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='station',
            field=models.CharField(choices=[('Tel Aviv - Savidor Center', 'Tel Aviv - Savidor Center'), ('Tel Aviv - University', 'Tel Aviv - University'), ('Tel Aviv - Ha-Shalom', 'Tel Aviv - Ha-Shalom'), ('Tel Aviv - Ha-Hagana', 'Tel Aviv - Ha-Hagana'), ('Haifa - Bat Galim', 'Haifa - Bat Galim'), ('Haifa - Hof Hakarmel', 'Haifa - Hof Hakarmel'), ('Beit Yehushua', 'Beit Yehushua'), ('Herzliya', 'Herzliya'), ('Petah Tikva - Kiryat Arye', 'Petah Tikva - Kiryat Arye'), ('Kfar Saba - Nordaoo', 'Kfar Saba - Nordaoo')], default='Tel Aviv - Savidor Center', max_length=100),
        ),
        migrations.AlterField(
            model_name='bookstationrelation',
            name='station',
            field=models.CharField(choices=[('Tel Aviv - Savidor Center', 'Tel Aviv - Savidor Center'), ('Tel Aviv - University', 'Tel Aviv - University'), ('Tel Aviv - Ha-Shalom', 'Tel Aviv - Ha-Shalom'), ('Tel Aviv - Ha-Hagana', 'Tel Aviv - Ha-Hagana'), ('Haifa - Bat Galim', 'Haifa - Bat Galim'), ('Haifa - Hof Hakarmel', 'Haifa - Hof Hakarmel'), ('Beit Yehushua', 'Beit Yehushua'), ('Herzliya', 'Herzliya'), ('Petah Tikva - Kiryat Arye', 'Petah Tikva - Kiryat Arye'), ('Kfar Saba - Nordaoo', 'Kfar Saba - Nordaoo')], default='Tel Aviv - Savidor Center', max_length=100),
        ),
    ]