from bidict import bidict
from itertools import starmap


Bottom = False
Top = True


class BBD_node:
    def __init__(self) -> None:
        self.L = None
        self.R = None
        self.is_zero_terminal = False
        self.is_one_terminal = False

    @property
    def is_terminal(self):
        return self.is_zero_terminal or self.is_one_terminal

    def __str__(self):
        if self.is_zero_terminal:
            return "ZeroTerminal"
        if self.is_one_terminal:
            return "OneTerminal"
        return "BranchingNode"

def Algo_1(n: int) -> BBD_node: 
    root = BBD_node()
    state = bidict({root : (1, 0, 0, Bottom)})

    ZeroTerminal = BBD_node()
    ZeroTerminal.is_zero_terminal = True
    OneTerminal = BBD_node()
    OneTerminal.is_one_terminal = True

    unprocessed_nodes = [root]

    while unprocessed_nodes:
        v = unprocessed_nodes.pop(0)

        i, hL, hR, F = state[v]
        
        pruned, L_state = compute_L_state(*state[v])
        if pruned or i == 2 or (i == 2*n and L_state[1] != L_state[2]):
            v.L = ZeroTerminal
        elif i == 2*n and L_state[1] == L_state[2]:
            v.L = OneTerminal
        else:
            add_to_bidict(state, L_state, unprocessed_nodes)
            v.L = state.inverse[L_state]
        
        
        pruned, R_state = compute_R_state(*state[v])
        if pruned or i == 1 or (i == 2*n and R_state[1] != R_state[2]):
            v.R = ZeroTerminal
        elif i == 2*n and R_state[1] == R_state[2]:
            v.R = OneTerminal
        else:
            add_to_bidict(state, R_state, unprocessed_nodes)
            v.R = state.inverse[R_state]

    #print(state)

    return root

# returns whether node should be pruned and if not, it's state
def compute_L_state(i, hL, hR, F):
    if i % 2 == 0: # i is even
        if F == Top:
            return hR-1 <= 0, (i+1, hL, hR-1, Top)
        else: # F == Bottom
            if hL - 1 == hR: # Case (i)
                return hR-1 <= 0, (i+1, hL, hR-1, Top)
            else: # Case (ii)
                return False, (i+1, hL, hR-1, Bottom)
    else: # i is odd
        return False, (i+1, hL+1, hR, F)


# same
def compute_R_state(i, hL, hR, F):
    if i % 2 == 0: # i is even
        if F == Top:
            return False, (i+1, hL, hR+1, Top)
        else: # F == Bottom
            if hL - 1 == hR: # Case (i)
                return False, (i+1, hL, hR+1, Bottom)
            else: # Case (ii)
                return True, None
    else: # i is odd
        if hL - 1 <= 0:
            return True, None
        else:
            return False, (i+1, hL-1, hR, F)




def add_to_bidict(the_bidict, key, the_list):
    if key not in the_bidict.inverse:
        node = BBD_node()
        the_bidict[node] = key
        the_list.append(node)

def BBD_DFS(root: BBD_node) -> list:
    out = []
    current_string = []

    def recurse(node: BBD_node):
        if node.is_zero_terminal:
            return
        if node.is_one_terminal:
            out.append("".join(current_string))
            return
        current_string.append("L")
        recurse(node.L)
        current_string.pop()
        current_string.append("R")
        recurse(node.R)
        current_string.pop()

    recurse(root)

    return out

def invert(s: str) -> str:
    s = s.replace("R", "X")
    s = s.replace("L", "R")
    s = s.replace("X", "L")
    return s

# abcdef -> afbecd
def alternate(s: str) -> str:
    n = len(s)//2
    return "".join(starmap(lambda a,b:a+b, zip(s[:n], s[:n-1:-1])))
    # the uglier the code the better lol

# abcdef -> acefdb
def unalternate(s: str) -> str:
    return s[0::2] + s[-1::-2]


def visualize_string(s: str) -> None:
    L, R = -1, -1
    for i in range(len(s)//2):
        L = s.find("L", L+1)
        R = s.find("R", R+1)
        print(" "*L + "[" + "="*(R-L-1) + "]")




import glfw
import OpenGL.GL as gl
import imgui
from imgui.integrations.glfw import GlfwRenderer

def gui_main(state):
    window = impl_glfw_init()
    imgui.create_context()
    impl = GlfwRenderer(window)

    try:
        
        while not glfw.window_should_close(window):
            glfw.poll_events()
            impl.process_inputs()
    
            imgui.new_frame()
            
            try:
                imgui.begin("ZeroTerminal")
                imgui.end()
                imgui.begin("OneTerminal")
                imgui.end()
                

                for node, s in state.items():
                    try:
                        imgui.begin(str(s))
                        imgui.text("L: " + (str(node.L) if node.L.is_terminal else str(state[node.L])))
                        imgui.text("R: " + (str(node.R) if node.R.is_terminal else str(state[node.R])))
                    finally:
                        imgui.end()

            except Exception as e:
                imgui.begin("Error:")
                imgui.text(str(e))
                imgui.end()
            finally:
                pass
    
            gl.glClearColor(.1, .1, .1, 1)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    
            imgui.render()
            impl.render(imgui.get_draw_data())
            glfw.swap_buffers(window)

    finally:
        impl.shutdown()
        glfw.terminate()
        

def impl_glfw_init():
    width, height = 1280, 720
    window_name = "minimal ImGui/GLFW3 example"

    if not glfw.init():
        print("Could not initialize OpenGL context")
        exit(1)

    # OS X supports only forward-compatible core profiles from 3.2
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(
        int(width), int(height), window_name, None, None
    )
    glfw.make_context_current(window)

    if not window:
        glfw.terminate()
        print("Could not initialize Window")
        exit(1)

    return window

from time import time
def time_it(f, *args, **kwargs):
    t = time()
    result = f(*args, **kwargs)
    return result, time() - t


if __name__ == "__main__":
    
    for n in range(18, 100):

        root, bdd_time = time_it(Algo_1, n)
        # strings, dfs_time = time_it(BBD_DFS, root)

        # for s in strings:
        #     visualize_string(unalternate(s))
        #     print(unalternate(s), "<-", s)

        print(f"{n:2} -> {0:9} : {bdd_time:.6f} : {0:.6f}")
        #print(f"{n:2} -> {len(strings):9} : {bdd_time:.6f} : {dfs_time:.6f}")
        #gui_main(state)


        # OEIS: A007123

"""
 n ->   #graphs : algo-t[s] : dfs-t [s]
 --------------------------------------
 1 ->         1 :  0.000000 :  0.000000
 2 ->         1 :  0.000000 :  0.000000
 3 ->         2 :  0.000000 :  0.000000
 4 ->         4 :  0.000000 :  0.000000
 5 ->        10 :  0.001000 :  0.000000
 6 ->        26 :  0.002001 :  0.000000
 7 ->        76 :  0.001001 :  0.000998
 8 ->       232 :  0.002001 :  0.000000
 9 ->       750 :  0.003999 :  0.001000
10 ->      2494 :  0.004001 :  0.004000
11 ->      8524 :  0.004998 :  0.012001
12 ->     29624 :  0.007001 :  0.044944
13 ->    104468 :  0.010002 :  0.158087
14 ->    372308 :  0.011992 :  0.591027
15 ->   1338936 :  0.017000 :  2.179932
16 ->   4850640 :  0.031002 :  8.290824
17 ->  17685270 :  0.074590 : 30.422356
18 ->       n/a :  0.025724 :       n/a
19 ->       n/a :  0.028000 :       n/a
20 ->       n/a :  0.047233 :       n/a
21 ->       n/a :  0.044002 :       n/a
22 ->       n/a :  0.060071 :       n/a
23 ->       n/a :  0.058997 :       n/a
24 ->       n/a :  0.054000 :       n/a
25 ->       n/a :  0.070029 :       n/a
26 ->       n/a :  0.087001 :       n/a
27 ->       n/a :  0.076690 :       n/a
28 ->       n/a :  0.092509 :       n/a
29 ->       n/a :  0.094955 :       n/a
30 ->       n/a :  0.104007 :       n/a
31 ->       n/a :  0.131999 :       n/a
32 ->       n/a :  0.125479 :       n/a
33 ->       n/a :  0.143105 :       n/a
34 ->       n/a :  0.153150 :       n/a
35 ->       n/a :  0.165997 :       n/a
36 ->       n/a :  0.175819 :       n/a
37 ->       n/a :  0.196319 :       n/a
38 ->       n/a :  0.217041 :       n/a
39 ->       n/a :  0.221885 :       n/a
40 ->       n/a :  0.246002 :       n/a
41 ->       n/a :  0.273678 :       n/a
42 ->       n/a :  0.280494 :       n/a
43 ->       n/a :  0.313759 :       n/a
44 ->       n/a :  0.321243 :       n/a
45 ->       n/a :  0.358741 :       n/a
46 ->       n/a :  0.366094 :       n/a
47 ->       n/a :  0.406135 :       n/a
48 ->       n/a :  0.414986 :       n/a
49 ->       n/a :  0.458128 :       n/a
50 ->       n/a :  0.485718 :       n/a
51 ->       n/a :  0.515084 :       n/a
52 ->       n/a :  0.543616 :       n/a
53 ->       n/a :  0.582156 :       n/a
54 ->       n/a :  0.611777 :       n/a
55 ->       n/a :  0.638038 :       n/a
56 ->       n/a :  0.675751 :       n/a
57 ->       n/a :  0.709817 :       n/a
58 ->       n/a :  0.736143 :       n/a
59 ->       n/a :  0.786161 :       n/a
60 ->       n/a :  0.836832 :       n/a
61 ->       n/a :  0.885775 :       n/a
62 ->       n/a :  0.923135 :       n/a
63 ->       n/a :  0.957855 :       n/a
64 ->       n/a :  1.022732 :       n/a
65 ->       n/a :  1.058249 :       n/a
66 ->       n/a :  1.115491 :       n/a
67 ->       n/a :  1.160442 :       n/a
68 ->       n/a :  1.220999 :       n/a
69 ->       n/a :  1.288104 :       n/a
70 ->       n/a :  1.321147 :       n/a
71 ->       n/a :  1.411138 :       n/a
72 ->       n/a :  1.458053 :       n/a
73 ->       n/a :  1.514955 :       n/a
74 ->       n/a :  1.584612 :       n/a
75 ->       n/a :  1.666175 :       n/a
76 ->       n/a :  1.712998 :       n/a
77 ->       n/a :  1.809608 :       n/a
78 ->       n/a :  1.861861 :       n/a
79 ->       n/a :  1.919695 :       n/a
80 ->       n/a :  1.991620 :       n/a
81 ->       n/a :  2.064260 :       n/a
82 ->       n/a :  2.189029 :       n/a
83 ->       n/a :  2.227124 :       n/a
84 ->       n/a :  2.323238 :       n/a
85 ->       n/a :  2.383532 :       n/a
86 ->       n/a :  2.477554 :       n/a
87 ->       n/a :  2.593927 :       n/a
88 ->       n/a :  2.642950 :       n/a
89 ->       n/a :  2.770933 :       n/a
90 ->       n/a :  2.884615 :       n/a
91 ->       n/a :  2.959571 :       n/a
92 ->       n/a :  3.025910 :       n/a
93 ->       n/a :  3.184751 :       n/a
94 ->       n/a :  3.275849 :       n/a
95 ->       n/a :  3.367059 :       n/a
96 ->       n/a :  3.537281 :       n/a
97 ->       n/a :  3.621239 :       n/a
98 ->       n/a :  3.707531 :       n/a
99 ->       n/a :  3.835971 :       n/a
"""