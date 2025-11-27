# data_gen_templates/items.py
#
# Copyright (C) 2025 James Petersen <m@jamespetersen.ca>
# Licensed under MIT. See LICENSE

from BaseClasses import ItemClassification
from collections.abc import Mapping
from dataclasses import dataclass
from enum import IntEnum
from typing import Dict, Set

class ItemClass(IntEnum):
    """These are the possible item classes."""
    # TEMPLATE: ITEM_CLASSES
    pass # TEMPLATE: DELETE

@dataclass(frozen=True)
class ItemData:
    label: str
    id: int
    clas: ItemClass
    count: int = 1
    classification: ItemClassification = ItemClassification.filler

    def get_raw_id(self) -> int:
        clas = self.clas
        id = self.id
        if self.count > 1:
            top_bit = id >> 8
            clas += top_bit + 1
            id = id & 0xFF | self.count << 8
        return clas << 12 | id

items: Mapping[str, ItemData] = {
    # TEMPLATE: ITEMS
}

item_groups: Dict[str, Set[str]] = {
    "HM01": {"HM01 Cut"},
    "HM02": {"HM02 Fly"},
    "HM03": {"HM03 Surf"},
    "HM04": {"HM04 Strength"},
    "HM05": {"HM05 Defog"},
    "HM06": {"HM06 Rock Smash"},
    "HM07": {"HM07 Waterfall"},
    "HM08": {"HM08 Rock Climb"},
    # TEMPLATE: ITEM_GROUPS
}
