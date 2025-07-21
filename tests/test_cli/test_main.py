from click.testing import CliRunner

from cli.main import main
from _pytest.monkeypatch import MonkeyPatch


def test_main_help() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Usage" in result.output


def test_check_command(monkeypatch: MonkeyPatch) -> None:
    runner = CliRunner()

    def fake_check(urls: list[str]) -> list[str]:
        return ["http://broken"]

    monkeypatch.setattr("cli.main.check_links", fake_check)
    result = runner.invoke(main, ["check", "http://broken", "http://ok"])
    assert result.exit_code == 0
    assert "http://broken" in result.output
