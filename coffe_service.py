from time import sleep
from prettytable import PrettyTable


def get_options(self):
    """
    Get the options for the coffee machine.
    :return:
    """
    table = PrettyTable()
    table.field_names = ["Option", "Description"]

    for option in self.conf['type']:
        table.add_row([option, self.conf['type'][option]])

    print(table)
    return input('\nWhat do you want to do?')


def check_resources(self, type_selected):
    """
    Check if there are enough resources to make the coffe or whatever the user wants and machine does.
    :param self:
    :param type_selected:
    :return:
    """
    for resource in self.conf['resources']:
        if self.conf['resources'][resource] < self.conf['ingredients'][type_selected][resource]:
            print(f'Sorry, we don\'t have enough {resource}.')
            exit("🤡Machine is out of resources. Call the admin!")
    return True


def askMoney():
    """
    Ask for money.
    :return:
    """
    print('How much money do you want to pay, write a float number in dollar?')
    # add money to total
    return float(input())


def calculate_change(self, money_paid, cost):
    """
    Calculate the change.
    :param self:
    :param cost:
    :param money_paid:
    """
    change = money_paid - cost
    self.conf['money']['total'] += cost
    print(f'\nHere is your change: {change}')


def prepare(self, type_selected):
    """
    Prepare the product for the user and subtract ingredients from the machine.
    :param self:
    :param type_selected:
    :return:
    """
    for resource in self.conf['ingredients'][type_selected]:
        self.conf['resources'][resource] -= self.conf['ingredients'][type_selected][resource]

    print(f'\nLet\'s prepare your {type_selected}...')
    sleep(2)
    print(f'{type_selected} is ready pay attention is really hot!')
    print(f'\n🚀 Operation completed.\n Ready for next Customer')


def print_options(self):
    """
    Print the options
    :return:
    """
    print("\n")
    for option in self.conf['type']:
        print(self.conf['type'][option])


def report(self):
    total_money = self.conf['money']
    print("\n")
    for resource in self.conf['resources']:
        if (resource == 'coffee_beans' or resource == 'coffee_grounds' or resource == 'tea_leaves'
                or resource == 'dark_chocolate'):
            print(f"{resource.title()}: {self.conf['resources'][resource]}g")
        else:
            print(f"{resource.title()}: {self.conf['resources'][resource]}ml")
    print(f"Money: ${total_money['total']}")


def start_coffe_machine(self):
    has_enough_ingredients = True

    while has_enough_ingredients:
        print("Here the options of machine: \n")
        option = get_options(self)
        if check_resources(self, option):
            money_payed = askMoney()
            calculate_change(self, money_payed, self.conf['cost'][option])
            prepare(self, option)
            ask_for_operation(self)
    else:
        exit(code="200: Bye, bye the machine go off.")


def ask_for_operation(self):
    """
    Ask for next operation
    :return:
    """
    operation_go_next = False
    while not operation_go_next:
        get_request = input(f'\nWhat do you want to do?\n report\n options\n go\n')
        if get_request == 'report':
            report(self)
        elif get_request == 'options':
            print_options(self)
        elif get_request == 'go':
            operation_go_next = True
            start_coffe_machine(self)
        elif get_request == 'off':
            exit("Turn off machine")
        else:
            exit("Wrong input")
