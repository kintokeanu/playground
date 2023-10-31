#!/usr/bin/env python3
"""
Program: taxform.py
Author: Diego Alvarez
Compute a persons federal and state income tax for Colorad(state tax rate is 4.55%).
1. Significant constants
federalTax rate
stateTax rate
standard deduction
deduction per dependent
2. The inputs are
gross income
number of dependents
3. Computations:
taxable income = gross income - the standard deduction - adeduction for each dependent
Federal income tax = is a fixed percentage of the taxable income
State income tax = is a fixed percentage of the taxable income
4. The outputs are
the federal income tax
the state income tax
"""

# Significant constants
FEDERAL_TAX_RATE = 0.20
STATE_TAX_RATE = 0.0455
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

def calculate_taxes(gross_income, num_dependents):
    """
    Calculate federal and state income taxes.

    Args:
    - gross_income (float): Gross income.
    - num_dependents (int): Number of dependents.

    Returns:
    - Tuple: (federal_income_tax, state_income_tax)
    
    Examples:
    >>> calculate_taxes(50000, 2)
    (6800.0, 1547.0)

    >>> calculate_taxes(75000, 3)
    (11200.0, 2548.0)
    
    """
    # Calculate deductions for standard and dependents
    total_deductions = STANDARD_DEDUCTION + (DEPENDENT_DEDUCTION * num_dependents)

    # Calculate taxable income after deductions
    taxable_income = max(gross_income - total_deductions, 0)

    # Calculate federal and state income taxes
    federal_income_tax = round(taxable_income * FEDERAL_TAX_RATE, 2)
    state_income_tax = round(taxable_income * STATE_TAX_RATE, 2)

    return federal_income_tax, state_income_tax

if __name__ == "__main__":
    # Run the embedded doctests
    import doctest
    doctest.testmod()

    # Request the inputs
    grossIncome = float(input("Enter the gross income: "))
    numDependents = int(input("Enter the number of dependents: "))

    # Calculate taxes
    federal_tax, state_tax = calculate_taxes(grossIncome, numDependents)

    # Display the federal and state income tax
    print(f"The Federal income tax is ${federal_tax}")
    print(f"The State income tax is ${state_tax}")
