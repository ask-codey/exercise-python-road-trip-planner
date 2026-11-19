"""A road trip planner: five functions for you to finish.

A trip is kept two ways:
- stops: a list of the cities, in order, from the start to the destination,
  such as ["Chicago", "Omaha", "Denver", "Moab", "Grand Canyon"].
- legs: a list of (city, miles) tuples, one for each day's drive: the city
  you reach that day and the miles it takes, such as
  [("Omaha", 470), ("Denver", 540), ("Moab", 355), ("Grand Canyon", 330)].

The docstring under each function says what it should do, with examples.
Replace each raise NotImplementedError("Not built yet.") line with your own
code. The tests read what each function returns, or, for add_stop, what it
does to the list it's given.
"""


def add_stop(stops, city):
    """Put city into stops right before the last stop, so the destination stays last.

    The list itself changes; add_stop doesn't need to return anything.
    If city is already in stops, leave the list as it is.

    stops = ["Chicago", "Denver", "Grand Canyon"]
    add_stop(stops, "Moab")    -> stops is now ["Chicago", "Denver", "Moab", "Grand Canyon"]
    add_stop(stops, "Denver")  -> stops stays ["Chicago", "Denver", "Moab", "Grand Canyon"]
    """
    raise NotImplementedError("Not built yet.")


def total_miles(legs):
    """Return the miles of every leg added together.

    A trip with no legs has driven 0 miles.

    total_miles([("Omaha", 470), ("Denver", 540), ("Moab", 355), ("Grand Canyon", 330)]) -> 1695
    total_miles([("Omaha", 470)]) -> 470
    total_miles([]) -> 0
    """
    raise NotImplementedError("Not built yet.")


def longest_leg(legs):
    """Return the (city, miles) tuple of the leg with the most miles.

    When two legs tie for the most miles, return the first of them.
    When there are no legs, return None.

    longest_leg([("Omaha", 470), ("Denver", 540), ("Moab", 355), ("Grand Canyon", 330)]) -> ("Denver", 540)
    longest_leg([("Moab", 355), ("Page", 355)]) -> ("Moab", 355)
    longest_leg([]) -> None
    """
    raise NotImplementedError("Not built yet.")


def first_and_last(stops, count=2):
    """Return a tuple of two lists: the first count stops, and the last count stops.

    count is how many stops go in each list, 2 when a call leaves it out, and
    always at least 1. When the trip has fewer stops than count, each list
    holds the whole trip.

    stops = ["Chicago", "Omaha", "Denver", "Moab", "Grand Canyon"]
    first_and_last(stops)     -> (["Chicago", "Omaha"], ["Moab", "Grand Canyon"])
    first_and_last(stops, 1)  -> (["Chicago"], ["Grand Canyon"])
    first_and_last(["Chicago", "Denver"], 3) -> (["Chicago", "Denver"], ["Chicago", "Denver"])
    """
    raise NotImplementedError("Not built yet.")


def itinerary_lines(legs):
    """Return a list of strings, one for each leg, numbered from day 1.

    Each line is "Day <number>: <city>, <miles> miles". With no legs, return [].

    itinerary_lines([("Omaha", 470), ("Denver", 540)])
    -> ["Day 1: Omaha, 470 miles", "Day 2: Denver, 540 miles"]
    """
    raise NotImplementedError("Not built yet.")
