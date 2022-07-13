
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dt_upload', models.DateField(auto_now_add=True)),
                ('place', models.CharField(max_length=200)),
                ('path_to_img', models.CharField(max_length=200)),
                ('size', models.IntegerField(default=0)),
            ],
        ),
    ]
