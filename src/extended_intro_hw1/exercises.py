"""Maintained implementations of the three programming questions."""

from __future__ import annotations

from pathlib import Path

OUTPUT_FILENAME = "output.txt"


def avg_word_len(filename: str | Path) -> None:
    """Write the average word length of each input line to ``output.txt``."""
    input_path = Path(filename)
    with (
        input_path.open(encoding="utf-8") as input_file,
        Path(OUTPUT_FILENAME).open("w", encoding="utf-8", newline="\n") as output_file,
    ):
        for line in input_file:
            words = line.split()
            average = sum(map(len, words)) / len(words) if words else 0
            output_file.write(f"{average}\n")


def k_boom(n: int, k: int) -> str:
    """Return the numbers from 1 to ``n`` using the assignment's K-boom rules."""
    _validate_inputs(n, k)
    values: list[str] = []
    for current_number in range(1, n + 1):
        contains_k = str(k) in str(current_number)
        divisible_by_k = current_number % k == 0
        if contains_k and divisible_by_k:
            values.append("boom-boom!")
        elif contains_k or divisible_by_k:
            values.append("boom!")
        else:
            values.append(str(current_number))
    return " ".join(values)


def max_even_seq(n: int, k: int) -> int:
    """Return the longest contiguous run of decimal digits divisible by ``k``."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if not 1 <= k <= 9:
        raise ValueError("k must be a digit between 1 and 9")

    longest = 0
    current = 0
    for digit in str(n):
        if int(digit) % k == 0:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest


def _validate_inputs(n: int, k: int) -> None:
    if n < 1:
        raise ValueError("n must be positive")
    if not 1 <= k <= 9:
        raise ValueError("k must be a digit between 1 and 9")
