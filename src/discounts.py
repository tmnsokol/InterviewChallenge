from status_codes import STATUS_OK, STATUS_NEGATIVE_TOTAL


def apply_discount(amount, discount_percent):
    discounted_amount = amount - (amount * discount_percent / 100)

    if discounted_amount <= 0:
        return STATUS_NEGATIVE_TOTAL, discounted_amount

    return STATUS_OK, discounted_amount
