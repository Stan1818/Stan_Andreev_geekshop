import json

from django.conf import settings
from django.core.management import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class Command(BaseCommand):

    def _load_data_from_file(self, file_name):
        with open(f'{settings.BASE_DIR}/mainapp/json/{file_name}.json', encoding='utf-8') as json_file:
            return json.load(json_file)

    def handle(self, *args, **options):
        ProductCategory.objects.all().delete()

        categories_list = self._load_data_from_file('categories')

        categories_batch = []
        for cat in categories_list:
             categories_batch.append(
                 ProductCategory(
                     name=cat.get('name'),
                     description=cat.get('description')
                 )
             )

        ProductCategory.objects.bulk_create(categories_batch)

        Product.objects.all().delete()

        products_list = self._load_data_from_file('products')

        for prod in products_list:
            _cat = ProductCategory.objects.get(name=prod.get('category'))
            prod['category'] = _cat

            Product.objects.create(**prod)


        shop_user = ShopUser.objects.create_superuser(username='django',email='stan@mail.ru', age=35)
        shop_user.set_password('geekbrains')
        shop_user.save()