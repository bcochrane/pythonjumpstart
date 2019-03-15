def main():
    print_header()
    load_journal()
    run_event_loop()
    save_journal()


def print_header():
    print('-----------------')
    print('   JOURNAL APP')
    print('-----------------')


def run_event_loop():
    print('What would you like to do?')

    action = None
    journal_data = []

    while action != 'X':
        action = input('[A]dd, [L]ist, or E[x]it: ')
        action = action.upper().strip()
        if action == 'A':
            add_entry(journal_data)
        elif action == 'L':
            list_entries(journal_data)
        elif action != 'X':
            print(f"I don't understand '{action}'.")

    print("Done...goodbye!")


def add_entry(data):
    data.append(input('Type your entry and press <ENTER>: '))


def list_entries(data):
    if not data:
        print('There are no entries to list.')
    else:
        for index, entry in enumerate(reversed(data)):
            print(f'[{index+1}] {entry}')


def load_journal():
    print('... loading journal entries ...')
    print('... loading complete ...')


def save_journal():
    print('... saving journal entries ...')
    print('... saving complete ...')


if __name__ == '__main__':
    main()
