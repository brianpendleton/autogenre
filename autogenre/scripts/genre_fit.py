#!/usr/bin/env python
"""
Script to auto calculate the genre of a book. It uses a user defined CSV rubric
for the metrics to calculate, and a json file of book descriptions.

Argparse or Optparse could be used, but no current requirements for optional
flags or features to the script.
"""

import sys
from operator import itemgetter
from autogenre.load import load_json, load_points_file
from autogenre.calc import count_keyword_hits, calc_genre_fit


def main(json_file, genre_file):

    # Load the points file from CSV
    genres = load_points_file(genre_file)
    keywords = set(g.keyword for g in genres)

    results = {}
    for book in load_json(json_file):  # Loads the json as a stream/iterable
        hits = count_keyword_hits(keywords, book['description'])
        results[book['title']] = calc_genre_fit(genres, hits)

    print_results(results)  # Print at the end for alphabetical sort


def print_results(results):
    # Sorts the keys (book titles) alphabetically
    sorted_titles = sorted(results.keys(), key=itemgetter(0))
    for title in sorted_titles:

        # Get the genre-fit score for this title, and sort by the values (desc)
        res = results[title]
        sorted_res = sorted(res.iteritems(), key=itemgetter(1), reverse=True)

        print '\n{}'.format(title)
        for genre, score in sorted_res[0:3]:  # We only print the top 3
            print '{}, {}'.format(genre, score)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        msg = """
        Invalid arguments specified.
        Usage:
        python genre_fit.py <json_filepath> <genre_points_csv_filepath>
        """
        print msg
    else:
        main(sys.argv[1], sys.argv[2])

