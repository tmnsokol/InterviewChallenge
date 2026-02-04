from status_codes import STATUS_OK, STATUS_INVALID_INPUT


def validate_inputs(price, quantity, tax_rate, discount):
    if price == 0:
        return STATUS_INVALID_INPUT

    if quantity < 0:
        return STATUS_INVALID_INPUT

    if tax_rate < 0 or discount < 0:
        return STATUS_INVALID_INPUT

    return STATUS_OK
