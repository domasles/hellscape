from pygame.math import Vector2
from data_types import *

import struct

class WADReader:
    def __init__(self, wad):
        self.wad = open(wad, "rb")
        self.header = self.read_header()
        self.dir = self.read_dir()

    def read_vertex(self, offset):
        x = self.read_2_bytes(offset, "h")
        y = self.read_2_bytes(offset + 2, "h")

        return Vector2(x, y)
    
    def read_linedef(self, offset):
        linedef = Linedef()

        linedef.start_vertex = self.read_2_bytes(offset, "H")
        linedef.end_vertex = self.read_2_bytes(offset + 2, "H")
        linedef.flags = self.read_2_bytes(offset + 4, "H")
        linedef.type = self.read_2_bytes(offset + 6, "H")
        linedef.sector_tag = self.read_2_bytes(offset + 8, "H")
        linedef.front_sidedef = self.read_2_bytes(offset + 10, "H")
        linedef.back_sidedef = self.read_2_bytes(offset + 12, "H")

        return linedef

    def read_header(self):
        return {
            "type": self.read_string(0, 4),
            "num_lumps": self.read_4_bytes(4),
            "init_offset": self.read_4_bytes(8)
        }
    
    def read_dir(self):
        dir = []

        for i in range(self.header["num_lumps"]):
            offset = self.header["init_offset"] + i * 16
            lump_info = {
                "offset": self.read_4_bytes(offset),
                "size": self.read_4_bytes(offset + 4),
                "name": self.read_string(offset + 8, 8)
            }

            dir.append(lump_info)

        return dir

    def read_string(self, offset, size):
        return "".join(b.decode("ascii") for b in self.read_bytes(offset, size, "c" * size) if ord(b) != 0).upper()

    def read_bytes(self, offset, size, format):
        self.wad.seek(offset)
        buffer = self.wad.read(size)

        return struct.unpack(format, buffer)
    
    def read_1_byte(self, offset, format="B"):
        return self.read_bytes(offset, 1, format)[0]
    
    def read_2_bytes(self, offset, format):
        return self.read_bytes(offset, 2, format)[0]
    
    def read_4_bytes(self, offset, format="i"):
        return self.read_bytes(offset, 4, format)[0]

    def close(self):
        self.wad.close()
