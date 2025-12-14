class DFA:
    def __init__(self, states, alphabet, transition, start, accept):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.start = start
        self.accept = accept

    def run(self, string):
        state = self.start
        for ch in string:
            state = self.transition[(state, ch)]
        return state in self.accept


states = {0, 1}
alphabet = {'0', '1'}
transition = {
    (0, '0'): 0,
    (0, '1'): 1,
    (1, '0'): 0,
    (1, '1'): 1
}
start = 0
accept = {1}

dfa = DFA(states, alphabet, transition, start, accept)
print(dfa.run("1011"))
