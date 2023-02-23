# Generated by Django 4.1.5 on 2023-02-23 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('allergies_id', models.AutoField(primary_key=True, serialize=False)),
                ('allergies_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('table_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('persons', models.IntegerField()),
                ('need_help', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('dish_id', models.AutoField(primary_key=True, serialize=False)),
                ('dish_name', models.CharField(max_length=75)),
                ('dish_quantity', models.IntegerField()),
                ('dish_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('dish_calories', models.IntegerField()),
                ('dish_availability', models.BooleanField(default=False)),
                ('category_id', models.ManyToManyField(to='restaurant.category')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(choices=[('Order in progress', 'Inprogress'), ('Received', 'Received'), ('Cooking', 'Cooking'), ('Ready to serve', 'Ready'), ('Delivered', 'Delivered'), ('Problem', 'Problem'), ('Cancelled', 'Cancelled')], default='Order in progress', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_time', models.DateTimeField()),
                ('order_finish', models.BooleanField(default=False)),
                ('dish_id', models.ManyToManyField(to='restaurant.dish')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.status')),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ingredient_id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient_name', models.CharField(max_length=20)),
                ('allergies_id', models.ManyToManyField(to='restaurant.allergies')),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='ingredient_id',
            field=models.ManyToManyField(to='restaurant.ingredient'),
        ),
    ]
