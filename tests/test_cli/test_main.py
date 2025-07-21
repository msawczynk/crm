from click.testing import CliRunner

from cli.main import main


def test_main() -> None:
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "CRM CLI placeholder" in result.output
