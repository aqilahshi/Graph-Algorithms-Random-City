import random
import datetime 
import time


#This class represents a directed graph using adjacency list representation
class Graph:

    # Dictionary for default graph
    graph_dict = {'AD':{'LD':357},
            'LD':{'SE':8859},
            'SE':{'TR':6652},
            'TR':{},
            'VN':{'TR':3180,'AD':936}}

# ------ BASIC FUNCTIONS
    
    #constructor
    def __init__(self,vertices, edges):
        self.V= vertices #Number of vertices
        self.graph = {} #default dictionary to store graph
        self.costs = {}
        
        #allocate memory for adjacency list
        for edge in edges:
            self.graph[edge] = []
            
    #print default graph
    def printDGraph(G):
        print(G.graph_dict)
        
    #print current graph
    def digraph(g):
        print(g.graph) 
        print("\n")
        print(g.costs)

    
    # function to add an edge to graph
    def add_Edge(self,u,v,cost):
        self.graph[u].append(v)
        self.costs[(u,v)] = cost
        
    # function to delete edges
    def delete_Edge(self,u,v,cost):
        temp = [v,cost]
        if temp in self.graph[u]:
            self.graph[u].remove(temp)
   
    # function to create random edge
    def random_edge(self, edges):
        cond = True
        while cond:
            #in funtion is return false
            found = False
            #generate random edge
            ran_Edges = random.choice(edges)
            for i in self.graph:
                for j in self.graph[i]:
                    if ran_Edges[0] == i and ran_Edges[1] == j:
                        found = True          
            if found == False:
                cond = False
        self.add_Edge(ran_Edges[0],ran_Edges[1],ran_Edges[2])
        
    
     
# ------ Function 1: Check if the graph is strongly connected by AQILAH SYAHIRAH  
    #  function to perform DFS
    def DFS(self, u, visited, stack, act):
        
        # mark the visited vertex
        visited[u] = "true"
        
        #recursive for all the vertices adjacent to this vertex
        for v in act[u]:
            if visited[v] == "false":
                repeat = self.DFS(v, visited, stack, act)
                if repeat == True:
                    return True
            elif visited[v]== "true":
                return True
        visited[u]= "false1"
        return False
         
    # The main function that returns true if graph is strongly connected
    def strongConnect(self):
        act = self.graph
        visited = {}
        stack = {}
        
        # mark ALL not visited vertex
        for u in act.keys():
            visited[u]= "false"
            stack[u]=None
            
        # perform DFS from first vertex
        for u in act.keys():
            if visited[u] == "false":
                repeat = self.DFS(u, visited, stack, act)
        
        # return false if first DFS does not visit all vertices
        for b in visited.keys():
            if visited[b] != "true":
                return False
        return True
    
# ------ Function 2: Check if the graph has a cycle by SITI SAKINAH 
    #function to trace the cycle of a graph using DFS
    def algoCycle(self, i, visited, route):
        #set the visited vertex and its route as TRUE
        visited[i] =True 
        route[i] =True  
        
        #find nearby vertex 
        nearby = self.graph[i]
        for m in range(len(nearby)):
            now =nearby[m]  
            if route[now]== True: #the route is already visited. it has a cycle.
                return True 
            if visited[now]== False:  #find another route. perform again the algorithm.
                doing=self.algoCycle(now,visited,route)
                if doing==True: #check again if the route is already visited. it has a cycle.
                    return True 
                
        route[i]=False #if the route cannot execute in the if statement
        return False
    
    #function to detect the graph's cycle (boolean)
    def detectCycle(self): 
        act=self.graph.keys() 
        visited = {}
        route = {} 
        
        for i in act: #initialize the variables
            visited[i]= False 
            route[i] = False 
        
        for i in act: 
            doing = self.algoCycle(i,visited,route) #perform algorithm to detect cycle
            if doing ==True: #if algoritm return true. cycle detect.
                return True 
        return False #acyclic

        
# ------ Function 3: Select two vertices and compute the shortest path between the vertices by TEOH SIN YEE   
    def dijkstra(self,graph_dict,start,goal): 
        shortest_distance = {}
        predecessor = {}
        unseenNodes = graph_dict
        infinity = 9999999
        path = []
        for node in unseenNodes:
            shortest_distance[node] = infinity
        shortest_distance[start] = 0
     
        while unseenNodes:
            minNode = None
            for node in unseenNodes:
                if minNode is None:
                    minNode = node
                elif shortest_distance[node] < shortest_distance[minNode]:
                    minNode = node
     
            for childNode, weight in graph_dict[minNode].items():
                if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                    shortest_distance[childNode] = weight + shortest_distance[minNode]
                    predecessor[childNode] = minNode
            unseenNodes.pop(minNode)
     
        currentNode = goal
        while currentNode != start:
            try:
                path.insert(0,currentNode)
                currentNode = predecessor[currentNode]
            except KeyError:
                print('Path not reachable')
                break
        path.insert(0,start)
        if shortest_distance[goal] != infinity:
            print("\nRESULT......")
            print('Shortest distance is ' + str(shortest_distance[goal]))
            print('And the path is ' + str(path))
        time.sleep(8)   
   
# ----- MAIN FUNCTION

if __name__ == '__main__':
    
    graph_dict =[('AD','LD',357),
                ('LD','SE',8859),
                ('SE','TR',6652),
                ('VN','TR',3180),
                ( 'VN','AD',936)]
                 
    capital = ["LD","AD","VN", "TR", "SE"]
    
    capitalsCost = [("LD","AD", 357),
                     ("LD","VN",1235),
                     ("LD","TR",4400),
                     ("LD","SE",8859),
                     ("AD","LD",357),
                     ("AD","VN", 936),
                     ("AD","TR",4067),
                     ("AD","SE",8557),
                     ("VN","LD", 1235),
                     ("VN","AD",936),
                     ("VN","TR", 3180),
                     ("VN","SE",8276),
                     ("TR","LD",4400),
                     ("TR","AD",4067),
                     ("TR","VN",3180),
                     ("TR","SE",6552),
                     ("SE","LD",8859),
                     ("SE","AD",8557),
                     ("SE","VN",8276),
                     ("SE","TR",65526)]
        
    currentDT = datetime.datetime.now()
    print ("\n",currentDT.strftime("%a-%Y-%m-%d %H:%M:%S"))
    
     
    while(True):
            
        print("\nGraph Algorithm ")
        print("_______________\n")
        
        ver=5
        
        g1 = Graph(ver,capital) #create 5 edges
        
        
        print ("Auto-generated graph......")
        print("\n")
        
        # #print default graph
        g1.printDGraph()
    
        print("\n1. Check if the graph is strongly connected ")
        print("2. Check if the graph has a cycle")
        print("3. Compute the shortest path between the 2 vertices")
        print("4. Exit");
        choice= int(input (">Enter choice :") )
    
        if choice==1: # Check if the graph is strongly connected
                   
            if g1.strongConnect() == True:
                print ("The graph is strongly connected") 
            else: 
                 while g1.strongConnect()==False:
                     g1.random_edge(capitalsCost)
                     if g1.strongConnect() == True:
                         print("The graph is strongly connected.")
                         g1.digraph()
            
                   
        elif choice==2:  # Check if the graph has a cycle
            if g1.detectCycle():
                print ("The graph has a cycle")
            else:
                while g1.detectCycle()==False: 
                     g1.random_edge(capitalsCost) #generate random edges
                     # print(g1.random_edge(capitalsCost))
                     if g1.detectCycle() == True:
                         print ("The graph has a cycle")
                         g1.digraph()
            
        elif choice==3: #Compute the shortest path between the 2 vertices
            
            print("\nAvailable vertices:")
            print(list(g1.graph_dict.keys()))
            
            v1 = input("Starting vertex: ")
            v2 = input("Ending vertex:")
            
            g1.dijkstra(g1.graph_dict,v1,v2)
           
    
        elif choice==4: #exit
            break
    
        else:  
            print("\nInvalid choice. Enter 1-4.")
            
    # --- END ----
         