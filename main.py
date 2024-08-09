# This is a sample coffe script
from time import sleep

from dict import conf


def get_options():
    """
    Get the options for the coffe machine.
    :return:
    """
    for option in conf['type']:
        print(conf['type'][option])
    return input('\nWhat do you want to do?')


def check_resources(type_selected):
    """
    Check if there are enough resources to make the coffe or whatever the user wants and machine does.
    :param type_selected:
    :return:
    """
    for resource in conf['resources']:
        if conf['resources'][resource] < conf['ingredients'][type_selected][resource]:
            print(f'Sorry, we don\'t have enough {resource}.')
            exit("🤡Machine is out of resources. Call the admin!")
    return True


def print_options():
    """
    Print the options
    :return:
    """
    print("\n")
    for option in conf['type']:
        print(conf['type'][option])


def askMoney():
    """
    Ask for money.
    :return:
    """
    print('How much money do you want to pay, write a float number in dollar?')
    # add money to total
    return float(input())


def calculate_change(money_paid, cost):
    """
    Calculate the change.
    :param cost:
    :param money_paid:
    """
    change = money_paid - cost
    conf['money']['total'] += cost
    print(f'\nHere is your change: {change}')


def prepare(type_selected):
    """
    Prepare the product for the user and subtract ingredients from the machine.
    :param type_selected:
    :return:
    """
    for resource in conf['ingredients'][type_selected]:
        conf['resources'][resource] -= conf['ingredients'][type_selected][resource]

    print(f'\nLet\'s prepare your {type_selected}...')
    sleep(2)
    print(f'{type_selected} is ready pay attention is really hot!')
    print(f'\n🚀 Operation completed.\n Ready for next Customer')


def report():
    total_money = conf['money']
    print("\n")
    for resource in conf['resources']:
        if (resource == 'coffee_beans' or resource == 'coffee_grounds' or resource == 'tea_leaves'
                or resource == 'dark_chocolate'):
            print(f"{resource.title()}: {conf['resources'][resource]}g")
        else:
            print(f"{resource.title()}: {conf['resources'][resource]}ml")
    print(f"Money: ${total_money['total']}")


def ask_if_exit():
    return input('Do you wanna exit or continue (y/n)?')


def ask_for_operation():
    """
    Ask for next operation
    :return:
    """
    operation_go_next = False
    while not operation_go_next:
        get_request = input(f'\nWhat do you want to do?\n report\n options\n go\n')
        if get_request == 'report':
            report()
        elif get_request == 'options':
            print_options()
        elif get_request == 'go':
            operation_go_next = True
            start_coffe_machine()
        elif get_request == 'off':
            exit("Turn off machine")
        else:
            exit("Wrong input")


def start_coffe_machine():
    has_enough_ingredients = True

    while has_enough_ingredients:
        print("Here the options of machine: \n")
        option = get_options()
        if check_resources(option):
            money_payed = askMoney()
            calculate_change(money_payed, conf['cost'][option])
            prepare(option)
            ask_for_operation()
    else:
        exit(code="200: Bye, bye the machine go off.")


if __name__ == '__main__':
    ask_for_start_machine = input(
        '☕️Do you want to start the coffe machine? (Type -> start)\n🖕🏻Turn off Machine '
        '(Type -> stop)\n')
    if ask_for_start_machine == 'start':
        ask_for_operation()
    else:
        exit(code="Fuck you, bye the machine go off.")
