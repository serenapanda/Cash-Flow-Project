#!/usr/bin/env python3  
#===============================================================================
# personal_financial_statement.py
#===============================================================================
"""Python 3 implementation of the personal financial spreadsheet"""

# Imports ----------------------------------------------------------------------
import argparse
import itertools
from fancyprint import fprint

# Functions --------------------------------------------------------------------

def income(earned, real_estate):
    """calculate total income from earned and passive income"""

    fprint('Income', color='b', style='bu')
    earned_lines = []
    for number, value in itertools.islice(
        enumerate([0] + args.earned),
        1,
        None
    ):
        earned_lines.append(f'Earned #{number}: {value}')
    for earned_line in earned_lines:
        print(earned_line)
    earned_total = round(sum(args.earned), 2)
    
    passive_lines = [real_estate, business]
    passive_total = total(real_estate, business)
    total_income = total(earned_total, passive_total)

    earned_total_line = f'Earned Total: {earned_total}'
    real_estate_line = f'Real Estate: {real_estate}'
    business = f'Business: {business}'
    passive_total_line = f'Passive Total: {passive_total}'
    total_income_line = f'Total Income: {total_income}'

    income_lines = earned_lines + [
        earned_total_line,
        real_estate_line,
        passive_total_line,
        total_income_line
    ]

    x = max([len(line) for line in income_lines])
    

    fprint(earned_total_line, style='b')
    fprint(real_estate_line)
    fprint(business_line)
    fprint(passive_total_line, style='b')
    fprint('-' * x, style='b')
    fprint(total_income_line, style='b')



def total(x, y):
    return x + y


def main(args):
    income(args.earned, args.real_estate, args.business)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description = (
            'Python 3 implementation of the personal financial statement '
            'spreadsheet'
        )
    )
    income_group = parser.add_argument_group('income group')
    income_group.add_argument(
        '-e',
        '--earned',
        metavar='float',
        type=float,
        default=[0],
        nargs='+',
        help='Earned income values'
    )
    income_group.add_argument(
        '--real-estate',
        metavar='float',
        type=float,
        default=0,
        help='Real Estate (NET) income value'
    )
    income_group.add_argument(
        '--biz',
        metavar='float',
        type=float,
        default=0,
        help='Business (NET) income value'
    )
    return parser.parse_args()


# Execute ----------------------------------------------------------------------
if __name__ == '__main__':
    args=parse_arguments()
    main(args)    
