from pathlib import Path
from modules.languages import get_extension
import os.path
from re import sub

# 상위 디렉토리 경로
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


class FileManager(object):
    default_dir = '_downloads'  # 파일을 저장할 기본 디렉토리
    save_cnt = 0  # 파일 저장 카운트

    def __init__(self, *dirs):
        self.dirname = BASE_DIR / self.default_dir / '/'.join(*dirs)
        mkdir_if_not_exists(self.dirname)

    def write_file(self, name, content, language) -> bool:
        basename = remove_win_special_char(name)
        file = self.dirname / ''.join([basename, get_extension(language)])
        if os.path.isfile(file):
            # print(f'이미 존재!: {basename}')
            return False
        else:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            self.save_cnt += 1
        return True

    def get_default_dir_file_list(self):
        return os.listdir(self.dirname)


def mkdir_if_not_exists(path_dir: str):
    while True:
        try:
            if os.path.isdir(path_dir) is False:
                os.mkdir(path_dir)
        except FileNotFoundError:
            mkdir_if_not_exists(
                os.path.abspath(os.path.join(path_dir, os.pardir)))
        else:
            return


def remove_win_special_char(before_str):
    """
    windows에서 파일명으로 사용하지 못하는 특수문자 제거
    :param before_str: 문자열
    :return: 특수문자가 제거된 문자열
    """
    return sub('[\\\/:*?"<>|]', '', before_str)


def get_file_dirname(file_path):
    return os.path.dirname(os.path.abspath(file_path))