# Knight Hacks 2020 Virtual Hackathon
My goal was to come out of this weekend with a pathfinding algorithm visualizer. I maneged to get the A* Search algorithm done. I used pygame to to visualize the algorithm. The window was broken up into column and rows, with each square representing Node.
# Description
The A* searching algorithm, further explained [here](https://brilliant.org/wiki/a-star-search/)<br/>
It uses concepts from Eulerian graph theory. The basics of this algorithms : <br/>
f(n)=g(n)+h(n)
<br/>where  <br/>
f(n) = total estimated cost of path through node n<br/>
g(n) = cost so far to reach node n<br/>
h(n) = estimated cost from nn to goal. This is the heuristic part of the  
 cost function, so it is like a guess. <br/>
h(n) can be calculated different ways, but these are the main 2<br/>  
 Manhattan Distance Heuristic abs(x_start - x_end) + abs(y_start - y_end)<br
 /> Euclidean Distance Heuristic sqrt((x_start - x_end)^2 + (y_start - y_end
 )^2)<br/> <br>
Manhattan Distance Heureistic is quicker to calculate, but the Euclidean  
Distance Heuristic created more realistic paths, so I went with the latter
# Credit

 - [Brilliant's A* Search page](https://brilliant.org/wiki/a-star-search/)
 - A plethora of frantic google searches
 - Coffee