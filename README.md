# autogenre

A simple script for calculating a "best-guess" at the genre for a book

## Steps to run

I built this on python 2.7

install_requires=['pytest', 'ijson']


## Edge cases
- I was concerned about the file size of the JSON, so I went for a streaming 
solution using ijson.
- I originally did all the computations using Pandas which is good for things
like grouping and calculating means over filters. I removed it as the calculations 
weren't large enough to warrant utilizing the library. If the CSV for the points
is much larger with denser groups, Pandas would be a smart option to bring back.
- Book descriptions with multilines
- Adding options for JSON file or a URL (a probable use case)

Any steps necessary to run your program
Any interesting trade-offs or edge cases you ran into
Approximately how long you spent (this is not timed, but it’s helpful for us)
