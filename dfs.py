from graph import Graph
from vertex import Vertex
from math import inf

def create_graph():
	g = Graph()
	A = Vertex("A")
	g.add_v(A)
	B = Vertex("B")
	g.add_v(B)
	C = Vertex("C")
	g.add_v(C)
	D = Vertex("D")
	g.add_v(D)
	E = Vertex("E")
	g.add_v(E)
	F = Vertex("F")
	g.add_v(F)
	g.add_e(A,B)
	g.add_e(A,C)
	g.add_e(B,C)
	g.add_e(B,D)
	g.add_e(B,F)
	g.add_e(D,E)
	g.add_e(D,F)
	g.add_e(E,F)
	return g,A

g,A = create_graph()