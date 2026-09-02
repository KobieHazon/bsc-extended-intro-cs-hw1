from pathlib import Path

import pytest

from extended_intro_hw1 import avg_word_len, k_boom, max_even_seq

REPOSITORY_ROOT = Path(__file__).parents[1]
FIXTURES = REPOSITORY_ROOT / "assignment/fixtures"


def test_avg_word_len_matches_supplied_dorian_gray_result(monkeypatch, tmp_path) -> None:
    monkeypatch.chdir(tmp_path)

    avg_word_len(FIXTURES / "dorian_gray.txt")

    assert (
        Path("output.txt").read_text(encoding="utf-8").splitlines()
        == (FIXTURES / "output_dorian_gray.txt").read_text(encoding="utf-8").splitlines()
    )


def test_avg_word_len_handles_blank_and_whitespace_only_lines(monkeypatch, tmp_path) -> None:
    input_path = tmp_path / "input.txt"
    input_path.write_text("one three\n\n  two   four  \n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    avg_word_len(input_path)

    assert Path("output.txt").read_text(encoding="utf-8") == "4.0\n0\n3.5\n"


def test_k_boom_matches_assignment_sample() -> None:
    assert k_boom(15, 7) == "1 2 3 4 5 6 boom-boom! 8 9 10 11 12 13 boom! 15"


def test_k_boom_matches_supplied_fixture() -> None:
    expected = (FIXTURES / "boom_sol.txt").read_text(encoding="utf-8").split()

    assert k_boom(100, 6).split() == expected


@pytest.mark.parametrize(
    ("n", "k", "expected"),
    [
        (559933195, 2, 0),
        (6284062826648, 2, 13),
        (9632569636984596322, 3, 6),
        (889562836895888958888, 8, 4),
        (123456789987654321, 1, 18),
    ],
)
def test_max_even_seq_matches_supplied_cases(n: int, k: int, expected: int) -> None:
    assert max_even_seq(n, k) == expected


@pytest.mark.parametrize(
    ("function", "arguments"),
    [(k_boom, (0, 2)), (k_boom, (10, 0)), (max_even_seq, (-1, 2)), (max_even_seq, (10, 10))],
)
def test_invalid_numeric_inputs_are_rejected(function, arguments) -> None:
    with pytest.raises(ValueError):
        function(*arguments)
