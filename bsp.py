from settings import *

class BSP:
    SUB_SECTOR_ID = 0x8000

    def __init__(self, engine):
        self.engine = engine
        self.player = engine.player
        self.nodes = engine.data.nodes
        self.sub_sectors = engine.data.sub_sectors
        self.segments = engine.data.segments
        self.root_node = len(self.nodes) - 1

    def update(self):
        self.render_node(self.root_node)

    def render_sub_sector(self, sub_sector_id):
        sub_sector = self.sub_sectors[sub_sector_id]

        for i in range(sub_sector.seg_count):
            segment = self.segments[sub_sector.first_seg + i]

            self.engine.renderer.draw_segment(segment, sub_sector_id)

    def render_node(self, node):
        if node >= self.SUB_SECTOR_ID:
            sub_sector = node - self.SUB_SECTOR_ID

            self.render_sub_sector(sub_sector)

            return None

        node = self.nodes[node]

        if self.is_on_back(node):
            self.render_node(node.left_child)
            self.render_node(node.right_child)
        else:
            self.render_node(node.right_child)
            self.render_node(node.left_child)

    def is_on_back(self, node):
        dx = self.player.pos.x - node.x_part
        dy = self.player.pos.y - node.y_part

        return dx * node.dy_part - dy * node.dx_part <= 0
