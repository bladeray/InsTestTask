import os

from back_tests.models import Pet, Category, Tag

ID_FIND_BY_ID = 123123123123123
ID_FIND_BY_STATUS = 123412341234123

PET_ONLY_ID = Pet(121212121212121)

PET_FULL = Pet(123451234512345, Category(10, 'cats'), 'Fill',
                ['https://www.firestock.ru/wp-content/uploads/2014/09/istock_cat2208748medium11-700x465.jpg'],
                [Tag(5, 'cute'), Tag(6, 'beautiful')], 'available')

PET_TOO_BIG_ID = Pet(12345678901234567890)

PET_TO_DELETE = Pet(123456123456123)

PET_UPDATED_FULL = Pet(123451234512345, Category(20, 'dogs'), 'Jack',
                ['https://images.pexels.com/photos/1805164/pexels-photo-1805164.jpeg?cs=srgb&dl=pexels-valeria-boltneva-1805164.jpg&fm=jpg',
                 'https://images.pexels.com/photos/1805165/pexels-photo-1805165.jpeg?cs=srgb&dl=pexels-valeria-boltneva-1805165.jpg&fm=jpg'],
                [Tag(7, 'strong'), Tag(8, 'peachy')], 'sold')

PET_UPDATED_ONLY_ID = Pet(123451234512345)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))