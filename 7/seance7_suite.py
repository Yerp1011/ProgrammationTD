### TD 7 suite


import tkinter
import random
import numpy



class Graph_random:
    def __init__(self, vertex_number):
        """Create a random graph on a grid and a tkinter object to draw the graph"""
        canva_length = 10 * vertex_number + 10
        self.__root = tkinter.Tk()
        self.__root.geometry(str(canva_length)+'x'+str(canva_length))
        self.__canvas = tkinter.Canvas(self.__root, width = canva_length, height = canva_length, bg = 'white')

        self.__index = {}

        positions = []
        for vertex1 in range(vertex_number):
            for vertex2 in range(vertex_number):
                positions.append([5 + vertex1 * 10, 5 + vertex2 * 10])
                self.__index[vertex1, vertex2] = len(positions) - 1
        self.__positions = positions

        self.__colors_index = [i for i in range (vertex_number**2)]

        def color_generator():
            r, g, b = random.randint(0,255), random.randint(0,255),random.randint(0,255)
            return f"#{r:02x}{g:02x}{b:02x}"



        #colors = ['chocolate' for i in range(vertex_number**2)]


        graph_list = [[] for i in range(vertex_number**2)]

        def bernoulli(proba):
            result = random.random()
            if result <= proba:
                return True
            else:
                return False

        def links(proba, vertex_number):
            graph_list = [[] for i in range(vertex_number)]
            for i in range(vertex_number):
                for j in range(vertex_number):
                    #i+1,j
                    if bernoulli(proba):
                        graph_list[self.__index[[i, j]]].append(self.__index[i + 1, j])
                    # i, j + 1
                    if bernoulli(proba):
                        graph_list[self.__index[[i, j]]].append(self.__index[i, j + 1])

        self.__graph_list = graph_list







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

        graph_length = len(self.__graph_list)


        for vertex1 in range(graph_length):
            position1 = self.__positions[vertex1]

            self.__canvas.create_oval(position1[0] - 5,position1[1] - 5,position1[0] + 5,position1[1] + 5, outline = 'black', fill = self.__colors_index[vertex1])
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

    graph = Graph_random(10)
    graph.execute()





















