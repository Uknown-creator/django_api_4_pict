
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191206_0316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='path_to_img',
            new_name='img',
        ),
    ]
