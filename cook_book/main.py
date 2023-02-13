import os.path

#Task 1
def read_recipes(recipes_file_name: str) -> dict:
    with open(recipes_file_name, "rt") as file:
        recipes_list = {}
        while(True):
            dish_name = file.readline().strip()
            if not dish_name:
                break
    
            recipes_list[dish_name] = []
            ingredients_count = file.readline()

            for i in range(int(ingredients_count)):
                ingredients = file.readline().strip()
                ingredient_name, quantity, measure = ingredients.split(" | ")
                recipes_list[dish_name].append({'ingredient_name': ingredient_name,
                                                'quantity': int(quantity),
                                                'measure': measure})
            file.readline()
    return recipes_list

#Task 2
def get_shop_list_by_dishes(recipes_dict: dict, dishes: list, person_count: int) -> dict:
    shop_list = {}

    for dish in dishes:
        if dish in recipes_dict:
            for ingredient in recipes_dict[dish]:
                if ingredient["ingredient_name"] in shop_list:
                    shop_list[ingredient["ingredient_name"]]["quantity"] += person_count * ingredient["quantity"]
                else:
                    shop_list[ingredient["ingredient_name"]] = {"measure": ingredient["measure"],
                                                                "quantity": ingredient["quantity"] * person_count}
    return shop_list


def solution():
    file_name = "recipes.txt"
    
    recipes_dict = {} #Task 1
    if os.path.exists(file_name):
        recipes_dict = read_recipes(file_name)
        print("Книга рецептов:")
        print(recipes_dict)
    else:
        print("Файла рецепта с таким именем не существует!")

    dishes_list = ["Запеченный картофель", "Омлет"] #Task 2
    person_count = 3
    shop_list = get_shop_list_by_dishes(recipes_dict, dishes_list, person_count)
    print("\nСписок покупок:")
    print(shop_list)

solution()