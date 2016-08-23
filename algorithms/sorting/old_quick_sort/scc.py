s = []
def dfs(g,v):
	global s
	if v in s:
		return

	

	s.append(v)
	if v not in g[v]:
		return
	
	for vertex in g[v]:
	#for each in [x for x in g[v] if x not in s]:
		dfs(g,vertex)
	return s

	

f = open("scc.txt", "r")
A = []
i = 0


for t in f.readlines():
	i = i + 1

graph = [(0,3), (0,2), (1,0), (1,2),(5,7),(6,2)]

def getgraph(graph):
	d = {}
	for test in graph:
		if test[0] in d:
			d[test[0]].append(test[1])
		else:
			l = []
			l.append(test[1])
			d[test[0]] = l
	return d

def getgraph_rev(graph):
	d = {}
	for test in graph:
		if test[1] in d:
			d[test[1]].append(test[0])
		else:
			l = []
			l.append(test[0])
			d[test[1]] = l
	return d


graph1 = { 0 : [1],
          1 : [3, 6],
          3 : [7],
          7 : [5],
          2 : [5, 6],
          5 : [],
          6 : [4],
          4 : []
        }

graph2 = { 0 : [3, 2],
          1 : [0, 2],
          3 : [],
          5 : [7],
          2 : [],
          7 : [],
          6 : [2],
          4 : []
        }
graph = [(0,3), (0,2), (1,0),(1,2),(5,7),(6,2)]
print dfs(getgraph(graph), 1)
print getgraph(graph)
print getgraph_rev(graph)
print dfs(getgraph_rev(graph), 0)
