import pandas as pd

json = [
    {
        'class': 'Year 1',
        'student count': 20,
        'room': 'Yellow',
        'info': {
            'teachers': {
                'math': 'Rick Scott',
                'physics': 'Elon Mask'
            }
        },
        'students': [
            {
                'name': 'Tom',
                'sex': 'M',
                'grades': {'math': 66, 'physics': 77}
            },
            {
                'name': 'James',
                'sex': 'M',
                'grades': {'math': 80, 'physics': 78}
            },
        ]
    },
    {
        'class': 'Year 2',
        'student count': 25,
        'room': 'Blue',
        'info': {
            'teachers': {
                'math': 'Alan Turing',
                'physics': 'Albert Einstein'
            }
        },
        'students': [
            {'name': 'Tony', 'sex': 'M'},
            {'name': 'Jacqueline', 'sex': 'F'},
        ]
    },
]
#The record_path value will create it's own dataframe first then we can specify other columns in meta from other values
d = pd.json_normalize(json, record_path='students',
                      meta=['class', 'student count', ['info', 'teachers', 'math'], ['info', 'teachers', 'physics']])
with pd.option_context('display.max_columns', None):
    print(d)



