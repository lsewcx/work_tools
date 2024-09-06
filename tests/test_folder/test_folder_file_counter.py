"""Module for testing the FileCounter class functionality."""

import pytest

from src.work_tools.folder.folder_file_counter import FileCounter

@pytest.fixture
def get_file_counter_fixture():
    """Fixture to create a FileCounter instance."""
    return FileCounter()

def test_count_files_without_return(
        file_counter_fixture: FileCounter
    )->None:
    """Test counting files without specifying an extension."""
    # 假设你的 count_files 方法返回文件数量
    file_counter_fixture.count_files("tests")
    file_counter_fixture.count_files("tests", ".py")
    file_counter_fixture.count_files("tests", [".py",".txt",".yml"], True)
