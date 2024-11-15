
from pprint import pprint
import os


# Создаем путь до файла
path = os.path.join(os.path.dirname(__file__), 'recipes.txt')

# Открываем файл
with open(path, encoding='utf-8') as file:
    lines = file.readlines()
    
    cook_book = {}
    current_dish = None
    current_ingredients = []

    for line in lines:
        line = line.strip() 

        if not line: 
            if current_dish:
                cook_book[current_dish] = current_ingredients
                current_dish = None
                current_ingredients = []
            continue

        if current_dish is None:
             current_dish = line
        else:
            ingredient_parts = line.split('|')
            if len(ingredient_parts) == 3:
                ingredient_name = ingredient_parts[0].strip()
                quantity = int(ingredient_parts[1].strip())
                measure = ingredient_parts[2].strip()
                current_ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:  # Проверяем, есть ли блюдо в cook_book
            ingredients = cook_book[dish]  # Получаем список ингредиентов для блюда
            
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                
                if ingredient_name in shop_list:
                    # Если ингредиент уже есть в списке, добавляем к количеству
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    # Если ингредиента нет в списке, добавляем его
                    shop_list[ingredient_name] = {
                        'measure': ingredient['measure'],
                        'quantity': quantity
                    }

    return shop_list

# Пример использования
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)
pprint(shop_list)

