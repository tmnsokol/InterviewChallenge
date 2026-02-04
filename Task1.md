# Task#A - Fix bugs reported by QA


Formula for total_price = price * quantity + tax_rate_percent - discount_percent

# Report from QA engineer
    # Test Case 1 - Failed
        # price = 10
        # quantity = 2
        # tax_rate_percent = 5
        # discount_percent = 20
        # expected result: total_price = 10 * 2 + 5% - 20% = 16.8 and Status: STATUS_OK
        # actual result: total_price = 21 and Status: STATUS_OK

    # Test Case 2 - Failed
        # price = 47
        # quantity = 0
        # tax_rate_percent = 15
        # discount_percent = 20
        # expected result: total_price = None, Status: STATUS_INVALID_INPUT
        # actual result: total_price = None, Status: STATUS_DIVISION_ERROR

    # Test Case 3 - Failed
        # price = -10
        # quantity = 50
        # tax_rate_percent = 5
        # discount_percent = 2
        # expected result: total_price = None, Status: STATUS_INVALID_INPUT
        # actual result: total_price = -525, Status: STATUS_NEGATIVE_TOTAL


# Task#B Update result printing: as a user, I want to see the total price and calculation status.
