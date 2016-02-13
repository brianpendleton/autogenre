import os
import pytest

from autogenre.load import GenreKeyword
from autogenre.calc import calc_genre_fit, count_keyword_hits


TEST_TEXT = "The boy has a dog. The\nd\no\ng barked. The dog ran away"
GENRES = [
    GenreKeyword('human', 'boy', 6),
    GenreKeyword('human', 'ran', 4),
    GenreKeyword('canine', 'dog', 6),
    GenreKeyword('canine', 'barked', 8),
    GenreKeyword('canine', 'ran', 4),
    GenreKeyword('bird', 'chirp', 4),
]


def test_count_keyword_hits():
    res = count_keyword_hits(['boy', 'dog'], TEST_TEXT)
    assert res['boy'] == 1
    assert res['dog'] == 3


def test_count_keyword_hits_case_sensitive():
    res = count_keyword_hits(['the', 'a'], TEST_TEXT, case_sensitive=True)
    assert 'the' not in res
    assert res['a'] == 6


def test_count_keyword_missing_text():
    res = count_keyword_hits(['test'], "")
    assert not res


def test_count_keyword_missing_keywords():
    res = count_keyword_hits([], TEST_TEXT)
    assert not res


def test_calc_genre_fit():
    """
    {'ran': 1, 'boy': 1, 'dog': 3, 'barked': 1}
    canine average -> 'dog': 6 + 'barked': 8 + 'ran': 4 = 18 / 3 = 6
    human average  -> 'boy': 6 + 'ran': 4 = 10 / 2 = 5

    Three unique keyword hits for DOG keywords: 3x10 = 30
    Two unique keyword hits for HUMAN keywords: 2x5 = 10
    No hits for BIRD: 0
    {'canine': 30, 'human': 10, 'bird': 0}
    """

    keywords = set(g.keyword for g in GENRES)
    hits = count_keyword_hits(keywords, TEST_TEXT)
    res = calc_genre_fit(GENRES, hits)

    assert res['canine'] == 30
    assert res['human'] == 10
    assert res['bird'] == 0


if __name__ == '__main__':
    pytest.main()
