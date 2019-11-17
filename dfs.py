from graph import Graph
from vertex import Vertex
from math import inf

global time
time = None

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

def DFS(g):
    for v in g.vertices:
        v.color = "white"
        v.pre = None
    global time
    time = 0
    for v in g.vertices:
        if v.color == "white":
            DFS_Visit(g,v)

def DFS_Visit(g,v):
    global time
    time = time + 1
    v.d = time
    v.color = "gray"
    for u in g.adjacents(v):
        if u.color == "white":
            u.pre = v
            DFS_Visit(g,u)
    v.color = "black"
    time = time + 1
    v.f = time

DFS(g)  #Starts from first vertex in g.vertices

for v in g.vertices:
    print(v.name,v.d,v.f)   #Prints the vertex name, discovery time, finish time