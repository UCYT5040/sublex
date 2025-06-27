from .http import HTTP
from .url import URL
from .json import JSON

class Interface: # To allow communication between Lua and Sublex
    URL = URL

    def __init__(self, sbx) -> None:
        self.sbx = sbx
        self.JSON = JSON(sbx)
        self.HTTP = HTTP(sbx)