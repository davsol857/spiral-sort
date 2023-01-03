# TODO
# implement start - if you are reading this
# DONT USE START - IT HAS YET TO BE IMPLEMENTED
# better visualization
# simplify

import math


class spiral_sort():
    def __init__(self,
                 points=None,
                 rotation=None,
                 start=None,
                 visualize=False):

        self.points = points
        self.start = start
        self.visualize = visualize

        if rotation == "left":
            self.rotation = self.rotate_left
        else:
            self.rotation = self.rotate_right

    def sort(self) -> list:
        self.create_spiral()

        if self.visualize:
            self.create_visual()

        return self.sorted_points

    def create_spiral(self) -> None:
        if self.start is not None:
            # TODO
            first_point = self.start
        else:
            first_point = min(self.points, key=lambda point: point[1])
            final_points = [(first_point[0], 0), first_point]

        del self.points[self.points.index(first_point)]

        for i in range(len(self.points)):
            angle_point_dict = dict()
            for point in self.points:
                x1, y1 = point
                x2, y2 = final_points[-1]
                x3, y3 = final_points[-2]
                angle1 = (360 + math.degrees(math.atan2(x1-x2, y1-y2))) % 360
                angle2 = (360 + math.degrees(math.atan2(x3-x2, y3-y2))) % 360
                if angle1 <= angle2:
                    angle_point_dict[angle2 - angle1] = point
                else:
                    angle_point_dict[360 - (angle1 - angle2)] = point

            selected_angle = self.rotation(angle_point_dict)
            final_points.append(selected_angle)
            del self.points[self.points.index(selected_angle)]

        self.sorted_points = final_points[1:]

    def rotate_right(self, angle_point_dict):
        return angle_point_dict[max(angle_point_dict)]

    def rotate_left(self, angle_point_dict):
        return angle_point_dict[min(angle_point_dict)]

    def create_visual(self) -> None:
        import tkinter
        width = max(self.sorted_points, key=lambda point: point[0])[0]
        height = max(self.sorted_points, key=lambda point: point[1])[1]

        canvas = tkinter.Canvas(width=width, height=height)
        canvas.pack()

        for point in self.sorted_points:
            canvas.create_oval(point[0]-3,
                               point[1]-3,
                               point[0]+3,
                               point[1]+3,
                               width=0,
                               fill="red")

        canvas.create_line(tuple(self.sorted_points),
                           width=2,
                           fill="green")
