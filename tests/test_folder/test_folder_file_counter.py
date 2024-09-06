"""Module for testing the FileCounter class functionality."""

import pytest

from src.work_tools.folder.folder_file_counter import FileCounter


@pytest.fixture
def file_counter_fixture():
    """Fixture to create a FileCounter instance."""
    return FileCounter()

# pylint: disable=redefined-outer-name
def test_count_files_without_return(
        file_counter_fixture: FileCounter
    )->None:
    """Test counting files without specifying an extension."""
    # 假设你的 count_files 方法返回文件数量
    file_counter_fixture.count_files("tests")
    file_counter_fixture.count_files("tests", ".py")
    file_counter_fixture.count_files("tests", [".py",".txt",".yml"], True)

# pylint: disable=redefined-outer-name
def test_count_files_with_return(
        file_counter_fixture: FileCounter
    )->None:
    """Test counting files without specifying an extension."""
    assert len(file_counter_fixture.count_files_dict("tests")) == 2
    assert len(file_counter_fixture.count_files_dict("tests", ".py")) == 1
    assert file_counter_fixture.count_files_dict("tests", ".py",True) == {'.py': 5}
    assert file_counter_fixture.count_files_dict("tests", [".py",".txt",".yml"], True) == {'.py': 5,'.yml': 1}

# pylint: disable=redefined-outer-name
def test_count_files_doc(
    file_counter_fixture: FileCounter
) -> None:
    '''
    测试doc是否正常
    '''
    assert file_counter_fixture.__doc__ is not None
