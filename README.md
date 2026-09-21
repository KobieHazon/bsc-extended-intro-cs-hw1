# Extended Introduction to Computer Science - Homework 1

A 2017 CS BSc introductory Python assignment covering per-line text statistics, conditional string generation, and a single-pass digit-sequence algorithm. The programming submission implements questions 3, 5, and 6; the retained written-answer PDF covers the conceptual and runtime-analysis questions.

## Exercises

- `avg_word_len`: writes the average word length for every input line to `output.txt`, treating blank lines as zero.
- `k_boom`: generates the sequence from 1 through `n`, replacing values that contain or are divisible by digit `k` with `boom!` or `boom-boom!`.
- `max_even_seq`: finds the longest contiguous run of digits that are divisible by `k` in one pass.

## Setup

```bash
git clone https://github.com/KobieHazon/bsc-extended-intro-cs-hw1.git
cd bsc-extended-intro-cs-hw1
uv sync --dev
```

The maintained package supports Python 3.10 or newer and has no runtime dependencies.

## Usage

```bash
uv run extended-intro-hw1 k-boom 15 7
uv run extended-intro-hw1 max-even-seq 6284062826648 2
uv run extended-intro-hw1 average-word-length assignment/fixtures/dorian_gray.txt
```

The first command prints:

```text
1 2 3 4 5 6 boom-boom! 8 9 10 11 12 13 boom! 15
```

The average-word-length command writes the assignment-required `output.txt` in the current directory.

## Testing

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

The tests reproduce the supplied Dorian Gray output, the complete 100-value K-boom fixture, all five supplied digit-sequence cases, blank-line behavior, invalid inputs, and command-line output.

## Repository Structure

- `assignment/hw1_tester.py`: supplied tester preserved in its original form
- `assignment/fixtures/`: supplied input and expected-output files used by that tester
- `assignment/score-key.pdf`: supplied generic grading key
- `solution/written-answers.pdf`: my four-page written submission
- `src/extended_intro_hw1/`: Python package containing the implementations and command-line interface
- `tests/`: portable pytest regression suite derived from the supplied checks
