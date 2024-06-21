# Generated by Django 5.0.1 on 2024-04-20 03:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="brand",
            fields=[
                (
                    "brand_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "brand_name",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                ("brand_is_active", models.CharField(default=True, max_length=100)),
                ("brand_created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "Brand_information_tb",
            },
        ),
        migrations.CreateModel(
            name="item_category",
            fields=[
                (
                    "item_category_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "item_category_name",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                (
                    "item_category_is_active",
                    models.CharField(default=True, max_length=100),
                ),
                ("item_category_created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "Item_Category_information_tb",
            },
        ),
        migrations.CreateModel(
            name="main_category",
            fields=[
                (
                    "main_category_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "main_category_name",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                (
                    "main_category_is_active",
                    models.CharField(default=True, max_length=100),
                ),
                ("main_category_created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "Main_Category_information_tb",
            },
        ),
        migrations.CreateModel(
            name="product",
            fields=[
                (
                    "product_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "product_name",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                (
                    "product_description",
                    models.CharField(
                        blank=True, default=None, max_length=10000, null=True
                    ),
                ),
                (
                    "product_price",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                (
                    "product_stock",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                (
                    "product_discount",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                ("product_is_active", models.CharField(default=True, max_length=100)),
                ("product_created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "product_is_featured",
                    models.CharField(default=False, max_length=100),
                ),
            ],
            options={
                "db_table": "Product_information_tb",
            },
        ),
        migrations.CreateModel(
            name="brand_item",
            fields=[
                (
                    "brand_item_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "brand_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="products.brand"
                    ),
                ),
                (
                    "item_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.item_category",
                    ),
                ),
            ],
            options={
                "db_table": "brand_item_information_tb",
            },
        ),
        migrations.CreateModel(
            name="main_brand",
            fields=[
                (
                    "main_brand_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "brand_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="products.brand"
                    ),
                ),
                (
                    "main_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.main_category",
                    ),
                ),
            ],
            options={
                "db_table": "main_brand_information_tb",
            },
        ),
        migrations.CreateModel(
            name="main_item",
            fields=[
                (
                    "main_item_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "item_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.item_category",
                    ),
                ),
                (
                    "main_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.main_category",
                    ),
                ),
            ],
            options={
                "db_table": "main_item_information_tb",
            },
        ),
        migrations.CreateModel(
            name="product_brand",
            fields=[
                (
                    "product_brand_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "brand_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="products.brand"
                    ),
                ),
                (
                    "product_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "db_table": "product_brand_information_tb",
            },
        ),
        migrations.CreateModel(
            name="product_brand_item",
            fields=[
                (
                    "product_brand_item_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "brand_item_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.brand_item",
                    ),
                ),
                (
                    "product_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "db_table": "product_brand_item_information_tb",
            },
        ),
        migrations.CreateModel(
            name="product_color",
            fields=[
                (
                    "product_color_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "color_stock",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                (
                    "color_name",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                (
                    "product_color_is_active",
                    models.CharField(default=True, max_length=100),
                ),
                ("product_color_created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "product_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "db_table": "product_color_information_tb",
            },
        ),
        migrations.CreateModel(
            name="product_image",
            fields=[
                (
                    "product_image_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                ("image_path", models.CharField(default=True, max_length=100)),
                (
                    "product_image_is_active",
                    models.CharField(default=True, max_length=100),
                ),
                ("product_image_created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "product_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "db_table": "product_image_information_tb",
            },
        ),
        migrations.CreateModel(
            name="product_item",
            fields=[
                (
                    "product_item_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "item_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.item_category",
                    ),
                ),
                (
                    "product_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "db_table": "product_item_information_tb",
            },
        ),
        migrations.CreateModel(
            name="product_main",
            fields=[
                (
                    "product_main_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "main_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.main_category",
                    ),
                ),
                (
                    "product_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "db_table": "product_main_information_tb",
            },
        ),
        migrations.CreateModel(
            name="product_main_brand",
            fields=[
                (
                    "product_main_brand_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "main_brand_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.main_brand",
                    ),
                ),
                (
                    "product_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "db_table": "product_main_brand_information_tb",
            },
        ),
        migrations.CreateModel(
            name="product_main_item",
            fields=[
                (
                    "product_main_item_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "main_item_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.main_item",
                    ),
                ),
                (
                    "product_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "db_table": "product_main_item_information_tb",
            },
        ),
        migrations.CreateModel(
            name="product_size",
            fields=[
                (
                    "product_size_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "size_value",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                (
                    "product_size_is_active",
                    models.CharField(default=True, max_length=100),
                ),
                ("product_size_created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "product_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "db_table": "product_size_information_tb",
            },
        ),
        migrations.CreateModel(
            name="product_price",
            fields=[
                (
                    "product_price_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "product_price",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                (
                    "extra_charges",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                (
                    "final_charges",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                (
                    "product_price_is_active",
                    models.CharField(default=True, max_length=100),
                ),
                ("product_price_created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "color_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product_color",
                    ),
                ),
                (
                    "product_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_prices",
                        to="products.product",
                    ),
                ),
                (
                    "size_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product_size",
                    ),
                ),
            ],
            options={
                "db_table": "product_price_information_tb",
            },
        ),
        migrations.CreateModel(
            name="product_size_color",
            fields=[
                (
                    "product_size_color_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "color_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product_color",
                    ),
                ),
                (
                    "product_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
                (
                    "size_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product_size",
                    ),
                ),
            ],
            options={
                "db_table": "product_size_color_information_tb",
            },
        ),
        migrations.CreateModel(
            name="wishlist_items",
            fields=[
                (
                    "wishlist_item_id",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                (
                    "product_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
                (
                    "product_image_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product_image",
                    ),
                ),
                (
                    "product_price_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product_price",
                    ),
                ),
                (
                    "user_fk",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.users",
                    ),
                ),
            ],
            options={
                "db_table": "wishlist_items_information_tb",
            },
        ),
    ]