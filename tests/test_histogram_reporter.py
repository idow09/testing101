from src.histogram_reporter import HistogramReporter


def test_histogram_reporter(tmp_path, mocker):
    # Arrange
    tmp_file = tmp_path / "tmp.txt"
    tmp_file.write_text("aaaaBBBcc")

    mock_print = mocker.patch("builtins.print")

    expected = " a : ####\n B : ###\n c : ##"

    # Act
    HistogramReporter().process(tmp_file)

    # Assert
    mock_print.assert_called_with(expected)
