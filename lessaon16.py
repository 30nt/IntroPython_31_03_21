# полиморфизм

# v_1 = "1."
# v_2 = "2."
# test_1 = v_1 + v_2
# print(test_1, type(v_2))

class Bbox:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def __repr__(self):
        return f"[({self.x0}, {self.y0}), ({self.x1}, {self.y1})]"

    def _get_area(self):
        return (self.x1 - self.x0) * (self.y1 - self.y0)

    def union(self, other):
        new_x0 = min(self.x0, other.x0)
        new_y0 = min(self.y0, other.y0)
        new_x1 = max(self.x1, other.x1)
        new_y1 = max(self.y1, other.y1)
        return Bbox(new_x0, new_y0, new_x1, new_y1)

    def __add__(self, other):
        new_x0 = min(self.x0, other.x0)
        new_y0 = min(self.y0, other.y0)
        new_x1 = max(self.x1, other.x1)
        new_y1 = max(self.y1, other.y1)
        return Bbox(new_x0, new_y0, new_x1, new_y1)

    def __eq__(self, other):
        return self.x0 == other.x0 and self.y0 == other.y0 and self.x1 == other.x1 and self.y1 == other.y1

    def __lt__(self, other):
        return self._get_area() < other._get_area()

bboxes = [Bbox(1,1,2,12), Bbox(1,1,2,2), Bbox(1,1,2,10)]
# bbox_test = Bbox(1,1,2,2)
# res = []
# for bbox in bboxes:
#     if bbox == bbox_test:
#         res.append(bbox)
# print(res)
# print(bboxes[0] >= bboxes[1])
sort_bboxes = sorted(bboxes)
print(sort_bboxes)





# bbox_1 = Bbox(7,1,8,24)
# bbox_2 = Bbox(7,1,8,24)
# bbox_3 = bbox_1 + bbox_2
# print(bbox_3)