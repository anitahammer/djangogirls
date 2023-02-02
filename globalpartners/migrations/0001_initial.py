# Generated by Django 3.2.16 on 2023-02-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GlobalPartner",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("company_name", models.CharField(max_length=100)),
                ("contact_person", models.CharField(max_length=100)),
                ("contact_email", models.EmailField(max_length=100)),
                ("prospective_sponsor", models.BooleanField(default=False)),
                ("patreon_sponsor", models.BooleanField(default=False)),
                (
                    "patreon_level_per_month",
                    models.IntegerField(
                        blank=True,
                        choices=[(100, "$100/month"), (250, "$250/month"), (500, "$500/month"), (1000, "$1,000/month")],
                        null=True,
                    ),
                ),
                (
                    "sponsor_level_annual",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (500, 500),
                            (1000, "Silver ($1000)"),
                            (2500, "Gold ($2,500)"),
                            (5000, "Platinum ($5,000)"),
                            (10000, "Diamond ($10,000)"),
                        ],
                        null=True,
                    ),
                ),
                ("date_joined", models.DateField(blank=True, null=True)),
                ("contacted", models.BooleanField(default=False)),
                ("date_contacted", models.DateField(blank=True, null=True)),
                ("next_renewal_date", models.DateField(blank=True, null=True)),
                ("logo", models.ImageField(blank=True, null=True, upload_to="uploads")),
                ("is_displayed", models.BooleanField(default=False)),
                ("website_url", models.URLField(blank=True, null=True)),
                ("style", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
