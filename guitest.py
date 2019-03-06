# command_properties.py
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pygubu, gui, os, plot, funcs
from PIL import Image as image
from pathlib import Path
from multiprocessing import Process

# define the function callbacks
#def on_button1_click():
    #im = Image.open('map.jpg')
    #im.show()
 
class MyApplication(pygubu.TkApplication):   
    def _create_ui(self):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('command_properties.ui')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        builder.add_resource_path(dir_path)
        #3: Create the widget using self.master as parent
        self.mainwindow = builder.get_object('mainwindow', self.master)
        self.set_title("Farmbot")
        self.filepath = builder.get_object('filepath')
        self.filepath2 = builder.get_object('filepath2')
        self.toplevel.resizable(False, False)
        builder.connect_callbacks(self)
        #img = Image.open(map.png)
        Label_2 = self.builder.get_object('Label_2')
        Label_2.new_image = tk.PhotoImage(file='default/1.png')
        Label_2.config(image=Label_2.new_image)

    def on_buttonExport_clicked(self):
        try:
            funcs.export()
            messagebox.showinfo('Success', 'Results were exported successfully')
        except:
            messagebox.showinfo('Error', 'Files not found')
            
    def on_menu1_clicked(self):
        print('1')
        Label_2 = self.builder.get_object('Label_2')
        try:
            img = image.open('results\map.png')
            img = img.resize((640,480))
            img.save('default\map.png')
            Label_2.new_image = tk.PhotoImage(file='default\map.png')
            Label_2.config(image=Label_2.new_image)
        except:
            messagebox.showinfo('Error', 'Map not found.')
        
    def on_menu2_clicked(self):
        print('2')
        Label_2 = self.builder.get_object('Label_2')
        try:
            img = image.open('results\map2.png')
            img = img.resize((640,480))
            img.save('default\map2.png')
            Label_2.new_image = tk.PhotoImage(file='default\map2.png')
            Label_2.config(image=Label_2.new_image)
        except:
            messagebox.showinfo('Error', 'Map not found.')
        
    def on_menu3_clicked(self):
        print('3')
        Label_2 = self.builder.get_object('Label_2')
        try:
            img = image.open('results\map3.png')
            img = img.resize((640,480))
            img.save('default\map3.png')
            Label_2.new_image = tk.PhotoImage(file='default\map3.png')
            Label_2.config(image=Label_2.new_image)
        except:
            messagebox.showinfo('Error', 'Map not found.')
            
    def on_menu4_clicked(self):
        print('4')
        Label_2 = self.builder.get_object('Label_2')
        try:
            img = image.open('results\map4.png')
            img = img.resize((640,480))
            img.save('default\map4.png')
            Label_2.new_image = tk.PhotoImage(file='default\map4.png')
            Label_2.config(image=Label_2.new_image)
        except:
            messagebox.showinfo('Error', 'Map not found.')
            
    def on_menu5_clicked(self):
        print('5')
        Label_2 = self.builder.get_object('Label_2')
        try:
            img = image.open('results\map5.png')
            img = img.resize((640,480))
            img.save('default\map5.png')
            Label_2.new_image = tk.PhotoImage(file='default\map5.png')
            Label_2.config(image=Label_2.new_image)
        except:
            messagebox.showinfo('Error', 'Map not found.')       
    """
    def on_buttonDir_clicked(self):
        global filename
        filename = filedialog.askdirectory()
        print(filename)
        Label_4 = self.builder.get_object('Label_4')
        Label_4.config(text=filename)
    """
    
    def on_buttonCopy_clicked(self):
        imgPath = self.filepath2.cget('path')
        try:
            funcs.delete()
            print("file deleted")
            gui.copy(imgPath)
            print("images copied")
            messagebox.showinfo('Success', 'Images copied!')
        except:
             messagebox.showinfo('Error', 'Please select valid path')
            
    def on_estTime_clicked(self):
        try:
            plot.plot_bar_x(1)
        except:
            messagebox.showinfo('Error', 'Results not found')
                
    def on_buttonGen_clicked(self):
        #copy images to another folder

        dim = []
        entry = self.builder.get_object('Entry_x')
        dim.append(int(entry.get()))
        entry = self.builder.get_object('Entry_y')
        dim.append(int(entry.get()))
        """
        entry = self.builder.get_object('Entry_x')
        valueX = entry.get()
        entry = self.builder.get_object('Entry_y')
        valueY = entry.get()
        """
        #print(valueX, valueY)
        path = self.filepath.cget('path')
        print("path" + path)
        funcs.wpGen(path)
        #create visual maps using multiprocessing
        """
        p1 = Process(target=gui.createMap, args=(dim, 'a')) # create a process object p1
        p1.start()                   # starts the process p1
        p2 = Process(target=gui.createMap, args=(dim, 'Level 2'))
        p2.start()
        p3 = Process(target=gui.createMap, args=(dim, 'Level 3'))
        p3.start()
        p4 = Process(target=gui.createMap, args=(dim, 'Level 4'))
        p4.start()
        p5 = Process(target=gui.createMap, args=(dim, 'Level 5'))
        p5.start()

        gui.createMap((int(valueX),int(valueY)))
        gui.createMap2((int(valueX),int(valueY)))
        gui.createMap3((int(valueX),int(valueY)))
        gui.createMap4((int(valueX),int(valueY)))
        gui.createMap5((int(valueX),int(valueY)))
        """
        p1 = Process(target=gui.createMap, args=(dim,))
        p1.start()
        """
        p2 = Process(target=gui.createMap2, args=(dim,))
        p2.start()
        p3 = Process(target=gui.createMap3, args=(dim,))
        p3.start()
        p4 = Process(target=gui.createMap4, args=(dim,))
        p4.start()
        p5 = Process(target=gui.createMap5, args=(dim,))
        p5.start()
        """
        p1.join()
        """
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        """
        gui.createMap(dim)
        funcs.getLatLong()
        messagebox.showinfo('Success', 'Waypoints generated!')
        #except:
            #messagebox.showinfo('Error', 'Invalid input')

    def on_loadLvl2_clicked(self):
        gui.loadLvl2()

    def on_loadLvl3_clicked(self):
        gui.loadLvl3()

    def on_loadLvl4_clicked(self):
        gui.loadLvl4()

    def on_loadLvl5_clicked(self):
        gui.loadLvl5()

    def on_loadAll_clicked(self):
        gui.loadAll()
        
if __name__ == '__main__':
    root = tk.Tk()
    app = MyApplication(root)
    app.run()
