from wad_reader import WADReader

class WADData:
    INDEXES = {
        "THINGS": 1,
        "LINEDEFS": 2,
        "SIDEDEFS": 3,
        "VERTEXES": 4,
        "SEGS": 5,
        "SSECTORS": 6,
        "NODES": 7,
        "SECTORS": 8,
        "REJECT": 9,
        "BLOCKMAP": 10
    }

    def __init__(self, engine, map):
        self.reader = WADReader(engine.wad)
        self.map_index = self.get_index(map)

        self.vertexes = self.get_data(self.reader.read_vertex, self.map_index + self.INDEXES["VERTEXES"], 4)
        self.linedefs = self.get_data(self.reader.read_linedef, self.map_index + self.INDEXES["LINEDEFS"], 14)
        self.nodes = self.get_data(self.reader.read_node, self.map_index + self.INDEXES["NODES"], 28)
        self.sub_sectors = self.get_data(self.reader.read_sub_sector, self.map_index + self.INDEXES["SSECTORS"], 4)
        self.segments = self.get_data(self.reader.read_segment, self.map_index + self.INDEXES["SEGS"], 12)
        self.things = self.get_data(self.reader.read_thing, self.map_index + self.INDEXES["THINGS"], 10)

        self.reader.close()

    def get_data(self, reader, lump, size, length=0):
        lump_info = self.reader.dir[lump]
        count = lump_info["size"] // size
        data = []

        for i in range(count):
            offset = lump_info["offset"] + i * size + length
            data.append(reader(offset))

        return data

    def get_index(self, lump):
        for index, lump_info in enumerate(self.reader.dir):
            if lump in lump_info.values():
                return index
