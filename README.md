# autogenre

A simple script for calculating a "best-guess" at the genre for a book

## Time spent

The time breakdown was roughly 5 hours on the coding.  That included a pure python
solution and a more Pandas/NumPy version.  I scrapped the Pandas version because it
felt like cheating, that library does a lot of heavy lifting for you.  I spent some 
time testing and writing tests so I could get some use cases down and understand the problem.

## Steps to run

I built this on python 2.7
Tested on Windows and Linux (using pythonanywhere)

- Unzip contents to autogenre folder (or clone: https://github.com/brianpendleton/autogenre.git)
- cd autogenre
- python setup.py develop

### Command
python autogenre/scripts/genre_fit.py tests/resource/sample_book_json.txt tests/resource/sample_genre_keyword_value.csv

### Tests
I couldn't get nosetests working on pythonanywhere, but it did work locally

- cd autogenre
- nosetests --with-coverage


## Edge cases
- I was concerned about the file size of the JSON, so I went for a streaming 
solution using ijson.
- I originally did all the computations using Pandas which is good for things
like grouping and calculating means over filters. I removed it as the calculations 
weren't large enough to warrant utilizing the library. If the CSV for the points
is much larger with denser groups, Pandas would be a smart option to bring back.
- Book descriptions with multilines
- Adding options for JSON file or a URL (a probable use case)
