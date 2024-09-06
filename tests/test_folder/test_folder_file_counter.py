"""Module for testing the FileCounter class functionality."""

import pytest

from src.work_tools.folder.folder_file_counter import FileCounter


@pytest.fixture
def file_counter_fixture():
    """Fixture to create a FileCounter instance."""
    return FileCounter()

def test_count_files_without_return(
        fc_fixture: FileCounter  # 修改参数名以避免名称冲突
    )->None:
    """Test counting files without specifying an extension."""
    # 假设你的 count_files 方法返回文件数量
    fc_fixture.count_files("tests")
    fc_fixture.count_files("tests", ".py")
    fc_fixture.count_files("tests", [".py",".txt",".yml"], True)
