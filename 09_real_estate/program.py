import csv
import operator
import os
try:
    import statistics
except:
    import statistics_standin_for_py2 as statistics

from models import Purchase


def print_the_header():
    print('-------------------------------')
    print('  REAL ESTATE DATA MINING APP')
    print('-------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    purchases = []
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            purchases.append(Purchase.create_from_dict(row))
    return purchases


def query_data(data: [Purchase]):
    data.sort(key=operator.attrgetter('price'))

    most_expensive = data[-1]
    print(f'The most expensive house is ${most_expensive.price:,} '
          f'with {most_expensive.beds} beds and {most_expensive.baths} baths')

    least_expensive = data[0]
    print(f'The least expensive house is ${least_expensive.price:,} '
          f'with {least_expensive.beds} beds and {least_expensive.baths} baths')

    print(f'The average home price is ${statistics.mean(purchase.price for purchase in data):,.2f}')

    print(f'The average price of a 2-bedroom home is '
          f'${statistics.mean(purchase.price for purchase in data if purchase.beds == 2):,.2f}')

def main():
    print_the_header()
    filename = get_data_file()
    load_file(filename)
    data = load_file(filename)
    # print(data[0].__dict__)
    query_data(data)


if __name__ == '__main__':
    main()
