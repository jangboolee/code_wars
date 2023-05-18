import re


def atm(value):

    # Prepare regex pattern to extract value and currency
    value_pattern = re.compile(r"\d+")
    currency_pattern = re.compile(r"[a-z]{3}", re.I)

    # Extract value and currency value
    value_match = value_pattern.search(value)
    currency_match = currency_pattern.search(value)

    # If both value and currencies have been found
    if all([value_match, currency_match]):

        # Extract the amount and currency from the match objects
        req_amount = int(value_match.group(0))
        req_currency = currency_match.group(0).upper()

        # If the requested currency does not exist in the ATM
        if req_currency not in [curr.upper() for curr in VALUES.keys()]:
            return f'Sorry, have no {req_currency}.'
        # If the requested currency exists
        else:
            # Get the relevant bank notes for the requested currency in ATM
            notes = VALUES[req_currency]
            # If the ATM can't give out the requested amount
            if req_amount % min(notes) != 0:
                return f"Can't do {req_amount} {req_currency}. " \
                       f"Value must be divisible by {min(notes)}!"
            # If the ATM can give out the requested amount
            else:
                # Create a dictionary of notes that can be issued by the ATM
                ATM_notes = {}
                # Sort the list of notes to start with the largest note
                sorted_notes = sorted(notes, reverse=True)
                # Loop through the sorted list of notes
                for note in sorted_notes:
                    # Compare the requested amount to the note
                    if req_amount >= note:
                        # Find how many notes can be issued
                        ATM_notes[note] = req_amount // note
                        # Subtract the issued amount from the requested amount
                        req_amount -= ATM_notes[note] * note
                # Give final message based on issued notes
                return ", ".join([f'{note_count} * {note_value} {req_currency}'
                                  for note_value, note_count
                                  in ATM_notes.items()])
