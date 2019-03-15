# TODO: add docstrings!

import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------')
    print('   JOURNAL APP')
    print('-----------------')


def run_event_loop():
    print('What would you like to do?')

    action = None
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while action != 'X':
        action = input('[A]dd, [L]ist, or E[x]it: ')
        action = action.upper().strip()
        if action == 'A':
            add_entry(journal_data)
        elif action == 'L':
            list_entries(journal_data)
        elif action and action != 'X':
            print(f"I don't understand '{action}'.")

    journal.save(journal_name, journal_data)
    print("Done...goodbye!")


def add_entry(data):
    text = input('Type your entry and press <ENTER>: ')
    journal.add_entry(text, data)


def list_entries(data):
    if not data:
        print('There are no entries to list.')
    else:
        for index, entry in enumerate(reversed(data)):
            print(entry)


if __name__ == '__main__':
    main()
