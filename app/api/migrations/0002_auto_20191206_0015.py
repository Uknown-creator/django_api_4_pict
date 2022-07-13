
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='path_to_img',
            field=models.FileField(upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
