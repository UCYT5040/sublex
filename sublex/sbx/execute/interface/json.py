from json import loads, dumps

class JSON:
    def __init__(self, sbx) -> None:
        self.sbx = sbx


    def decode(self, data: str) -> dict:
        return self.sbx["lua"].table_from(loads(data))

    @staticmethod
    def encode(data: dict) -> str:
        return dumps(data, indent=4, ensure_ascii=False)