### TD 5

import tkinter
import random




class Target:
    def __init__(self):
        """Create a tkinter object """

        def score(impact):
            """Associate a score to a shot """
            distance_to_center = ((200 - impact[0])**2 + (200 - impact[1])**2)**0.5
            if distance_to_center <= 20:
                return 6
            elif distance_to_center > 20 and distance_to_center <= 50:
                return 5
            elif distance_to_center > 50 and distance_to_center <= 80:
                return 4
            elif distance_to_center > 80 and distance_to_center <= 110:
                return 3
            elif distance_to_center > 110 and distance_to_center <= 140:
                return 2
            elif distance_to_center > 140 and distance_to_center <= 170:
                return 1
            else :
                return 0




        self.__shooting_score = 0



        def to_fire():
            """Allows the Fire! button to work """
            impacts = []
            for i in range (5):
                impacts.append([random.randint(5, 395),random.randint(5, 395)])
            for impact in impacts :
                self.__canvas.create_oval(impact[0] - 5, impact[1] + 5, impact[0] + 5, impact[1] - 5,outline = 'red', fill = 'black')
                self.__shooting_score += score(impact)
            # print(self.__shooting_score)

            # Score Label
            score_panel = tkinter.Label(self.__root, text = self.__shooting_score)
            score_panel.grid(row=3,column=2)





        self.__root = tkinter.Tk()
        self.__root.geometry('400x600')
        self.__score = 0
        self.__canvas = tkinter.Canvas(self.__root, width = 400, height = 400, bg = 'red')



        def to_quit():
            """Allows the quit button to work """
            # print("to quit")
            self.__root.destroy()


        # Oval
        self.__canvas.create_oval(30,30,370,370, outline = 'red', fill = 'ivory')
        self.__canvas.create_oval(60,60,340,340, outline = 'red', fill = 'ivory')
        self.__canvas.create_oval(90,90,310,310, outline = 'red', fill = 'ivory')
        self.__canvas.create_oval(120,120,280,280, outline = 'red', fill = 'ivory')
        self.__canvas.create_oval(150,150,250,250, outline = 'red', fill = 'red')
        self.__canvas.create_oval(180,180,220,220, outline = 'red', fill = 'ivory')

        # Lines
        self.__canvas.create_line(200,0,200,400, fill = 'red')
        self.__canvas.create_line(0,200,400,200, fill = 'red')

        # Numbers
        self.__canvas.create_text(200,45,text = '1',font = ('Times',20,'bold'), fill = 'red')
        self.__canvas.create_text(200,75,text = '2',font = ('Times',20,'bold'), fill = 'red')
        self.__canvas.create_text(200,105,text = '3',font = ('Times',20,'bold'), fill = 'red')
        self.__canvas.create_text(200,135,text = '4',font = ('Times',20,'bold'), fill = 'red')
        self.__canvas.create_text(200,165,text = '5',font = ('Times',20,'bold'), fill = 'ivory')
        self.__canvas.create_text(200,195,text = '6',font = ('Times',20,'bold'), fill = 'red')
        self.__canvas.grid(row = 1, column = 1, rowspan = 2, columnspan = 3)


        # Fire button
        button1 = tkinter.Button(self.__root, text = "Fire!", command = to_fire)
        button1.grid(row = 3,column = 1)


        # Quit button
        button2 = tkinter.Button(self.__root, text = 'Quit', command = to_quit)
        button2.grid(row = 3,column = 3)


        # f keyboard
        def f_keyboard(e):
            """Shoot one time when <f> is pressed """
            impact = [random.randint(5, 395),random.randint(5, 395)]
            self.__canvas.create_oval(impact[0] - 5, impact[1] + 5, impact[0] + 5, impact[1] - 5,outline = 'red', fill = 'black')
            self.__shooting_score += score(impact)
            # print(self.__shooting_score)

            # Score Label
            score_panel = tkinter.Label(self.__root, text = self.__shooting_score)
            score_panel.grid(row=3,column=2)


        self.__root.bind("<f>",f_keyboard)



        #self.__root.mainloop()




    def execute(self):
        """Shows the tkinter object """
        self.__root.mainloop()








if __name__ == '__main__':
    target = Target()
    target.execute()