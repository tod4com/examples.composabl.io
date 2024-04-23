import os

license_key = os.environ["COMPOSABL_LICENSE"]
PATH: str = os.path.dirname(os.path.realpath(__file__))
PATH_HISTORY: str = f"{PATH}/history"

from sensors import sensors


