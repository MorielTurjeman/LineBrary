# Generated by Django 3.0.3 on 2020-07-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0009_auto_20200715_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstationrelation',
            name='station',
            field=models.CharField(choices=[('Tel Aviv - Savidor Center', 'Tel Aviv - Savidor Center'), ('Tel Aviv - University', 'Tel Aviv - University'), ('Tel Aviv - Ha-Shalom', 'Tel Aviv - Ha-Shalom'), ('Tel Aviv - Ha-Hagana', 'Tel Aviv - Ha-Hagana'), ('Nahariya', 'Nahariya'), ('Akko', 'Akko'), ('Karmiel', 'Karmiel'), ('Ahihod', 'Ahihod'), ('Kiryat Motskin', 'Kiryat Motskin'), ('Kiryat Haim', 'Kiryat Haim'), ('Haifa - Hutsot HaMifrats', 'Haifa - Hutsot HaMifrats'), ('Haifa - Merkazit HaMifrats', 'Haifa - Merkazit HaMifrats'), ('Haifa - Merkaz Hashmuna', 'Haifa - Merkaz Hashmuna'), ('Haifa - Bat Galim', 'Haifa - Bat Galim'), ('Haifa - Hof Hakarmel', 'Haifa - Hof Hakarmel'), ('Beit Sheaan', 'Beit Sheaan'), ('Afula', 'Afula'), ('Migdal HaEmek', 'Migdal HaEmek'), ('Yofneaam', 'Yofneaam'), ('Atlit', 'Atlit'), ('Binayamina', 'Binayamina'), ('Keysaria - Pardes Hana', 'Keysaria - Pardes Hana'), ('Hedera West', 'Hedera West'), ('Netanya', 'Netanya'), ('Netanya - Sapir', 'Netanya - Sapir'), ('Beit Yehushua', 'Beit Yehushua'), ('Herzliya', 'Herzliya'), ('Petah Tikva - Kiryat Arye', 'Petah Tikva - Kiryat Arye'), ('Petah Tikva - Sgula', 'Petah Tikva - Sgula'), ('Rosh HaAin North', 'Rosh HaAin North'), ('Kfar Saba - Nordaoo', 'Kfar Saba - Nordaoo'), ('Hod HaSharon - Sokolov', 'Hod HaSharon - Sokolov'), ('Raanana South', 'Raanana South'), ('Airport Ben Gurion', 'Airport Ben Gurion'), ("Modi'in outskirts", "Modi'in outskirts"), ("Modi'in Center", "Modi'in Center"), ('Jerusalem - Yizhak Navon', 'Jerusalem - Yizhak Navon'), ('Kfar Habad', 'Kfar Habad'), ('Lud - Ganei Aviv', 'Lud - Ganei Aviv'), ('Lud/Ramla', 'Lud/Ramla'), ('Beit Shemesh', 'Beit Shemesh'), ('Jesrualem - Tanahi Zoo', 'Jesrualem - Tanahi Zoo'), ('Jerusalem - Malha', 'Jerusalem - Malha'), ('Mazkeret Batia', 'Mazkeret Batia'), ('Kiryat Malachi - Yoav', 'Kiryat Malachi - Yoav'), ('Kiryat Gat', 'Kiryat Gat'), ("Lehavim/Raha'at", "Lehavim/Raha'at"), ("Be'er Sheva North - University", "Be'er Sheva North - University"), ("Be'er Sheva Center", "Be'er Sheva Center"), ('Dimona', 'Dimona'), ('Ofakim', 'Ofakim'), ('Netivot', 'Netivot'), ('Sderot', 'Sderot'), ('Ashkelon', 'Ashkelon'), ('Asdod - Ad Halom', 'Asdod - Ad Halom'), ('Yavne - West', 'Yavne - West'), ('Yavne - East', 'Yavne - East'), ("Be'er Yakov", "Be'er Yakov"), ('Rishon Letsiyon - HaRishonim', 'Rishon Letsiyon - HaRishonim'), ('Rishon Letsiyon - Moshe Dayan', 'Rishon Letsiyon - Moshe Dayan'), ('Bat Yam - HaKomemiyut', 'Bat Yam - HaKomemiyut'), ('Bat Yam - Yoseftal', 'Bat Yam - Yoseftal'), ('Holon Junction', 'Holon Junction')], default='Tel Aviv - Savidor Center', max_length=100),
        ),
    ]
