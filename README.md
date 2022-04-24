# Python Exercises

## Python Workout: 50 ten-minute exercises 
Reuven Lerner
https://www.manning.com/books/python-workout

### 1. Numbers
- [x] [Guessing Game](https://github.com/najmabad/python_exercises/blob/main/python_workout_50_essential_exercises/ch01-numbers/ex01_guessing_game.py)

Notes:
- `random.randint(a,b)` --> both extremes are included
- if you want to create an infinite loop, you can use `while True` and then have one break condition
- `user_guess` is best placed inside and at the start of the loop
- if you use two `elif` the conditions are clearer
- [x] [Test Guessing Game](https://github.com/najmabad/python_exercises/blob/main/python_workout_50_essential_exercises/ch01-numbers/tests/test_ex01_guessing_game.py)

Notes:
- you can use `monkeypatch` to mimic something. For example, with `monkeypatch.setattr('sys.stdin', StringIo('49\n')` we mimic a user that enters 49 through the consooe
- `capsys` is used to capture what is being printed by a function. It returns a namedtuple, that you can unpack with `captured_out, captured_err = capsys.readouterr()`
- we tested: correct flow, too low, two high, too low (twice), too high (twice)

### 2. Strings
### 3. Lists and tuples
### 4. Dictionaries and sets
### 5. Files
### 6. Functions
### 7. Functional programming
### 8. Modules
### 9. Objects
### 10. Iterators and generators



