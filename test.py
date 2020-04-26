from pathlib import Path
DIR_PATH = Path("../mk_web")
FILE_PATH_LIST = list(DIR_PATH.glob("*"))
FILE_NAME_LIST = [str(path).split('/')[-1] for path in FILE_PATH_LIST]

print(FILE_PATH_LIST)
print(FILE_NAME_LIST)