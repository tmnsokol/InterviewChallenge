from calculator import calculate_total
from validator import validate_inputs
from status_codes import *

def process_invoice(price, quantity, tax_rate_percent, discount_percent):
    status = validate_inputs(price, quantity, tax_rate_percent, discount_percent)
    if status != STATUS_OK:
        return status, None

    return calculate_total(price, quantity, tax_rate_percent, discount_percent)

if __name__ == "__main__":
    result = process_invoice(
        price=10,
        quantity=2,
        tax_rate_percent=5,
        discount_percent=20
    )

print("Result:", result)
