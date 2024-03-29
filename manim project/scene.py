from manim import *

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

        graph = Graph(V, E)

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