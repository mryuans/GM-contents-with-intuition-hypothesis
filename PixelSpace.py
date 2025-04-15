from manimlib import *


class PixelSpace(ThreeDScene):
    def construct(self):
        title = Text("A Piexl Space in m*n dimensions").set_color(BLACK).scale(0.5).to_corner(UR).fix_in_frame()
        self.add(title)
        axes = ThreeDAxes().set_color(BLACK)
        self.add(axes)

        vec1 = Vector(
            [1, 1, 1]
        ).set_color(BLUE)
        label1 = Matrix([
            ["a_{11}", "a_{12}", r"\cdots", "a_{1n}"],
            ["a_{21}", "a_{22}", r"\cdots", "a_{2n}"],
            [r"\vdots", r"\vdots", r"\ddots", r"\vdots"],
            ["a_{m1}", "a_{m2}", r"\cdots", "a_{mn}"]
        ],
            ellipses_row=-2,
            ellipses_col=-2
        ).next_to(vec1).set_color(BLACK).scale(0.5).fix_in_frame()
        label_name = Text("Pixel matrix").set_color(BLACK).next_to(label1, UP, SMALL_BUFF).fix_in_frame().scale(0.5)
        self.add(vec1, label1, label_name)

        vec2 = Vector(
            [1, -1, 1]
        ).set_color(RED)
        label2 = Matrix([
            ["b_{11}", "b_{12}", r"\cdots", "b_{1n}"],
            ["b_{21}", "b_{22}", r"\cdots", "b_{2n}"],
            [r"\vdots", r"\vdots", r"\ddots", r"\vdots"],
            ["b_{m1}", "b_{m2}", r"\cdots", "b_{mn}"]
        ],
            ellipses_row=-2,
            ellipses_col=-2
        ).next_to(vec1, LEFT).set_color(BLACK).scale(0.5).fix_in_frame()
        label_name_2 = Text("Judge matrix").set_color(BLACK).next_to(label2, UP, SMALL_BUFF).fix_in_frame().scale(0.5)
        self.add(vec2, label2, label_name_2)

