import My_orders
import My_clients
import My_discounts
import My_menu
import My_exeptions


if __name__ == '__main__':
    try:
        dish_1 = My_menu.Dish('Fish', 'Fried fish', 15)
        dish_2 = My_menu.Dish('Steak', 'Beef steal', 20)
        dish_3 = My_menu.Dish('Tom yam', 'Asian spicy soup', 17)
        dish_4 = My_menu.Dish('Borch', 'Ukrainian national soup', 25)
        dish_5 = My_menu.Dish('B-B-Q', 'B-B-Q souse', 3)
        dish_6 = My_menu.Dish('Bread', 'Just bread', 5)

        main_dishes = My_menu.MenuCategory('Main dishes', dish_1, dish_2)
        soups = My_menu.MenuCategory('Soups', dish_3, dish_4)
        other_dishes = My_menu.MenuCategory('Other', dish_5, dish_6)

        main_menu = My_menu.Menu('Our menu')
        main_menu.add_category(main_dishes)
        main_menu.add_category(soups)
        main_menu.add_category(other_dishes)

        test_order = My_orders.Order()
        test_order.add_to_order(dish_1, 2)
        test_order.add_to_order(dish_6, 1)
        test_order.add_to_order(dish_5, 2)

        test_client = My_clients.Client('Vova', test_order, My_discounts.gold_discount)
    except (TypeError, ValueError, My_exeptions.PriceError) as e:
        print('Error: ' + str(e))

    else:
        print(test_client.order)
        print(test_client.count_order())