class Node:
    class Bounds:
        __slots__ = [
            "top",
            "bottom",
            "left",
            "right"
        ]

    __slots__ = [
        "x_part",
        "y_part",
        "dx_part",
        "dy_part",
        "bounds",
        "right_child",
        "left_child"
    ]

    def __init__(self):
        self.bounds = {"right": self.Bounds(), "left": self.Bounds()}

class SubSector:
    __slots__ = [
        "seg_count",
        "first_seg"
    ]

class Segment:
    __slots__ = [
        "start_vertex",
        "end_vertex",
        "angle",
        "linedef",
        "direction",
        "offset"
    ]

class Thing:
    __slots__ = [
        "pos",
        "angle",
        "type",
        "flags"
    ]

class Linedef:
    __slots__ = [
        "start_vertex",
        "end_vertex",
        "flags",
        "type",
        "sector_tag",
        "front_sidedef",
        "back_sidedef"
    ]
