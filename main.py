# This is a sample coffe script
from dict import conf


def get_options():
    """
    Get the options for the coffe machine.
    :return:
    """
    for option in conf['type']:
        print(conf['type'][option])
    return input('Choose an option: ')


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
    for option in conf['type']:
        print(conf['type'][option])


def askMoney():
    """
    Ask for money.
    :return:
    """
    print('How much money do you want to pay, write a float number in dollar?')
    return float(input())


def calculate_change(money_paid, cost):
    """
    Calculate the change.
    :param cost:
    :param money_paid:
    """
    change = money_paid - cost
    print(f'\nHere is your change: {change}')


def prepare_machine(type_selected):
    """
    Prepare the product for the user and subtract ingredients from the machine.
    :param type_selected:
    :return:
    """
    for resource in conf['ingredients'][type_selected]:
        conf['resources'][resource] -= conf['ingredients'][type_selected][resource]
    print(f'\nLet\'s prepare your {type_selected}.')


def report():
    for resource in conf['resources']:
        print(f"\n{resource}: {conf['resources'][resource]}")


def ask_if_exit():
    return input('Do you wanna exit or continue (y/n)?')


def start_coffe_machine(name):
    has_enough_ingredients = True
    exit_from_process = False
    while not exit_from_process:
        get_request = input(f'\nWhat do you want to do?\n report\n options\n proceed\n')
        if get_request == 'report':
            report()
        elif get_request == 'options':
            print_options()
        elif get_request == 'proceed':
            exit_from_process = True

    while has_enough_ingredients:
        option = get_options()
        if check_resources(option):
            money_payed = askMoney()
            calculate_change(money_payed, conf['cost'][option])
            prepare_machine(option)
    else:
        exit(code="200: Bye, bye the machine go off.")


if __name__ == '__main__':
    ask_for_start_machine = input(
        '☕️Do you want to start the coffe machine? (Type -> start)\n🖕🏻Turn off Machine '
        '(Type -> stop)\n')
    if ask_for_start_machine == 'start':
        start_coffe_machine(name='alBz')
    else:
        exit(code="Fuck you, bye the machine go off.")
