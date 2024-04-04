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
        if pruned or (i == 2*n and L_state[1] != L_state[2]):
            v.L = ZeroTerminal
        elif i == 2*n and L_state[1] == L_state[2]:
            v.L = OneTerminal
        else:
            add_to_bidict(state, L_state, unprocessed_nodes)
            v.L = state.inverse[L_state]
        
        
        pruned, R_state = compute_R_state(*state[v])
        if pruned or (i == 2*n and R_state[1] != R_state[2]):
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
            return False, (i+1, hL+1, hR, Top)
        else:
            if hL - 1 == hR: # Case (i)
                return False, (i+1, hL, hR-1, Top)
            else: # Case (ii)
                return False, (i+1, hL, hR-1, Bottom)
    else: # i is odd
        return False, (i+1, hL + 1, hR, F)

# same
def compute_R_state(i, hL, hR, F):
    if i % 2 == 0: # i is even
        if F == Top:
            return False, (i+1, hL, hR+1, Top)
        else:
            if hL - 1 == hR: # Case (i)
                return False, (i+1, hL, hR+1, Bottom)
            else: # Case (ii)
                return True, None
    else: # i is odd
        if hL - 1 <= 0:
            return True, None
        else:
            return False, (i+1, hL - 1, hR, F)





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

    


if __name__ == "__main__":
    strings = BBD_DFS(Algo_1(3))
    # print(alternate("abcdef"))

    for s in strings:
        print(s, "->", unalternate(s), "->", ss := alternate(unalternate(s)))
        assert s == ss