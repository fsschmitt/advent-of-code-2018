import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_lines(fname):      
    with open(f'{BASE_DIR}/../input/{fname}') as f:
        return [x.strip() for x in f.readlines()]