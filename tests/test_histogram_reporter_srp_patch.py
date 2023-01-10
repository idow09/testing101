from src.histogram_reporter_srp_patch import HistogramReporterSRPPatch


def test_histogram_reporter_srp_simple_mock(mocker):
    # Arrange
    expected = [("cc", 4), ("a", 3), ("bbb", 2)]
    mocker.patch(
        "src.histogram_reporter_srp_patch.read_file",
        return_value=["a", "a", "a", "bbb", "bbb", "cc", "cc", "cc", "cc"],
    )
    spy_printer = mocker.MagicMock()
    mocker.patch("src.histogram_reporter_srp_patch.print_histogram", new=spy_printer)

    # Act
    HistogramReporterSRPPatch().process("dummy_path")

    # Assert
    spy_printer.assert_called_with(expected, symbol="#")
