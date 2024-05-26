### TD 7


import tkinter
import random
import numpy





class Graph:
    def __init__(self, graph_list, positions, colors_index):
        """Create a tkinter object to draw the graph"""

        self.__root = tkinter.Tk()
        self.__root.geometry('700x700')
        self.__canvas = tkinter.Canvas(self.__root, width = 700, height = 700, bg = 'white')

        self.__graph_list = graph_list
        self.__positions = positions
        self.__colors_index = colors_index


        self.__canvas.grid(row = 1, column = 1, rowspan = 2, columnspan = 3)

        self.draw()



        # def min_local(self, vertex):
        #     """Return the lower ID amond the direct neighbors of the Vertex """
        #     neighbors = self.__graph_list[vertex]
        #     neighbors.append(vertex)
        #
        #     min_neighbors = min(neighbors)
        #
        #     self.__colors_index[vertex] = min_neighbors
        #     self.draw()


        # f keyboard


        self.__vertex_i = 0
        def f_keyboard(e):
            """Apply min local on  """
            if self.__vertex_i <= 11:
                self.min_local(self.__vertex_i)
                self.__vertex_i+=1



        self.__root.bind("<f>",f_keyboard)




    def draw(self):
        """Represents a graph """
        #erase canva
        self.__canvas.delete("all")

        colors = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']

        graph_length = len(self.__graph_list)


        for vertex1 in range(graph_length):
            position1 = self.__positions[vertex1]

            self.__canvas.create_oval(position1[0] - 5,position1[1] - 5,position1[0] + 5,position1[1] + 5, outline = 'black', fill = colors[self.__colors_index[vertex1]])
            self.__canvas.create_text(position1[0] - 12, position1[1], text = vertex1, font = ('Times',9,'bold'), fill = 'black')

            for vertex2 in self.__graph_list[vertex1]:
                position2 = self.__positions[vertex2]
                self.__canvas.create_line(position1[0], position1[1], position2[0], position2[1], fill = 'black')





    def min_local(self, vertex):
        """Return the lower ID amond the direct neighbors of the Vertex """
        neighbors = self.__graph_list[vertex].copy()
        for vertex1 in range(len(self.__graph_list)):
            if vertex in self.__graph_list[vertex1]:
                neighbors.append(vertex1)

        neighbors.append(vertex)
        # print(neighbors)
        min_neighbors = min(neighbors)
        # print("min : ", min_neighbors)
        self.__colors_index[vertex] = self.__colors_index[min_neighbors]
        self.draw()







    def execute(self):
        """Shows the tkinter object """
        self.__root.mainloop()




if __name__ == '__main__':
    graph1 = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]

    positions = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198])

    colors_index = [i for i in range(len(graph1))]

    graph = Graph(graph1, positions, colors_index)
    graph.execute()






















