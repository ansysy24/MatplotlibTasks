from collections import Counter
from matplotlib import pyplot as plt
import pandas as pd

data_file_path = 'pl.csv'


def get_axis(data_file_path: str):
    '''
    Method takes a data file path as an input.
    Returns a tuple with x and y axis data
    '''
    plt.xkcd()
    data = pd.read_csv('pl.csv')

    print(data['Responder_id'])

    counter = Counter()
    for element in data['LanguagesWorkedWith']:
        counter.update(element.split(';'))

    items = counter.most_common()
    items.reverse()
    return ([tup[0] for tup in items], [tup[1] for tup in items])


axis_data = get_axis(data_file_path)
plt.barh(axis_data[0], axis_data[1], label='Python')
plt.show()
