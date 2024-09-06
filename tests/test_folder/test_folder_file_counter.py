import pytest

from src.work_tools.folder.folder_file_counter import FileCounter


@pytest.fixture
def file_counter():
    return FileCounter()

def test_count_files_without_extension(file_counter):
    # 假设你的 count_files 方法返回文件数量
    file_counter.count_files("tests")

def test_count_files_with_extension(file_counter):
    file_counter.count_files("tests", ".py")

def test_count_files_with_recursive(file_counter):
    file_counter.count_files("tests", [".py",".txt",".yml"], True)