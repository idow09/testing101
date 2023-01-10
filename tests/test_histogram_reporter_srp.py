from src.histogram_reporter_srp import HistogramReporterSRP


def test_histogram_reporter_srp(mocker):
    # Arrange
    reader = mocker.MagicMock()
    reader.read_file.return_value = ['a', 'a', 'a', 'bbb', 'bbb', 'cc', 'cc', 'cc', 'cc']
    printer = mocker.MagicMock()

    expected = [("cc", 4), ("a", 3), ("bbb", 2)]

    # Act
    HistogramReporterSRP(reader, printer).process("dummy_path")

    # Assert
    reader.read_file.assert_called_with("dummy_path")
    printer.print_histogram.assert_called_with(expected)
