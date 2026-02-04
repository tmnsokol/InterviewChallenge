from status_codes import *
from taxes import calculate_tax
from discounts import apply_discount


def calculate_total(price, quantity, tax_rate, discount_percent):
    if quantity == 0:
        return STATUS_DIVISION_ERROR, None

    subtotal = price * quantity

    tax_status, tax_value = calculate_tax(subtotal, tax_rate)
    if tax_status != STATUS_OK:
        return tax_status, None

    total = subtotal + tax_value

    discount_status, discounted_total = apply_discount(total, discount_percent)
    if discount_status != STATUS_OK:
        return discount_status, total

    if total < 0:
        return STATUS_NEGATIVE_TOTAL, total

    return STATUS_OK, total

