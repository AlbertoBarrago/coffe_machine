# Coffe class
from coffe_service import get_options, check_resources, calculate_change, prepare_product, ask_for_operation, askMoney, \
    save_coffee


class Coffe:
    """
    Coffe machine
    Need configuration for start_machine method

    Simple project for testing OOP approach made starting by procedural code
    """
    operation_count = 0

    def __init__(self, conf_option):
        self.conf = conf_option
        self.has_enough_ingredients = True

    def start_machine(self):
        while self.has_enough_ingredients:
            print("Services: \n")
            option = get_options(self)
            if check_resources(self, option):
                money_payed = askMoney()
                self.operation_count += 1
                calculate_change(self, money_payed, self.conf['cost'][option])
                prepare_product(self, option)
                save_coffee(option, money_payed, self.operation_count)
                ask_for_operation(self)
        else:
            exit(code="200: Bye, bye the machine go off.")
