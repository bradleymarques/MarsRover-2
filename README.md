# MarsRover

Welcome to the Mars Rover project documentation.

## Overview

This is a simulation of a Mars Rover. The basic functionality of the rover is:

Move forward
Rotate left
Rotate right

A Mars sector and starting point and initial direction must be specified before
commands can be sent to the device.

## Installation

You will need Python 3.6+ and git installed to run the application.

1. Type in git clone https://github.com/deanraemaekers/MarsRover.git
2. Type in cd MarsRover
3. Type in "pip install -r requirements.txt"

## Usage

To start the Mars Rover, simply type "python app.py".

1. First, you will need to create a Mars sector.

The prompt will read:

* Enter mars sector coordinates:

The sector can be a maximum of 9x9 squares.

The format must be a single number between 11 and 99.

2. Next, you will need to enter a starting position and direction.

The prompt will read:

* Enter starting position and direction:

The format must be a number (eg 12) followed by a space, followed by a cardinal direction (eg N, W, E, S)

For example: 12 E

3. Enter Rover commands

Valid commands are: M, L, R

* M - The rover will move one position
* L - The rover will rotate left
* R - The rover will rotate right

Commands can be sent as a single instruction, eg: M
Or as a string of instructions, eg: MMMLRLRMRMMMMRMMMMM

## Design decisions

I noted that the format for creating the grid was specified as "88", and this represented an 8x8 grid.

However, this could become ambiguous if there was a number such as 103. This is why I limited the grid
size to 9x9.

Another option would have been to only allow even numbers and split them in half.

I have attempted to do good input validation and separate the methods and functions used into parts that
are as testable as possible.

## Testing

To test the project, just type "pytest".

There are 3 test files:

- test_input.py, testing the input validation
- test_rover.py, testing the Rover class methods
- test_user_story.py, testing the application from a user point of view


