#!/usr/bin/env python3
def compute_tax(gross_income, num_dependents):
    """
    Compute federal and state income tax for a person.

    :param gross_income: The gross income of the person.
    :param num_dependents: The number of dependents claimed.
    :return: Tuple containing (federal_income_tax, state_income_tax)

    >>> compute_tax(50000, 2)
    (7600.0, 2277.5)

    >>> compute_tax(75000, 3)
    (13000.0, 3412.5)
    """

    FEDERAL_TAX_RATE = 0.20
    STATE_TAX_RATE = 0.0455
    STANDARD_DEDUCTION = 10000.0
    DEPENDENT_DEDUCTION = 3000.0

    taxable_income = round(gross_income - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * num_dependents, 2)
    federal_income_tax = round(taxable_income * FEDERAL_TAX_RATE, 2)
    state_income_tax = round(taxable_income * STATE_TAX_RATE, 2)

    return federal_income_tax, state_income_tax


if __name__ == "__main__":
    import doctest
    doctest.testmod()
