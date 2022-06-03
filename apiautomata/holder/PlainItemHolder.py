from typing import Optional

from apiautomata.holder.PlainItem import PlainItem


class PlainItemHolder:
    __instance: Optional[PlainItem] = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = PlainItem()
        return cls.__instance

    @staticmethod
    def get(name):
        return PlainItemHolder.__instance.get(name)
