from manimlib import *


class PixelDot(Scene):
    def random_color(self):
        return Color(hsl=(np.random.random(), 0.7, 0.65))
    def construct(self):
        axes = NumberPlane()
        def func(p):
            p = np.array(p)
            x, y = p.T
            dx = -x
            dy = -y
            vec = np.column_stack([dx, dy])
            return vec
        
        field = VectorField(func, axes)
        # self.add(field) If you want to add a score function here, please uncomment this line.
        points_num = 100
        step_scale = 0.05

        particles = VGroup(*[
            Dot(radius=0.05).set_color(self.random_color()) 
            for _ in range(points_num)
        ])
        paths = VGroup(*[
            VMobject().set_stroke(color=particle.get_color(), width=2, opacity=0.7)
            for particle in particles
        ])

        self.add(particles, paths)
        
        def update_system(mobs, dt):
            for particle, path in zip(particles, paths):
                dx = np.random.normal(0, step_scale) 
                dy = np.random.normal(0, step_scale)
                particle.shift(dx*RIGHT + dy*UP)
                if len(path.get_all_points()) == 0:
                    path.start_new_path(particle.get_center())
                else:
                    path.add_line_to(particle.get_center()).set_stroke(width=1.2)
        particles.add_updater(update_system)
        self.wait(15)
        particles.remove_updater(update_system)
