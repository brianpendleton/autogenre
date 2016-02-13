import re
from itertools import groupby
from operator import attrgetter


def count_keyword_hits(keywords, text, case_sensitive=False):
    """
    Counts the number of case-insensitive keyword matches.

    Parameters
    ----------
    keywords: list
        The list of words to search for in the text
    text: str
        The text to lookup the keywords in
    case_sensitive: bool

    Examples
    --------

    >>> count_keyword_hits(['boy', 'dog'], "The boy has a dog. The dog barked")
    {'boy': 1, 'dog': 2}
    >>> count_keyword_hits(['the', 'a'], "The dog barked", case_sensitive=True)
    {'a': 1}
    >>> count_keyword_hits(['the', 'a'], "The dog barked", case_sensitive=False)
    {'a': 1, 'the': 1}

    Returns
    -------
    A dictionary of the matches with their respective count

    """
    flags = 0 if case_sensitive else re.I
    counts = {}
    for word in keywords:
        # Here we don't care about the match object returned by re.finditer, we
        # only care about counting the number of matches.
        hits = sum(1 for _ in re.finditer(r'%s' % re.escape(word), text, flags))
        if hits:
            counts[word] = hits
    return counts


def calc_genre_fit(genres, hit_counts):
    """
    Calculates a score by genre. Scores are calculated using:
        total num keyword matches * avg point value of unique matching keywords

    Parameters
    ----------
    genres: list(GenreKeywords)
        A list of GenreKeyword namedtuples that represent the CSV for points
    hit_counts: dict
        The {keyword: count} result from count_keyword_hits

    Returns
    -------

    """
    scores = {}
    for k, row in groupby(genres, attrgetter('genre')):
        scores[k] = 0

        # We only care about rows from the CSV that we have counts for
        points = [r for r in row if r.keyword in hit_counts]

        if points:
            # A non-weighted average of the keyword points
            avg = sum(g.points for g in points) / len(points)
            hits = sum(hit_counts[g.keyword] for g in points)
            scores[k] = avg * hits
    return scores
