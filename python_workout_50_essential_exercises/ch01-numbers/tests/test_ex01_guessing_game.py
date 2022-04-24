from python_workout_50_essential_exercises.numeric_types.ex01_guessing_game import guessing_game
import random
from io import StringIO


def test_correct_guess(monkeypatch, capsys):
    random.seed(0)
    monkeypatch.setattr('sys.stdin', StringIO('49'))  # mocking a user input == 49
    guessing_game()
    captured_out, captured_err = capsys.readouterr()  # capturing what is being printed to stdout and stderr
    assert captured_out.endswith('Right! The answer is 49\n')


def test_too_low(monkeypatch, capsys):
    random.seed(0)

    monkeypatch.setattr('sys.stdin', StringIO('1\n49\n'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert 'Your guess of 1 is too low!' in captured_out
    assert captured_out.endswith('Right! The answer is 49\n')


def test_too_high(monkeypatch, capsys):
    random.seed(0)

    monkeypatch.setattr('sys.stdin', StringIO('59\n49\n'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert 'Your guess of 59 is too high!' in captured_out
    assert captured_out.endswith('Right! The answer is 49\n')


def test_too_low_twice(monkeypatch, capsys):
    random.seed(0)

    monkeypatch.setattr('sys.stdin', StringIO('1\n2\n49'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert 'Your guess of 1 is too low!' in captured_out
    assert 'Your guess of 2 is too low!' in captured_out

    assert captured_out.endswith('Right! The answer is 49\n')


def test_too_high_twice(monkeypatch, capsys):
    random.seed(0)

    monkeypatch.setattr('sys.stdin', StringIO('59\n79\n49'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert 'Your guess of 59 is too high!' in captured_out
    assert 'Your guess of 79 is too high!' in captured_out

    assert captured_out.endswith('Right! The answer is 49\n')

