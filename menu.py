class Food:
    def __init__(self, id, name, prep_time, complexity, cooking_apparatus):
        self.id = id
        self.name = name
        self.prep_time = prep_time
        self.complexity = complexity
        self.cooking_apparatus = cooking_apparatus

## food items
food1 = Food(1, "Pasta", 20, 2, "oven")
food2 = Food(2, "Beef Steak", 32, 3, "oven")
food3 = Food(3, "Waffles", 8, 1, "stove")
food4 = Food(4, "Chicken Breast", 28, 2, "stove")
food5 = Food(5, "Cheeseburger", 12, 1, "oven")
food6 = Food(6, "Cheesecake", 18, 3, "stove")
food7 = Food(7, "Pizza", 18, 2, "oven")
food8 = Food(8, "Pasta", 20, 2, "oven")
food9 = Food(9, "Salad", 9, 1, None)
food10 = Food(10, "Pasta", 20, 2, "oven")

## menu
menu = [food1, food2, food3, food4, food5, food6, food7, food8, food9, food10]
