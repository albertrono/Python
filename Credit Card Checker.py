card_no = input("Enter the credit card number: ")

def authentication():
    print(f"Card Number: {card_no}")
    sum_even = 0
    sum_odd = 0

    # Reverse the card number for Luhn's Algorithm
    reversed_card = card_no[::-1]
    print(f"The reversed card number is: {reversed_card}")

    for index, digit in enumerate(reversed_card):
        digit = int(digit)  # Convert to integer

        if index % 2 == 0:  # Odd placed (since reversed)
            sum_odd += digit
        else:  # Even placed
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            sum_even += doubled

    total_sum = sum_even + sum_odd
    print(f"Sum of digits: {total_sum}")
    print(f"The sum of the odd placed numbers: {sum_odd}")
    print(f"The sum of the doubled placed numbers: {sum_even}")

    if total_sum % 10 == 0:
        card_issuer()
    else:
        print("Invalid Credit Card")

def card_issuer():
    first_two = int(card_no[:2])
    first_four = int(card_no[:4]) if len(card_no) >= 4 else 0
    first_six = int(card_no[:6]) if len(card_no) >= 6 else 0

    if card_no.startswith("4") and len(card_no) in [16, 19]:
        issuer = "Visa"
    elif first_two in [34, 37] and len(card_no) == 15:
        issuer = "American Express"
    elif 51 <= first_two <= 55 or (2221 <= first_four <= 2720 and len(card_no) in [16, 19]):
        issuer = "MasterCard"
    elif first_four == 6011 or (622126 <= first_six <= 622925) or (644 <= first_two <= 649) or card_no.startswith("65"):
        issuer = "Discover"
    elif first_two in [36, 38] or (300 <= first_three <= 305 and len(card_no) == 14):
        issuer = "Diners Club"
    elif 3528 <= first_four <= 3589 and len(card_no) in [16, 17, 18, 19]:
        issuer = "JCB"
    else:
        issuer = "Unknown"

    print(f"Valid: {issuer} Credit Card")

authentication()