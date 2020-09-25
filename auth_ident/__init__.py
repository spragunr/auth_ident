import os


TRAIN_LEN = 1000000  # 1e6
VAL_LEN = 50000
TEST_LEN = 50000
DATA_SIZE = TRAIN_LEN + VAL_LEN + TEST_LEN

os.environ["TF_KERAS"] = '1' 

from auth_ident.generic_execute import GenericExecute
