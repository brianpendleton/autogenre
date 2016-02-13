import ijson
import csv
from collections import namedtuple

GenreKeyword = namedtuple('GenreKeyword', 'genre, keyword, points')


def load_json(filepath):
    """
    Returns a generator that will stream a JSON file.  This utilizes the ijson
    python package: https://pypi.python.org/pypi/ijson.

    Parameters
    ----------
    filepath: str
        The filepath to the JSON input file.

    Returns
    -------
    result: generator
        A generator to consume the JSON elements
    """
    f = open(filepath)
    return ijson.items(f, 'item')


def load_points_file(filepath):
    """
    Returns a list of GenreKeyword namedtuples that represent the points we
    use to calculate the genre-fit.

    Parameters
    ----------
    filepath: str
        The filepath to the CSV input file.

    Returns
    -------
    result: list

    """
    with open(filepath, 'rb') as f:
        csv_reader = csv.reader(f, skipinitialspace=True)
        next(csv_reader)  # skip the header row
        return [GenreKeyword(r[0], r[1], int(r[2])) for r in csv_reader]
