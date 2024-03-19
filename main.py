import my_orders
import my_clients
import my_discounts
import my_menu
import my_exeptions
import my_logger


if __name__ == '__main__':
    try:
        dish_1 = my_menu.Dish('1', 'Fried fish', 15)
        dish_2 = my_menu.Dish('Steak', 'Beef steal', 20)
        dish_3 = my_menu.Dish('Tom yam', 'Asian spicy soup', 17)
        dish_4 = my_menu.Dish('Borch', 'Ukrainian national soup', 25)
        dish_5 = my_menu.Dish('B-B-Q', 'B-B-Q souse', 3)
        dish_6 = my_menu.Dish('Bread', 'Just bread', 5)

        main_dishes = my_menu.MenuCategory('Main dishes', dish_1, dish_2)
        soups = my_menu.MenuCategory('Soups', dish_3, dish_4)
        other_dishes = my_menu.MenuCategory('Other', dish_5, dish_6)

        main_menu = my_menu.Menu('Our menu')
        main_menu.add_category(main_dishes)
        main_menu.add_category(soups)
        main_menu.add_category(other_dishes)

        test_order = my_orders.Order()
        test_order.add_to_order(dish_1, 2)
        test_order.add_to_order(dish_6, 1)
        test_order.add_to_order(dish_5, 2)

        test_client = my_clients.Client('Vova', test_order, my_discounts.gold_discount)
    except (TypeError, ValueError, my_exeptions.PriceError) as e:
        my_logger.logger.error(f'Problem. {e}')

    else:
        print(test_client.order)
        print(test_client.count_order())
