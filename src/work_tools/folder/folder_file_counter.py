import os
from collections import Counter
from typing import List, Optional, Union

from loguru import logger


class FileCounter:
    def __init__(self) -> None:
        pass 

    def count_files(self, 
        folder_path: str, 
        file_extension: Union[str, List[str], Optional[str]] = None, 
        recursive: bool = False
    ) -> None:
        counter = Counter()
        if isinstance(file_extension, str):
            file_extension = [file_extension]

        for root, dirs, files in os.walk(folder_path):
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