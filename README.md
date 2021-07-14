# Sunburst

Sunburst is a Python console application for building and testing ideas for a lightshow.

## Background
![Studio 54 Sunburst](/sunburst7.jpg "Studio 54 Sunburst")
While working on modifying the above installation by artist Erika Margaret to control 10 sections of RGB LED lights, I wanted to test different effects without using the actual installation and its hardware. The screen display shows 10 shapes that are in the same configuration as the planned lighting for this installation.

This project has also served to learn Python and practice Object Oriented Programming.

## Required Features
3 + features to submit project for Code Louisville Python class: 
1. Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program.
2. Create a class, then create at least one object of that class and populate it with data. The value of at least one object must be used somewhere in your code.
3. Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.
4. Read data from an external file, such as text, JSON, CSV, etc and use that data in your application.
5. Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code.
6. Visualize data in a graph, chart, or other visual representation of data.
## Usage

```
pip install 'pygame==2.0.1'
pip install itertools
pip install csv

python sunburst.py

# runs a lightshow that cycles through colors, one at a time, from bottom sections to top sections
1

# returns lightshow that cycles through colors, one at a time, from inside sections to outside sections
2

# runs a lightshow that cycles through colors, one at a time, covering all sections at the same time, from bottom sections to top sections
3

# quits
ESC
```
## Contributing
Pull requests are welcome.

## Support
Contact <discolarrence@gmail.com>

## License
[MIT](https://choosealicense.com/licenses/mit/)