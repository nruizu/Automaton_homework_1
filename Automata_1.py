from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from pyformlang.finite_automaton import State
from pyformlang.finite_automaton import Symbol

dfa = DeterministicFiniteAutomaton()

estado0 = State(0)
estado1 = State(1)
estado2 = State(2)

symb_0 = Symbol("0")
symb_1 = Symbol("1")

dfa.add_start_state(estado0)
dfa.add_final_state(estado0)

dfa.add_transition(estado0, symb_0, estado0)
dfa.add_transition(estado0, symb_1, estado1)
dfa.add_transition(estado1, symb_1, estado0)
dfa.add_transition(estado1, symb_0, estado2)
dfa.add_transition(estado2, symb_1, estado2)
dfa.add_transition(estado2, symb_0, estado1)

numero = input()
print(dfa.accepts(numero))
