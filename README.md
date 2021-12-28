# Ex4_Graphs-IN-Python
* Written by Guy Azoulay and Yahalom Chasid.

## Main goal of the Project

In this assignment we asked to build a graph from zero, but in this time, in Python.
The main goal of this project is a good and deep understanding of the graph's world, and deal with a code skelaton by yourself,
thankes to this assigment we improved our coding skills and started to really understand what is to "think outside of a box".
Another goal of this project is to create comperation between the same assigment but in different languges, in our case, Java and Python.
At first it was a little bit confusing how different the implementation between this two.
For example, when we coded in java we had to think about every little detail like in which data structure is the best to use in, how to get the specific value from a specific 
position, it was a little bit discouraging, until we started doing the but i python.
In python , for our opinion, it was much more easy, the dict struct is very helpful and comfortable for use.

In this assigment we implement classes such as Graph and graph algorithms such as:  
* Center
* TSP
* Dijkstra
* And a GUI interface of graph drawing using MatPlotLib


## Explanation about the Class:
 
 ## The Directed Weighted Graph class
The main purpose of this class is to demonstarte how a graph is really look like.
We desided not to implement a class of nodes and edges like in the last assigment, in the Graph constructor we created two
dicts(but in aim to initialize the graph we give it two lists in the json files) , one for nodes and one for edges, and with them we implemented all the other functions.

The main veriables which we use in this class are:
  - nodes (dict type)
    - here we held all our nodes using the uniqe ids and position
  - edges (dict type)
    - here we held all our edges using three variables:
      - src : what is the node id i came from
      - dest : what is the node id i go to
      - w: what is the "weight" of this edge

|Main Functions|Explenation|RunTime|
|---|---|---|
|DiGraph constructor | The main constuctor of new Graph, here we initialize the nodes dict and the edges dict |O(1)
|get_all_v| return as a dict all the node in the graph |O(1)
|all_out_edges_of_node| return a dict of all the edges which go out from a given node |O(1)
|all_in_edges_of_node| return a dict of all the edges which in to a given node |O(1)
|add_node| adding a new node to our data structure(if his id exsist)|O(1)
|add_edge| create new edge in the graph|O(1)
|remove_node| in this function we removing a node from our graph, we need to find the givven id delete the edge go from it and into it|O(E)
|remove_edge| here we remove an edge from our graph|O(1)
|v_size| gives us the amount of nodes in our graph|O(1)
|e_size| gives us the number of edges in the graph|O(1)


## The GraphAlgo class
The main purpose of this class is to implement known graph algorythms on the graph we was created.
We liked this part because we did the same thing in java but in more complicated and long way,
and now we really apply the approch of KIS- Keep It Simple

The main veriables which we use in this class are:
  * graph (which is a DiGraph type)
    * here we have all of the graph information we built earlier.
    
|Main Functions|Explenation|RunTime|
|---|---|---|
|GraphAlgo constructor | The main constuctor of the Graph's algorythms, using the DiGraph class|O(1)|
|get_graph| getting the graph information|O(1)|
|isConnected| this function check if a graph is strongly connected using the DFS method and the Kosaraju algorythm, this function is Boolean and we implement it in aim to solve the center algo |O(V +V*(V+E))|
|shortestpath| in this function i have used in the Dijkstra algorythm, at first we update al the nodes "weight" to inf execept the src node which we update to 0, we ran on all the nodes and update their weight to the min, and also saved the prev node of each node in the shortest path in aim to return the list of nodes we walk in |O(V^2 +E)|
|center| in the center function we find the center of a graph (if it connected) using the shortestPathDist, for each node we check the max path to other node and take the maximum one, than we returned the shortest path between all of the nodes maximum path and take his node | O(V^4)
|TSP| in a given list of cities we need to find the shortest path which contain all of them and the weight of it|O(n^4)
|load_from_json| this function loads the json file to our project|O(V+E)|
|save_to_json| saving the file of the graph|O(V+E) 


## Graph Functions Examples:

![WhatsApp Image 2021-12-27 at 19 46 36](https://user-images.githubusercontent.com/87694635/147495779-4010019c-998c-4776-8dbe-8635b00274a1.jpeg)
![WhatsApp Image 2021-12-27 at 19 46 40](https://user-images.githubusercontent.com/87694635/147495778-668657b1-e65e-4010-bc63-d7bd9d5b2f8b.jpeg)
![WhatsApp Image 2021-12-27 at 19 46 59](https://user-images.githubusercontent.com/87694635/147495777-70696024-4b14-4179-ac32-c15a49a5e4a2.jpeg)
![WhatsApp Image 2021-12-27 at 19 47 10](https://user-images.githubusercontent.com/87694635/147495775-37c51dbc-1b41-481d-bf08-849d479bf18d.jpeg)

### Jave Vs Python

After we did the same work in Java and in Python we got some interesting conclusions.
When we did the project in java, a simple function could take us three times or maybe more raws of code (compared to Python).
But in this project we understood that the amout of lines isn't a factor in coding languges, there are many othe factor such as
run time, split to section and more.

When we ran simple graph is Java (the given one) the max time that any function took to solve is maybe 1 sec, unlike python,
in python it was a little bit different, simple programs such as shortest path os if a graph is connected took to the code in python
a little bit more time.

When we make a little bit research about the resons of its slowliness, we learned that beacause Pyhton is such a high level language
it is very "far" from the hardware, unlike other programming languges, In addition, Python's database access layer is found to be bit underdeveloped and primitive . However, it cannot be applied in the enterprises that need smooth interaction of complex legacy data.
And the last disadventage ( out of many) python has a lot Runtime errors, the reason for that is python language is dynamically typed ,
 it requires more testing and has errors that only show up at runtime .
 
 ### RunTime between Java and Python
 |Java|1000 Nodes|10,000 Nodes|100,000 Nodes|     
 |---|---|---|---|                                         
 |Build Graph|0.0081 sec|0.213 sec| 18.341 sec|
 |Center|0.22 sec| TimeOut| TimeOut|
 |Shortest Path| 0.187 sec| 1.954 sec| 14.517 sec|
 |TSP(3 cities)| 0.487 sec| 14.62 sec| 62.254 sec|
 
 ![JavaRunTime](https://user-images.githubusercontent.com/87694635/147560036-0bbecd6e-7631-4281-9373-44d93b92df2c.png)

 
 |Python|1000 Nodes|10,000 Nodes|100,000 Nodes|
 |---|---|---|---|
 |Build Graph|0.016 sec|0.285 sec| 26.764 sec|
 |Center|0.27 sec| Timeout| Timeout|
 |Shortest Path|0.215 sec| 2.021 sec|19.546 sec|
 |TSP (3 cities)|0.765 sec| 17.56 sec| 87.654 sec|
 
 ![Python runTime](https://user-images.githubusercontent.com/87694635/147560053-b4ce1c8c-d033-4dd1-b14d-8d0c41789581.png)

#### As we can see in the two charts, when the amount of nodes are getting bigger and bigget, Java RunTime is getting better against python.

# Examples of Algorithms on Given Graphs
 
|Algorythm|Graph T0|Graph A0|Graph A1|Graph A2|Graph A3|Graph A4|Graph A5|
|---|---|---|---|---|---|---|---|
|isConnected|False|True|True|True|True|True|True|
|centerPoint and Distansce|None|7 -> 6.8068|8 -> 9.92528|0 -> 7.8199|2 -> 2.1822|6 -> 8.0713|40 ->9.2917
|ShortestPath for node 0 and node 8|None|[0,10,9,8] -> 4.008|[0,1,2,6,7,8] -> 7.4368|[0,1,26,8] -> 3.5127|[0,1,26,8] -> 3.5127|[0, 1, 2, 30, 31, 32, 7, 8] ->9.1643|[0,8] -> 0.9|
|TSP -> [0,7,8]|None|[7, 8, 9, 10, 0] -> 5.4063|[0, 1, 2, 6, 7, 8] -> 7.4368|[0, 1, 26, 8, 7] -> 4.7944|[0, 1, 26, 8, 7] -> 4.7944|[0, 1, 2, 30, 31, 32, 7, 8] -> 9.1643|[0, 8, 7] -> 2.049|
  
  
  ## Resources
 
 [DFS Algorythm](https://en.wikipedia.org/wiki/Depth-first_search)
 
 [Center in Graph](https://en.wikipedia.org/wiki/Graph_center)
 
 [Kosaraju's algorithm](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm)
 
 [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)





