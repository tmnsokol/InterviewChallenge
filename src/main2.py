STATUS_OK = 0
STATUS_INVALID_INPUT = 1
STATUS_DIVISION_ERROR = 2
STATUS_NEGATIVE_TOTAL = 3
STATUS_UNKNOWN_ERROR = 99

def validate_inputs(price, quantity, tax_rate, discount):
    if price == 0:
        return STATUS_INVALID_INPUT

    if quantity < 0:
        return STATUS_INVALID_INPUT

    if tax_rate < 0 or discount < 0:
        return STATUS_INVALID_INPUT

    return STATUS_OK

def process_invoice(price, quantity, tax_rate_percent, discount_percent):
    status = validate_inputs(price, quantity, tax_rate_percent, discount_percent)
    if status != STATUS_OK:
        return status, None

    return calculate_total(price, quantity, tax_rate_percent, discount_percent)

def apply_discount(amount, discount_percent):
    discounted_amount = amount - (amount * discount_percent / 100)

    if discounted_amount <= 0:
        return STATUS_NEGATIVE_TOTAL, discounted_amount

    return STATUS_OK, discounted_amount

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

def calculate_tax(amount, tax_rate):
    try:
        tax = amount * tax_rate / 100
        return STATUS_OK, tax
    except ZeroDivisionError:
        return STATUS_UNKNOWN_ERROR, None
    
if __name__ == "__main__":
    result = process_invoice(
        price=10,
        quantity=2,
        tax_rate_percent=5,
        discount_percent=20
    )

print("Result:", result)
