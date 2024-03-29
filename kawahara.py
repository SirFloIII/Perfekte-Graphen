from bidict import bidict


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

    print(state)

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

if __name__ == "__main__":
    Algo_1(2)