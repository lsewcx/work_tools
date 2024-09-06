"""
用于统计文件夹中文件的数量。
"""

import os
from collections import Counter
from typing import List, Optional, Union

from loguru import logger


class FileCounter:
    """
    用于统计指定目录下的文件数量。
    """
    def __init__(self) -> None:
        """
        初始化 FileCounter 实例。
        """
    def __doc__(self):
        print(self.__doc__)

    def count_files(self,
                    folder_path: str,
                    file_extension: Union[str, List[str], Optional[str]] = None,
                    recursive: bool = False) -> None:
        """
        统计指定目录下的文件数量。

        参数:
        - folder_path (str): 要统计文件的目录路径。
        - file_extension (Union[str, List[str], Optional[str]]): 可选参数，指定要统计的文件扩展名。
          可以是单个扩展名的字符串，也可以是包含多个扩展名的列表。如果不提供此参数，将统计所有文件。
        - recursive (bool): 可选参数，指示是否递归统计子目录中的文件。默认为 False，即不递归。

        使用示例:
        ```python
        from folder_file_counter import FileCounter

        # 创建 FileCounter 实例
        file_counter = FileCounter()

        # 统计当前目录下所有文件的数量
        file_counter.count_files('.')

        # 统计当前目录下所有 .py 文件的数量
        file_counter.count_files('.', file_extension='.py')

        # 递归统计当前目录及所有子目录下所有 .py 和 .txt 文件的数量
        file_counter.count_files('.', file_extension=['.py', '.txt'], recursive=True)
        ```
        """
        counter = Counter()
        if isinstance(file_extension, str):
            file_extension = [file_extension]

        for _, dirs, files in os.walk(folder_path):  # 使用 _ 替换未使用的变量 root
            if not recursive:
                dirs.clear()
            for file in files:
                if file_extension is None or any(file.endswith(ext) for ext in file_extension):
                    ext = os.path.splitext(file)[1]
                    counter[ext] += 1

        total_files = sum(counter.values())
        logger.info(f"总文件数量: {total_files}")
        for ext, count in counter.items():
            logger.info(f"{ext} 后缀的文件数量: {count}")

    def count_files_dict(self,
            folder_path: str,
            file_extension: Union[str, List[str], Optional[str]] = None,
            recursive: bool = False
        ) -> dict:
        """
        统计指定目录下的文件数量，并以字典形式返回。

        参数:
        - folder_path (str): 要统计文件的目录路径。
        - file_extension (Union[str, List[str], Optional[str]]): 可选参数，指定要统计的文件扩展名。
        可以是单个扩展名的字符串，也可以是包含多个扩展名的列表。如果不提供此参数，将统计所有文件。
        - recursive (bool): 可选参数，指示是否递归统计子目录中的文件。默认为 False，即不递归。

        返回:
        - dict: 一个字典，键为文件扩展名，值为对应扩展名的文件数量。
        """
        counter = Counter()
        if isinstance(file_extension, str):
            file_extension = [file_extension]

        for _, dirs, files in os.walk(folder_path):
            if not recursive:
                dirs.clear()
            for file in files:
                if file_extension is None or any(file.endswith(ext) for ext in file_extension):
                    ext = os.path.splitext(file)[1]
                    counter[ext] += 1

        return dict(counter)
