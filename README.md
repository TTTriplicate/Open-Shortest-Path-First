# Problem Set 3
## Open Shortest Path

### REQUIREMENTS

This program is designed to be run in Docker-Compose version 2 or later.  It will not work as-is on Linux systems, which use Docker-Compose v1.x.

In order to run this program, Docker must be installed on the system with a docker-compose version of 2 or later.  This can be confirmed with the command `docker-compose --version`.

### Distances During Djikstra's Algorithm

Rather than do this by hand, I chose to write some code to do it.  I stored the Node and Edge information in a `MySQL` instance, and wrote a python script to access that information and calculate the minimum-length paths to each node from `0`.

The process was simple: store all of the `Nodes` in a table in the database.  Store all of the `Edges` in another table keyed to the first; each edge had a `source`, a `destination`, and a `weight`.  Starting from `0`, I pulled all edges with that Node as a Source.  If the current length to the destination was greater than the current length to the source plus the weight between, the new length replaced the old and the destination was added to the queue to check if that new value would reduce any paths already calcuated.

This continued until all paths had been exhausted.  If the graph in question were not a Directed Acyclic Graph, more work may have been needed to prevent unnecessary recursion.

The results were stored in a dictionary, mapping the router label to the current minimum length, and outputted at each iteration.

The actual output of the program:
```python
{0: 0, 1: 0, 2: 0, 4: 0, 5: 0, 7: 0, 9: 0, 10: 0}
{0: 0, 1: 1, 2: 0, 4: 8, 5: 0, 7: 4, 9: 0, 10: 0}
{0: 0, 1: 1, 2: 3, 4: 7, 5: 0, 7: 4, 9: 0, 10: 0}
{0: 0, 1: 1, 2: 3, 4: 7, 5: 0, 7: 4, 9: 0, 10: 0}
{0: 0, 1: 1, 2: 3, 4: 7, 5: 0, 7: 4, 9: 0, 10: 0}
{0: 0, 1: 1, 2: 3, 4: 7, 5: 0, 7: 4, 9: 0, 10: 0}
{0: 0, 1: 1, 2: 3, 4: 7, 5: 5, 7: 4, 9: 4, 10: 0}
{0: 0, 1: 1, 2: 3, 4: 6, 5: 5, 7: 4, 9: 4, 10: 6}
{0: 0, 1: 1, 2: 3, 4: 6, 5: 5, 7: 4, 9: 4, 10: 6}
{0: 0, 1: 1, 2: 3, 4: 6, 5: 5, 7: 4, 9: 4, 10: 6}
{0: 0, 1: 1, 2: 3, 4: 6, 5: 5, 7: 4, 9: 4, 10: 6}
{0: 0, 1: 1, 2: 3, 4: 6, 5: 5, 7: 4, 9: 4, 10: 6}
{0: 0, 1: 1, 2: 3, 4: 6, 5: 5, 7: 4, 9: 4, 10: 6}
```