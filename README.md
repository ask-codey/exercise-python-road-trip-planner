# Exercise: Road Trip Planner

Exercise code for the lesson **Exercise: Road Trip Planner** in the Python in Depth course on [ask-codey.com](https://www.ask-codey.com).

A road trip from Chicago to the Grand Canyon needs a planner: one that adds a stop before the destination, adds up the miles, finds the longest drive, shows the first and last stops, and lists each day's drive. You'll write its five functions in `trip.py`, and tests call each function to check what it returns.

## What's here

- `trip.py`: the five functions, `add_stop`, `total_miles`, `longest_leg`, `first_and_last` and `itinerary_lines`. Each one stops with `NotImplementedError: Not built yet.` for now. The docstring under each says what it should do, with examples. For you to finish.
- `plan.py`: prints the trip's plan with your five functions, so you can see them at work. Ready to use.
- `tests/test_trip.py`: tests that call your functions and check what comes back. You don't need to change this file.
- `requirements.txt`: the one package the tests need, pytest, at an exact version. Ready to use.
- `pytest.ini`: tells pytest where the tests are and where to find `trip.py`. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment and the files Python and pytest make as they run. Ready to use.

The tests and `plan.py` bring your functions in with an `import` line, such as `from trip import total_miles`. *import and the Standard Library*, in Module 3, explains how that works.

## Before you start

The tests need pytest, and pytest goes in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it: here, only pytest.

*Virtual Environments and pip*, in Module 3, explains all three. The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

## Check your work

```bash
pytest
```

At first every test fails: that is expected, because each function stops with a `NotImplementedError` for now. Each function you finish turns its tests green. A failing test's message says what it called, what it expected and what came back, for example *total_miles([]) should return 0, but it returned None.*

To see your functions at work, run:

```bash
python plan.py
```

## The rules

- Keep each function's name and parameters as they are.
- `add_stop` changes the list it's given. The other four return their answer and change nothing; the tests read what comes back.
- A trip's `stops` is a list of city names, from the start to the destination. Its `legs` is a list of `(city, miles)` tuples, one for each day's drive.
- Don't change the tests or `plan.py`.

## Tips

- Work one example through by hand before you write the code: which leg of the four is the longest, and what are its city and miles?
- `in` checks whether a value is in a list, and `.insert()` puts an item at an index. A negative index counts from the end.
- `for city, miles in legs:` unpacks each leg as the loop reaches it.
- A slice such as `stops[:2]` never stops with an error, even when the list is shorter than the slice.
- `enumerate(legs, start=1)` numbers the legs from 1, and an f-string builds each line: `f"Day {day}: {city}"` is its start.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.
