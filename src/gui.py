from tkinter import *

class Window:
    
    def __init__(self, width, height, title):
        self.window = Tk() 
        self.window.geometry(f'{width}x{height}')
        self.window.title(title)
        self.enter_state = 0
        self.state_name = ''
    
    def display(self):
        self.window.mainloop()
    
    def submit(self):
        self.state_name = self.enter_state.get().upper()
        self.window.destroy()
        
    def create_submit_page(self):
        header = Label(
            self.window, 
            text='Endangered Species\nIn Your State', 
            font=('MV Boli', 30, 'bold'), 
            fg='#046e0d'
        )
        header.place(x=10, y=10)
        header.pack()

        desc = Label(
            self.window, 
            text='This program will give you information\nabout the 5 most endangered species in your state.', 
            font=('Arial', 20, 'bold')
        )
        desc.place(x=10, y=30)
        desc.pack()

        entry_header = Label(
            self.window, 
            text='Enter your state\'s ABBREVIATION below\n(ex. NJ)', 
            font=('MV Boli', '20', 'bold')
        )
        entry_header.place(x=10, y=60)
        entry_header.pack()

        self.enter_state = Entry(
            self.window,
            font=('Arial', 40) 
        )
        self.enter_state.place(x=10, y=70)
        self.enter_state.pack(side=LEFT)

        submit_button = Button(
            self.window,
            text='Submit',
            font=('Arial', 12, 'bold'),
            command=self.submit,
            height=3,
            width=10
        )
        submit_button.place(x=60)
        submit_button.pack(side=RIGHT)


 
