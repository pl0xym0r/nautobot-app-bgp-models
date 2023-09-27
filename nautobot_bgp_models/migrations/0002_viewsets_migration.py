# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring,invalid-name
# Generated by Django 3.2.18 on 2023-03-15 21:03

from django.db import migrations
import django.db.models.deletion
import nautobot.extras.models.statuses


class Migration(migrations.Migration):
    dependencies = [
        ("nautobot_bgp_models", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="peergroup",
            old_name="template",
            new_name="peergroup_template",
        ),
        migrations.AddField(
            model_name="bgproutinginstance",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_bgp_models_bgproutinginstance_related",
                to="extras.status",
            ),
        ),
    ]