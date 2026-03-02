from manim import *


class SuvatGraph(Scene):
    def construct(self):

        x_min, x_max, x_step = 0, 10, 1
        y_min, y_max, y_step = 0, 20, 2

        axes = Axes(x_range=[x_min, x_max + x_step, x_step], y_range=[y_min, y_max + y_step, y_step],
                    x_axis_config={"numbers_to_include": range(x_min, x_max + x_step, x_step)},
                    y_axis_config={"numbers_to_include": range(y_min, y_max + y_step, y_step)})
        self.add(axes)

        x_label = axes.get_x_axis_label(r"time \, \mathrm{s}")       
        y_label = axes.get_y_axis_label(r"v\, \mathrm{m\,s^{-1}}")  

        # v = u + at <--- Formula we are using to calculate stuff
        u = 0 #! Initial Velocity
        a = 2 #! Acceleration
        t = ValueTracker(0)

        acceleration = MathTex("a=2 ms^{-2}").next_to(axes, UP)
        # v = u + a*t

        dot = always_redraw(lambda: Dot(axes.c2p(t.get_value(), u + a*t.get_value()), color=YELLOW))
        self.add(dot)

        # x = [float(t) for t in range(0, 11)]
        # y = [float(u + a*t) for t in range(0, 11)]

        # line = axes.plot_line_graph(x,y,add_vertex_dots=False, line_color=RED)
        self.add(axes, x_label, y_label)

        new_line = always_redraw(lambda: Line(start=axes.c2p(0,u), end=axes.c2p(t.get_value(), u + a*t.get_value()), color=RED))

        # area = always_redraw(lambda: axes.get_area(lambda t: u+a*t, x_range=[0, t.get_value()], color=BLUE, opacity=0.5))
      
        self.play(Create(new_line))
        self.play(Create(acceleration))
        self.wait()

        self.play(t.animate.set_value(10), run_time=5, rate_func=smooth)

        

        #! Area

        t2 = ValueTracker()

        nonvisibleDot = always_redraw(lambda: Dot(axes.c2p(t.get_value(), u + a*t2.get_value()), color=YELLOW,fill_opacity=0))
        self.add(nonvisibleDot)

        graph = axes.plot(lambda t2: u + a*t2, x_range=[0, 20], color=RED)
        area = always_redraw(
        lambda: axes.get_area(
            graph,                    
            x_range=[0, t2.get_value()],
            color=YELLOW,
            opacity=0.3
        )
    )
        
        area_label = always_redraw(
        lambda: MathTex(
             r"\mathbf{s = " + f"{u*t2.get_value() + 0.5*a*t2.get_value()**2:.1f}m" + "}", 
        )
        .move_to(area.get_center() + RIGHT*0.4) 
        .scale(0.7)
)
    
        self.add(area,area_label)

        self.play(t2.animate.set_value(10), run_time=5, rate_func=smooth)
        self.wait()

        formula = MathTex("s = vt").move_to(area.get_center() + RIGHT*2.1 + DOWN*2).scale(1)
 
        self.play(Create(formula))
        self.wait()
        self.wait()
