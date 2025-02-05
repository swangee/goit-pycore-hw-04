import handlers


def parse_input(user_input):
    """
    Parse the input from the user. If there is no input - set default command to "help"
    :param user_input:
    :return:
    """
    if user_input == "":
        return "help", []

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print("Welcome to the assistant bot!")

    # Each handler must accept two arguments: args and contacts dictionary and return tuple with the output
    # and the termination flag if program should exit
    command_to_handler = {
        "close": handlers.exit,
        "exit": handlers.exit,
        "hello": handlers.hello,
        "add": handlers.add_contact,
        "change": handlers.set_contact_phone,
        "phone": handlers.get_contact_phone,
        "all": handlers.get_contacts_list,
    }

    contacts = {}

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "help":
            print(handlers.render_help(command_to_handler))
            continue

        if command not in command_to_handler:
            print("Invalid command!")
            continue

        output, should_terminate = command_to_handler[command](args, contacts)
        print(output)

        if should_terminate:
            break


if __name__ == "__main__":
    main()
