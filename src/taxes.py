from status_codes import STATUS_OK, STATUS_UNKNOWN_ERROR


def calculate_tax(amount, tax_rate):
    try:
        tax = amount * tax_rate / 100
        return STATUS_OK, tax
    except ZeroDivisionError:
        return STATUS_UNKNOWN_ERROR, None
