#!/usr/bin/env python3
# Program: taxform.py
# Author: Diego Alvarez

"""In this altered code, I deliberately changed the STATE_TAX_RATE value
from 0.0455 to 0.045 (an incorrect rate) to introduce an error in the state tax calculation."""

def calculate_taxes(gross_income, num_dependents):
    """
    Calculate federal and state income taxes.

    Args:
    - gross_income (float): Gross income.
    - num_dependents (int): Number of dependents.

    Returns:
    - Tuple: (federal_income_tax, state_income_tax)
    """
    FEDERAL_TAX_RATE = 0.20
    STATE_TAX_RATE = 0.045  # Incorrect state tax rate
    STANDARD_DEDUCTION = 10000.0
    DEPENDENT_DEDUCTION = 3000.0

    # Calculate deductions for standard and dependents
    total_deductions = STANDARD_DEDUCTION + (DEPENDENT_DEDUCTION * num_dependents)

    # Calculate taxable income after deductions
    taxable_income = max(gross_income - total_deductions, 0)

    # Calculate federal and state income taxes
    federal_income_tax = round(taxable_income * FEDERAL_TAX_RATE, 2)
    state_income_tax = round(taxable_income * STATE_TAX_RATE, 2)  # Error in state tax rate

    return federal_income_tax, state_income_tax

if __name__ == "__main__":
    # Input values from user
    grossIncome = float(input("Enter the gross income: "))
    numDependents = int(input("Enter the number of dependents: "))

    # Calculate taxes
    federal_tax, state_tax = calculate_taxes(grossIncome, numDependents)

    # Display the federal and state income tax
    print(f"The Federal income tax is ${federal_tax}")
    print(f"The State income tax is ${state_tax}")
