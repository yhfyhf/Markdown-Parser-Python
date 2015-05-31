# -*- encoding: utf-8 -*-


class ItemTypeError(Exception):

    def __init__(self, item_type):
        self.item_type = item_type

    def __str__(self):
        return "%s type item should not exist here." % self.item_type
