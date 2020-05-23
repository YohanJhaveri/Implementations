class NFA:
    def __init__(self, transition, start, final):
        self.transition = transition
        self.start = start
        self.final = final

    def run_recursively(self, string):
        def recurse(current, i):
            if i == len(string):
                return current in self.final
            states = self.transition[current].get(string[i], []) + self.transition[current].get('_', [])
            for state in states:
                return False or recurse(state, i + 1)

        return recurse(self.start, 0)

    def run(self, string):
        possible = [set() for i in range(len(string) + 1)]
        possible[0] = {self.start}.union(set(self.transition[self.start].get('_', [])))
        for i, symbol in enumerate(string):
            if string == '0110': print(possible[i])

            for state in possible[i]:
                possible[i + 1] = possible[i + 1].union(set(self.transition[state].get(string[i], [])))

            for state in possible[i + 1]:
                possible[i + 1] = possible[i + 1].union(set(self.transition[state].get('_', [])))

        return set(possible[len(string)]).intersection(set(self.final)) != set()

    def convert_to_DFA():
        

class DFA:
    def __init__(self, transition, start, final):
        self.transition = transition
        self.start = start
        self.final = final

    def run(self, string):
        state = self.start
        for symbol in string:
            state = self.transition[state][symbol]
        return state in self.final

transition = {
    'A': {
        '0': 'B',
        '1': 'A'
    },

    'B':{
        '0': 'B',
        '1': 'C'
    },

    'C':{
        '0': 'B',
        '1': 'A'
    }
}

dfa = DFA(transition, 'A', ['C'])
print(dfa.run('010'))
print(dfa.run('1010'))
print(dfa.run('0110'))
print(dfa.run('0101'))
print(dfa.run('01011'))
print(dfa.run('010010'))
print(dfa.run('0101101'))

transition = {
    'A': {
        '0': ['A'],
        '1': ['A', 'B']
    },

    'B':{
        '0': ['C'],
        '_': ['C']
    },

    'C':{
        '1': ['D']
    },

    'D':{
        '0': ['D'],
        '1': ['D']
    },
}

nfa = NFA(transition, 'A', ['D'])
print(nfa.run('010'))
print(nfa.run('101'))
print(nfa.run('0110'))
print(nfa.run('0101'))
print(nfa.run('01'))
print(nfa.run('010010'))
print(nfa.run('0101101'))
