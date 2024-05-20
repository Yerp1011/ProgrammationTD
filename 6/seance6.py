### TD 6

import tkinter
import random
import numpy





class Graph:
    def __init__(self, graph_list):
        """Create a tkinter object to draw the graph"""

        self.__root = tkinter.Tk()
        self.__root.geometry('700x700')
        self.__canvas = tkinter.Canvas(self.__root, width = 700, height = 700, bg = 'white')

        self.__graph_list = graph_list



        # position

        self.__positions = numpy.array([[random.uniform(100, 600), random.uniform(100, 600)] for i in range (len(self.__graph_list))])


        # Velocity

        self.__velocities = numpy.array([[(random.random() - 0.5) * 10, (random.random() - 0.5) * 10] for i in range(len(self.__graph_list))])


        self.__canvas.grid(row = 1, column = 1, rowspan = 2, columnspan = 3)

        self.draw()


        def distance(vertex1, vertex2):
            """Calculs the distance between two vertex """
            x1 = self.__positions[vertex1][0]
            y1 = self.__positions[vertex1][1]
            x2 = self.__positions[vertex2][0]
            y2 = self.__positions[vertex2][1]
            return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

        def distance_to_center(vertex1):
            """Calculs the distance from the center to the vertex """
            x1 = self.__positions[vertex1][0]
            y1 = self.__positions[vertex1][1]
            x2 = 200
            y2 = 200
            return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


        def force(vertex1, vertex2):
            """caculs the strength between every vertex """
            stiffness = 1
            proper_length = 1

            x1 = self.__positions[vertex1][0]
            y1 = self.__positions[vertex1][1]
            x2 = self.__positions[vertex2][0]
            y2 = self.__positions[vertex2][1]
            ux = x2 - x1
            uy = y2 - y1
            D = distance(vertex1, vertex2)
            F = stiffness * (D - proper_length)
            return numpy.array([F * ux/D, F * uy/D])



        def force_center(vertex1):
            """calculs the strength applyed onn every vertex by the center """
            stiffness = 1
            proper_length = 0.2

            x1 = self.__positions[vertex1][0]
            y1 = self.__positions[vertex1][1]
            x2 = 350
            y2 = 350
            ux = x2 - x1
            uy = y2 - y1
            D = distance_to_center(vertex1)
            F = stiffness * (D - proper_length)
            return numpy.array([F * ux/D, F*uy/D])




        # f keyboard
        def f_keyboard(e):
            """Changes the vertex positions when <f> is pressed """
            dt = 0.05

            # Forces
            forces = numpy.array([numpy.array([0, 0]) for i in range(len(self.__graph_list))])
            for vertex in range(len(self.__graph_list)):
                sons = self.__graph_list[vertex]  # every vertex that is link to the one that we consider
                forces[vertex] = force_center(vertex)
                for son in sons:
                    # print(forces[vertex])
                    # print(force(vertex, son))
                    forces[vertex] = forces[vertex] + force(vertex, son)


            # velocity

            velocities = self.__velocities + dt * forces
            #print(velocities)

            #position
            positions = self.__positions + dt * velocities
            self.__positions = positions
            self.__velocities = velocities
            self.draw()


        self.__root.bind("<f>",f_keyboard)


    def draw(self):
        """Represents a graph """
        #erase canva
        self.__canvas.delete("all")


        for vertex in range(len(self.__graph_list)):
            position =  self.__positions[vertex]
           #oval
            self.__canvas.create_oval(position[0] - 5,position[1] - 5,position[0] + 5,position[1] + 5, outline = 'black', fill = 'white')
            #number
            self.__canvas.create_text(position[0],position[1],text = vertex, font = ('Times',7,'bold'), fill = 'black')

            #links
            for son in self.__graph_list[vertex]:
                son_position = self.__positions[son]
                position = self.__positions[vertex]
                self.__canvas.create_line(position[0], position[1], son_position[0], son_position[1], fill = 'red')






    def execute(self):
        """Shows the tkinter object """
        self.__root.mainloop()




if __name__ == '__main__':
    graph1 = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]

    graph = Graph(graph1)
    graph.execute()
