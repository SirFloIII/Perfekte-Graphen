from manim import *
from RecognizingTriangulatedGraphs import GraphWithAdj, pick_maximal_unnumbered_vertex


class ExampleImperfectGraph(Scene):
    def construct(self):
        V = [1, 2, 3, 4, 5, 6]
        E = [
            (1, 2),
            (2, 3),
            (1, 3),
            (1, 4),
            (2, 5),
            (3, 6),
            (4, 5),
            (5, 6),
            #(4, 6),
            ]

        graph = Graph(V, E,
                    layout = "spring",
                    vertex_type=Dot,
                    vertex_config={"radius" : 0.15},
                    )

        text1 = MathTex(r"{{\omega(G) = 3}}").shift(3*DOWN)
        text2 = MathTex(r"{{\omega(G) = 3}}= \chi(G)").shift(3*DOWN)
        text3 = MathTex(r"{{\omega(G') = 2}}").shift(3*DOWN)
        text4 = MathTex(r"{{\omega(G') = 2}}\neq 3 = \chi(G')").shift(3*DOWN)

        self.play(Create(graph))

        self.wait(1)

        self.play(Indicate(graph.vertices[1]),
                  Indicate(graph.vertices[2]),
                  Indicate(graph.vertices[3]),
                  Indicate(graph.edges[(1, 2)]),
                  Indicate(graph.edges[(2, 3)]),
                  Indicate(graph.edges[(1, 3)]),
                  FadeIn(text1)
        )

        self.wait(1)

        self.play(graph.vertices[1].animate.set_color(RED),
                  graph.vertices[2].animate.set_color(GREEN),
                  graph.vertices[3].animate.set_color(BLUE),
        )
        
        self.play(graph.vertices[4].animate.set_color(BLUE),
                  graph.vertices[5].animate.set_color(RED),
                  graph.vertices[6].animate.set_color(GREEN),
        )

        self.play(TransformMatchingTex(text1, text2))

        self.wait(1)

        self.play(FadeOut(text2))

        self.play(graph.vertices[1].animate.set_color(WHITE),
                  graph.vertices[2].animate.set_color(WHITE),
                  graph.vertices[3].animate.set_color(WHITE),
                  graph.vertices[4].animate.set_color(WHITE),
                  graph.vertices[5].animate.set_color(WHITE),
                  graph.vertices[6].animate.set_color(WHITE),
        )

        self.play(FadeOut(graph.remove_vertices(2)))

        self.wait(1)

        self.play(Indicate(graph.vertices[4]),
                  Indicate(graph.vertices[5]),
                  Indicate(graph.edges[(4, 5)]),
                  FadeIn(text3),
        )

        self.wait(1)

        self.play(graph.vertices[1].animate.set_color(RED),
                  graph.vertices[3].animate.set_color(GREEN),
                  graph.vertices[4].animate.set_color(GREEN),
                  graph.vertices[5].animate.set_color(RED),
                  graph.vertices[6].animate.set_color(BLUE),
        )

        self.play(TransformMatchingTex(text3, text4))

        self.wait(1)
        self.play(FadeOut(graph, text4))

class RecognizingTriangulatedGraphs(Scene):
    def construct(self):
        self.build_code_block()

        self.wait(1)

        a = "a"
        b = "b"
        c = "c"
        d = "d"
        e = "e"
        f = "f"
        g = "g"

        G = GraphWithAdj([a, b, c, d, e, f, g],
                    [
                        (a, b),
                        (b, c),
                        (c, d),
                        (e, f),
                        (f, g),
                        (a, e),
                        (b, e),
                        (b, f),
                        (c, f),
                        (c, g),
                        (d, g),
                    ],
                    layout = "kamada_kawai",
                    layout_scale = 9,
                    vertex_config={"radius" : 0.15},
                    ).shift(2*DOWN + 2*RIGHT)

        self.play(Create(G))
        
        label_anim = {v : MathTex(v).scale(0.8).next_to(G.vertices[v], 0.4*UR * (-1 if v in "efg" else 1)) for v in G.vertices}
        
        self.play(*[FadeIn(t) for t in label_anim.values()])

        self.prev_line = 1

        ### line 2
        self.highlight(1)
        label = {v : [] for v in G.vertices}
        for v in label_anim.keys():
            t = label_anim[v]
            new_t = MathTex("{{"+v+"}}" + "{{: [}}{{]}}").scale(0.8).next_to(G.vertices[v], 0.4*UR * (-1 if v in "efg" else 1))
            self.play(TransformMatchingTex(t, new_t), run_time = 0.2)
            label_anim[v] = new_t

        ### line 3
        self.highlight(2)
        order = []
        order_anim = MathTex(r"{{order = [}}{{]}}").shift(DOWN*1 + LEFT*4)
        self.play(Create(order_anim))


        ### line 4
        self.highlight(3)
        for i in range(len(G.vertices), 0, -1):
            i_anim = MathTex(r"{{i = }}"+str(i)).shift(DOWN*2 + LEFT*4)
            if i == len(G.vertices):
                self.play(Create(i_anim))
                i_anim_old = i_anim
            else:
                self.play(Transform(i_anim_old, i_anim))
            
            ### line 5
            self.highlight(4)
            v = pick_maximal_unnumbered_vertex(label, order)
            self.play(G.vertices[v].animate.set_fill(GREEN))

            ### line 6
            self.highlight(5)
            order.append(v)
            order_anim_new = MathTex(r"{{order = [}}{{"+"}},{{".join(order)+"}}{{]}}").shift(DOWN*1 + LEFT*4)
            self.play(TransformMatchingTex(order_anim, order_anim_new))
            order_anim = order_anim_new

            ### line 7
            self.highlight(6)
            for w in G.adj(v):
                self.play(Indicate(G.vertices[w]))


                ### line 8
                self.highlight(7)
                label[w].append(i)
                t = label_anim[w]
                new_t = MathTex("{{"+w+"}}" + "{{: [}}"+"{{,}}".join(map(str, label[w]))+"{{]}}").scale(0.8).next_to(G.vertices[w], 0.4*UR * (-1 if w in "efg" else 1))
                self.play(TransformMatchingTex(t, new_t), run_time = 0.2)
                label_anim[w] = new_t

            self.play(G.vertices[v].animate.set_fill(GRAY))

        

        ### line 9
        #return reversed(order)
        self.highlight(8)
        self.play(FadeOut(i_anim_old)
        )
        order_anim_new = MathTex(r"{{return [}}{{"+"}},{{".join(reversed(order))+"}}{{]}}").shift(DOWN*2 + LEFT*4)
        self.play(TransformMatchingTex(order_anim, order_anim_new))
        order_anim = order_anim_new

        self.wait(5)

        for v in reversed(order):
            self.play(
                    *(Indicate(G.vertices[w]) for w in G.adj(v)),
                    FadeOut(label_anim[v]),
                    FadeOut(G.remove_vertices(v)),
                    )

        self.wait(10)
    
    def build_code_block(self):
        # build the code block
        code = Code(code = """
def Lex_BFS(G: Graph) -> list:
    label = {v : [] for v in G.vertices}
    order = []
    for i in range(len(G.vertices), 0, -1):
        v = pick_maximal_unnumbered_vertex(label, order)
        order.append(v)
        for w in G.adj(v):
            label[w].append(i)
    return reversed(order)""",
                    font="Consolas",
                    language="Python",
                    style="monokai"
                   ).shift(2*UP + LEFT)
        self.play(FadeIn(code))
        # build sliding windows (SurroundingRectangle)
        self.sliding_wins = VGroup()
        height = code.code[0].height
        for line in code.code:
            self.sliding_wins.add(
                SurroundingRectangle(line)
                .set_fill(YELLOW)
                .set_opacity(0)
                .stretch_to_fit_width(code.background_mobject.get_width())
                .align_to(code.background_mobject, LEFT)
            )

        self.add(self.sliding_wins)
        return code

    def highlight(self, line):
        self.play(self.sliding_wins[self.prev_line].animate.set_opacity(0.3))
        self.play(ReplacementTransform(self.sliding_wins[self.prev_line], self.sliding_wins[line]))
        self.play(self.sliding_wins[line].animate.set_opacity(0.3))
        self.prev_line = line


from kawahara import Algo_1, collect


class Kawahara(Scene):
    def construct(self):
        
        n = 6

        root = Algo_1(n)

        V, E = collect(root)

        mobj_from_V = {}

        for node in V:
            text = Text(str(node), font_size=18)
            mobj = RoundedRectangle(corner_radius=0.15, height=0.3, width=1.2, fill_color=LOGO_BLACK, fill_opacity=1.0)
            text.move_to(mobj)
            mobj.add(text)
            text.z_index = 0
            mobj.z_index = 0
            mobj_from_V[node] = mobj

        offset = 4
        spacing = 3.2/n

        for i in range(1, 2*n+1):
            VGroup(*[mobj_from_V[node] for node in V if not node.is_terminal and node.state[0] == i]).arrange().set_y(offset-spacing*i)

        # VGroup(*[mobj_from_V[node] for node in V if node.is_terminal]).arrange().set_y(offset-spacing*(2*n+1))
        
        VGroup(*[mobj_from_V[node] for node in V if node.is_zero_terminal]).set_y(0).set_x(5)
        VGroup(*[mobj_from_V[node] for node in V if node.is_one_terminal]).arrange().set_y(offset-spacing*(2*n+1))



        L_arrows = {}
        R_arrows = {}
        
        for node, mobj in mobj_from_V.items():
            if node.is_terminal:
                continue
            for child, color, zerocolor, arrows, offset in [(node.L, RED, rgb_to_color((158, 60, 53)), L_arrows, -0.3), (node.R, GREEN, GREEN_E, R_arrows, 0.3)]:
                arrow = Arrow(stroke_width=4, max_stroke_width_to_length_ratio=100)
                arrow.put_start_and_end_on(mobj.get_center()+DOWN*0.15+RIGHT*offset, mobj_from_V[child].get_center()+UP*0.15)
                arrow.set_color(zerocolor if child.is_zero_terminal else color)
                arrows[node] = arrow

        
        for node, mobj in mobj_from_V.items():
            if not node.is_terminal:
                self.add(L_arrows[node])
                self.add(R_arrows[node])
        for node, mobj in mobj_from_V.items():
            self.add(mobj)

        self.add(Text("L", color=RED).move_to(UP*3 + LEFT*5))
        self.add(Text("R", color=GREEN).move_to(UP*3 + RIGHT*5))

        