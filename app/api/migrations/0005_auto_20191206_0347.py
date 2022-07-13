
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191206_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
