def add_contact(args, contacts: dict):
    set_contact_phone(args, contacts)

    return "Contact has been added.", False


def exit(args, contacts: dict):
    return "Good bye!", True


def hello(args, contacts: dict):
    return "How can I help you?", False


def set_contact_phone(args, contacts: dict):
    name, phone = args
    contacts[name] = phone

    return "Contacts' phone has been changed.", False


def get_contact_phone(args, contacts: dict):
    name = args[0]

    if name not in contacts:
        return "Contact not found", False

    return contacts[name], False


def get_contacts_list(args, contacts: dict):
    output = ""

    for contact, phone in contacts.items():
        output += f"{contact} - {phone}\n"

    return output, False


def render_help(commands: dict):
    output = "list of allowed commands: ["

    for command in commands:
        output += f"{command},"

    output = output.strip(',')

    return output + "]"
