# Prints the road trip's plan with your five functions from trip.py, so you can see them at work. Ready to use.
# Run it with: python plan.py
from trip import add_stop, first_and_last, itinerary_lines, longest_leg, total_miles

stops = ["Chicago", "Omaha", "Denver", "Grand Canyon"]
add_stop(stops, "Moab")
add_stop(stops, "Denver")

print("Road trip: Chicago to the Grand Canyon")
print("Stops:", stops)
first_two, last_two = first_and_last(stops)
print("Starts with", first_two, "and ends with", last_two)
print()

legs = [("Omaha", 470), ("Denver", 540), ("Moab", 355), ("Grand Canyon", 330)]
for line in itinerary_lines(legs):
    print(line)
print()

city, miles = longest_leg(legs)
print("Total:", total_miles(legs), "miles")
print("Longest drive:", miles, "miles, to", city)
