# Generated by Django 4.0.4 on 2022-05-18 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='proprietaire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='media',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.service'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='categorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.categorie'),
        ),
        migrations.AlterField(
            model_name='service',
            name='classe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.classement'),
        ),
        migrations.AlterField(
            model_name='service',
            name='contactrs',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.contactrs'),
        ),
        migrations.AlterField(
            model_name='service',
            name='type_de_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.typeservice'),
        ),
    ]
