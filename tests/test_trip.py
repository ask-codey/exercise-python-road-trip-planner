# Tests for trip.py. Run them with: pytest (in the exercise folder, with the virtual environment active).
# Each test calls one of your functions with the values in its name and checks what it returns (or, for add_stop,
# what the list holds afterward). A failing test says what it called, what it expected and what came back.
# You don't need to change this file.
from trip import add_stop, first_and_last, itinerary_lines, longest_leg, total_miles

LEGS = [("Omaha", 470), ("Denver", 540), ("Moab", 355), ("Grand Canyon", 330)]


def check(call, got, expected):
    """Fails with a message that says what the call returned and what it should return."""
    assert got == expected, f"{call} should return {expected!r}, but it returned {got!r}."


def check_list(call, got, expected):
    """Fails with a message that says what the list holds after the call and what it should hold."""
    assert got == expected, f"After {call}, the stops should be {expected!r}, but they are {got!r}."


def test_1_add_stop_moab_goes_before_grand_canyon():
    stops = ["Chicago", "Denver", "Grand Canyon"]
    add_stop(stops, "Moab")
    check_list('add_stop(stops, "Moab")', stops, ["Chicago", "Denver", "Moab", "Grand Canyon"])


def test_2_add_stop_denver_to_a_two_stop_trip_goes_in_the_middle():
    stops = ["Chicago", "Grand Canyon"]
    add_stop(stops, "Denver")
    check_list('add_stop(stops, "Denver")', stops, ["Chicago", "Denver", "Grand Canyon"])


def test_3_add_stop_denver_already_there_leaves_the_list_as_it_is():
    stops = ["Chicago", "Denver", "Grand Canyon"]
    add_stop(stops, "Denver")
    check_list('add_stop(stops, "Denver")', stops, ["Chicago", "Denver", "Grand Canyon"])


def test_4_total_miles_four_legs_is_1695():
    check("total_miles(LEGS)", total_miles(LEGS), 1695)


def test_5_total_miles_one_leg_of_470_is_470():
    check('total_miles([("Omaha", 470)])', total_miles([("Omaha", 470)]), 470)


def test_6_total_miles_no_legs_is_0():
    check("total_miles([])", total_miles([]), 0)


def test_7_longest_leg_of_four_is_denver_540():
    check("longest_leg(LEGS)", longest_leg(LEGS), ("Denver", 540))


def test_8_longest_leg_tie_at_355_is_the_first_moab():
    check('longest_leg([("Moab", 355), ("Page", 355)])', longest_leg([("Moab", 355), ("Page", 355)]), ("Moab", 355))


def test_9_longest_leg_no_legs_is_none():
    check("longest_leg([])", longest_leg([]), None)


def test_10_first_and_last_five_stops_gives_two_and_two():
    stops = ["Chicago", "Omaha", "Denver", "Moab", "Grand Canyon"]
    check("first_and_last(stops)", first_and_last(stops), (["Chicago", "Omaha"], ["Moab", "Grand Canyon"]))


def test_11_first_and_last_five_stops_count_1_gives_chicago_and_grand_canyon():
    stops = ["Chicago", "Omaha", "Denver", "Moab", "Grand Canyon"]
    check("first_and_last(stops, 1)", first_and_last(stops, 1), (["Chicago"], ["Grand Canyon"]))


def test_12_first_and_last_two_stops_count_3_gives_the_whole_trip_twice():
    stops = ["Chicago", "Denver"]
    check("first_and_last(stops, 3)", first_and_last(stops, 3), (["Chicago", "Denver"], ["Chicago", "Denver"]))


def test_13_itinerary_lines_four_legs_from_day_1_to_day_4():
    check("itinerary_lines(LEGS)", itinerary_lines(LEGS), [
        "Day 1: Omaha, 470 miles",
        "Day 2: Denver, 540 miles",
        "Day 3: Moab, 355 miles",
        "Day 4: Grand Canyon, 330 miles",
    ])


def test_14_itinerary_lines_one_leg_is_day_1_moab_355_miles():
    check('itinerary_lines([("Moab", 355)])', itinerary_lines([("Moab", 355)]), ["Day 1: Moab, 355 miles"])


def test_15_itinerary_lines_no_legs_is_an_empty_list():
    check("itinerary_lines([])", itinerary_lines([]), [])
