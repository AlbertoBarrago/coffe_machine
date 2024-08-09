from coffe import Coffe
from dict import conf

if __name__ == '__main__':
    ask_for_start_machine = input('☕️ Do you want to start the coffe machine? (Type -> start)')
    if ask_for_start_machine == 'start':
        coffe_machine = Coffe(conf, True)
        coffe_machine.start_machine()
    else:
        exit(code="Fuck you, bye the machine go off.")
