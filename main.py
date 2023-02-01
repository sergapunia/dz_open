with open(r'2.4.files\recipes.txt','rt', encoding='utf-8') as f:
    recipe_book = {}
    for line in f:
        dish = line.strip()
        ingredients_count=int(f.readline().strip())
        ingredients = []
        for i in range(ingredients_count):
            ing = f.readline().strip()
            ingridient_name, quantity, measure =ing.split(' | ')
            ingredients.append({
                'ingridient_name': ingridient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        recipe_book[dish]=ingredients
print(recipe_book)
