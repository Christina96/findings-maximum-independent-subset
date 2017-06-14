# Findings on maximum independent subset or Far Away and Fave

This is a work which is about **Findings on maximum independent subset**. Is written in **Python 3.X** and is based on the article 

David S. Johnson, Mihalis Yannakakis, and Christos H. Papadimitriou: [On Generating All Maximal Independent Sets](https://github.com/dmst-algorithms-course/assignment-2016-bonus/blob/master/generating_all_maximal_independent_datasets.pdf). Information Processing Letters, 27, 119-123, 1988.

To run the program:

`mis.py [-h] [-d] [-n NAME] [-f FIGURE] input`

* The parameter `input` is the name of .txt file which has the graph. The file haw the graph in networkx adjacency list format.
* If `–d `parameter given Αν δίνεται η παράμετρος -d will appear on the computer screen:
  * Image with the graph
  * Images with maximum independent subset
* If `-n ΝΑΜΕ` and `-f FIGURE` given the program save the images with name `NAME_x.FIFURE`. For example `-n cube -f png` the images saved like **cube_0.png, cube_1.png** etc.

This work was given from [Panos Louridas](https://github.com/louridas) in course **Algorithms and Data Structures** (*Department of Forest Science and Technology*, Athens University of Economics and Business).
