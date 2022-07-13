
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191206_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='dt_upload',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='photo',
            name='path_to_img',
            field=models.ImageField(upload_to='%Y/%m/%d/'),
        ),
    ]
