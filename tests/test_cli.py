from extended_intro_hw1_cli import cli


def test_k_boom_cli(monkeypatch, capsys) -> None:
    monkeypatch.setattr("sys.argv", ["extended-intro-hw1", "k-boom", "8", "7"])

    cli()

    assert capsys.readouterr().out == "1 2 3 4 5 6 boom-boom! 8\n"


def test_max_even_seq_cli(monkeypatch, capsys) -> None:
    monkeypatch.setattr("sys.argv", ["extended-intro-hw1", "max-even-seq", "24008", "2"])

    cli()

    assert capsys.readouterr().out == "5\n"
