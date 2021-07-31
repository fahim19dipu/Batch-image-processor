# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 01:25:56 2019

@author: fahim
"""
import os

import convertion as conv
import resize as rsz
import shadow_remove as sr
import roations as rot
import noise_removal as nr

import sys
from tkinter import messagebox        
from tkinter import filedialog
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

#global dest
#import UI_test_page_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    #UI_test_page_support.set_Tk_var()
    top = Toplevel1 (root)
   # UI_test_page_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
   # UI_test_page_support.set_Tk_var()
    top = Toplevel1 (w)
    #UI_test_page_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
#def cmdcolor():
#    selected_color_model=selectedColor
#    print(selected_color_model)
class Toplevel1:

    #dest=tk.StringVar()
    def cmdcolor(self):
        selected_color_model=selectedColor.get()
        print(selected_color_model)
    def show_size(self,event):
        print(img_height.get())
        print(img_width.get())
        
    def cmdshadow(self):
        selected_shadow=selectedShadow.get()
        print(selected_shadow)
        
    def cmdnoise(self):
        selected_noise=selectedNoise.get()
        print(selected_noise)
        
    def cmdrotation(self):
        selected_rotation=selectedRotation.get()
        print(selected_rotation)  
        
    def importImages2(self,event):
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = 
        "Select file",filetypes = (("all files","*.*"),("JEPG files","*.jpg"),("png files","*.png")))
        
        path=root.filename
        print(path)
        global dest
        dest = path.rpartition("/")
        dest=dest[0]
        #return path
        dest=dest
        self.path_display.insert(tk.END,dest)

        #try:
        from PIL import Image,ImageTk 
        image=Image.open(root.filename)
        #image.verify()
        image = image.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        panel = tk.Label(root, image = img)
        panel.image = img
        #panel.place(x=550, y=200, anchor="center")
        panel.place(relx=0.514, rely=0.147, relheight=0.245
            , relwidth=0.342)
    #except:
        #    print("Error")

    def looping(self,event):
            #import errno
            import os
            from datetime import datetime
            import cv2
            mydir = os.path.join(
            os.getcwd(),'output', 
            datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
            os.makedirs(mydir)
            
            self.looping_color(mydir)
            self.looping_resize(mydir)
            self.looping_noise(mydir)
            
            self.looping_shadow(mydir)
    
            
                    
            self.looping_rotate(mydir)
            from tkinter import messagebox
            messagebox.showinfo("Message","Process Complete")
    def looping_color(self,mydir):
        print(dest)
        
        for image_path in os.listdir(dest):
            img_p = "f_"+image_path
            temp=os.path.join(mydir,img_p)
            conv.converted(selectedColor.get(),image_path,dest,temp)
        print("Converted")

    def looping_resize(self,mydir):
        print(img_width.get())
        print(img_height.get())
        for image_path in os.listdir(mydir):
            import cv2
            height=img_height.get()
            width =img_width.get()
            temp=os.path.join(mydir,image_path)
            image=cv2.imread(temp)
            #cv2.imshow('pic',image)
            if img_height.get() == 0:
                height =image.shape[0]
            if img_width.get() == 0 :
                width = image.shape[1]
            rsz.resized(image_path,dest,height,width,temp)
        print("Finished Resizing :)") 
        #vp_start_gui()
    def looping_rotate(self,mydir):
        print(dest)
        if selectedRotation.get()==1 :
            for image_path in os.listdir(mydir):
                temp=os.path.join(mydir,image_path)
                rot.rotate_90(image_path,dest,temp)
        elif selectedRotation.get()==2 :
            for image_path in os.listdir(mydir):
                temp=os.path.join(mydir,image_path)
                rot.rotate_270(image_path,dest,temp)
        elif selectedRotation.get()==3 :
            for image_path in os.listdir(mydir):
                temp=os.path.join(mydir,image_path)
                rot.rotate_180(image_path,dest,temp)


        
        print("Finished Rotating:)") 
        #vp_start_gui()
    def looping_shadow(self,mydir):
        print(dest)
        
        if selectedShadow.get()==1:
            for image_path in os.listdir(dest):
                temp=os.path.join(mydir,image_path)
                sr.remove_shadow(image_path,dest,temp)

        print("Finished Shadow removal:)") 
        #vp_start_gui()
    def looping_noise(self,mydir):
            print(dest)
            #for image_path in os.listdir(dest):
                #conv.converted(selectedColor.get(),image_path,dest)
            if selectedNoise.get()==1:
                if selectedColor.get() == 0:
                   for image_path in os.listdir(dest):
                       temp=os.path.join(mydir,image_path)
                       nr.color_gaussian(image_path,dest,temp)
                else:
                   for image_path in os.listdir(dest):
                       temp=os.path.join(mydir,image_path)
                       nr.gray_gaussian(image_path,dest,temp)
                
            elif selectedNoise.get()==2 :
                for image_path in os.listdir(dest):
                    temp=os.path.join(mydir,image_path)
                    nr.colorgray_salt(image_path,dest,temp)
            print("Finished Noise removal")
            
        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        global selectedColor,selectedShadow,selectedNoise,selectedRotation,img_height,img_width
        #selectedColor=0
        selectedColor=tk.IntVar()
        selectedShadow=tk.IntVar()
        selectedNoise=tk.IntVar()
        selectedRotation=tk.IntVar()
        img_height =tk.IntVar()
        
        img_width=tk.IntVar()
        
        #img_width = 100
        #global path
        #selectedColor=tk.IntVar()
        top.geometry("645x770+252+0")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Batch Image Processor")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.import_button = tk.Button(top)
        self.import_button.place(relx=0.772, rely=0.027, height=33, width=106)
        self.import_button.configure(activebackground="#ececec")
        self.import_button.configure(activeforeground="#000000")
        self.import_button.configure(background="#d9d9d9")
        self.import_button.configure(disabledforeground="#a3a3a3")
        self.import_button.configure(foreground="#000000")
        self.import_button.configure(highlightbackground="#d9d9d9")
        self.import_button.configure(highlightcolor="black")
        self.import_button.configure(pady="0")
        self.import_button.configure(text='''Select Folder''')
        self.import_button.bind("<Button-1>",self.importImages2)
        
        self.path_display = tk.Text(top)
        self.path_display.place(relx=0.113, rely=0.027,height=34, relwidth=0.617)
        self.path_display.configure(background="white")
        #self.path_display.configure(disabledforeground="#a3a3a3")
        self.path_display.configure(font="TkFixedFont")
        self.path_display.configure(foreground="#000000")
        self.path_display.configure(highlightbackground="#d9d9d9")
        self.path_display.configure(highlightcolor="black")
        self.path_display.configure(insertbackground="black")
        self.path_display.configure(selectbackground="#c4c4c4")
        self.path_display.configure(selectforeground="black")
        #self.path_display.insert(tk.END,path)    
        
        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.514, rely=0.147, relheight=0.245
                , relwidth=0.342)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")

        self.preview_label = tk.Label(top)
        self.preview_label.place(relx=0.6, rely=0.107, height=26, width=103)
        self.preview_label.configure(activebackground="#f9f9f9")
        self.preview_label.configure(activeforeground="black")
        self.preview_label.configure(background="#d9d9d9")
        self.preview_label.configure(disabledforeground="#a3a3a3")
        self.preview_label.configure(foreground="#000000")
        self.preview_label.configure(highlightbackground="#d9d9d9")
        self.preview_label.configure(highlightcolor="black")
        self.preview_label.configure(text='''Image Preview''')

        self.color_label = tk.Label(top)
        self.color_label.place(relx=0.048, rely=0.214, height=26, width=89)
        self.color_label.configure(activebackground="#f9f9f9")
        self.color_label.configure(activeforeground="black")
        self.color_label.configure(background="#d9d9d9")
        self.color_label.configure(disabledforeground="#a3a3a3")
        self.color_label.configure(foreground="#000000")
        self.color_label.configure(highlightbackground="#d9d9d9")
        self.color_label.configure(highlightcolor="black")
        self.color_label.configure(text='''Color Model''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.032, rely=0.255, relheight=0.141
                , relwidth=0.233)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(cursor="fleur")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        
        self.RGB = tk.Radiobutton(self.Frame1)
        self.RGB.place(relx=0.069, rely=0.095, relheight=0.2, relwidth=0.393)
        self.RGB.configure(activebackground="#ececec")
        self.RGB.configure(activeforeground="#000000")
        self.RGB.configure(background="#d9d9d9")
        self.RGB.configure(disabledforeground="#a3a3a3")
        self.RGB.configure(foreground="#000000")
        self.RGB.configure(highlightbackground="#d9d9d9")
        self.RGB.configure(highlightcolor="black")
        self.RGB.configure(justify='left')
        self.RGB.configure(text='''RGB''')
        self.RGB.configure(variable=selectedColor,value=0,command=self.cmdcolor)
        
        self.Grayscale = tk.Radiobutton(self.Frame1)
        self.Grayscale.place(relx=0.069, rely=0.381, relheight=0.2
                , relwidth=0.634)
        self.Grayscale.configure(activebackground="#ececec")
        self.Grayscale.configure(activeforeground="#000000")
        self.Grayscale.configure(background="#d9d9d9")
        self.Grayscale.configure(disabledforeground="#a3a3a3")
        self.Grayscale.configure(foreground="#000000")
        self.Grayscale.configure(highlightbackground="#d9d9d9")
        self.Grayscale.configure(highlightcolor="black")
        self.Grayscale.configure(justify='left')
        self.Grayscale.configure(text='''Grayscale''')
        self.Grayscale.configure(variable=selectedColor,value=1,command=self.cmdcolor)

        self.Binary = tk.Radiobutton(self.Frame1)
        self.Binary.place(relx=0.069, rely=0.667, relheight=0.2
                , relwidth=0.483)
        self.Binary.configure(activebackground="#ececec")
        self.Binary.configure(activeforeground="#000000")
        self.Binary.configure(background="#d9d9d9")
        self.Binary.configure(disabledforeground="#a3a3a3")
        self.Binary.configure(foreground="#000000")
        self.Binary.configure(highlightbackground="#d9d9d9")
        self.Binary.configure(highlightcolor="black")
        self.Binary.configure(justify='left')
        self.Binary.configure(text='''Binary''')
        self.Binary.configure(variable=selectedColor,value=2,command=self.cmdcolor)
        


        self.path = tk.Label(top)
        self.path.place(relx=0.016, rely=0.013, height=46, width=42)
        self.path.configure(activebackground="#f9f9f9")
        self.path.configure(activeforeground="black")
        self.path.configure(background="#d9d9d9")
        self.path.configure(disabledforeground="#a3a3a3")
        self.path.configure(foreground="#000000")
        self.path.configure(highlightbackground="#d9d9d9")
        self.path.configure(highlightcolor="black")
        self.path.configure(text='''Path''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.048, rely=0.402, height=26, width=117)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Remove Shadow''')

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.032, rely=0.44, relheight=0.101
                , relwidth=0.233)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.remove_shadow_y = tk.Radiobutton(self.Frame2)
        self.remove_shadow_y.place(relx=0.069, rely=0.133, relheight=0.413
                , relwidth=0.352)
        self.remove_shadow_y.configure(activebackground="#ececec")
        self.remove_shadow_y.configure(activeforeground="#000000")
        self.remove_shadow_y.configure(background="#d9d9d9")
        self.remove_shadow_y.configure(disabledforeground="#a3a3a3")
        self.remove_shadow_y.configure(foreground="#000000")
        self.remove_shadow_y.configure(highlightbackground="#d9d9d9")
        self.remove_shadow_y.configure(highlightcolor="black")
        self.remove_shadow_y.configure(justify='left')
        self.remove_shadow_y.configure(text='''Yes''')
        self.remove_shadow_y.configure(variable=selectedShadow,value=1,command=self.cmdshadow)

        self.remove_shadow_n = tk.Radiobutton(self.Frame2)
        self.remove_shadow_n.place(relx=0.069, rely=0.533, relheight=0.413
                , relwidth=0.338)
        self.remove_shadow_n.configure(activebackground="#ececec")
        self.remove_shadow_n.configure(activeforeground="#000000")
        self.remove_shadow_n.configure(background="#d9d9d9")
        self.remove_shadow_n.configure(disabledforeground="#a3a3a3")
        self.remove_shadow_n.configure(foreground="#000000")
        self.remove_shadow_n.configure(highlightbackground="#d9d9d9")
        self.remove_shadow_n.configure(highlightcolor="black")
        self.remove_shadow_n.configure(justify='left')
        self.remove_shadow_n.configure(text='''No''')
        self.remove_shadow_n.configure(variable=selectedShadow,value=0,command=self.cmdshadow)

        self.rotate_label = tk.Label(top)
        self.rotate_label.place(relx=0.048, rely=0.55, height=26, width=50)
        self.rotate_label.configure(background="#d9d9d9")
        self.rotate_label.configure(disabledforeground="#a3a3a3")
        self.rotate_label.configure(foreground="#000000")
        self.rotate_label.configure(text='''Rotate''')

        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.032, rely=0.583
                          , relheight=0.194
                , relwidth=0.442)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        self.rotate_left = tk.Radiobutton(self.Frame3)
        self.rotate_left.place(relx=0.036, rely=0.069, relheight=0.214
                , relwidth=0.385)
        self.rotate_left.configure(activebackground="#ececec")
        self.rotate_left.configure(activeforeground="#000000")
        self.rotate_left.configure(background="#d9d9d9")
        self.rotate_left.configure(disabledforeground="#a3a3a3")
        self.rotate_left.configure(foreground="#000000")
        self.rotate_left.configure(highlightbackground="#d9d9d9")
        self.rotate_left.configure(highlightcolor="black")
        self.rotate_left.configure(justify='left')
        self.rotate_left.configure(text='''Rotate Left''')
        self.rotate_left.configure(variable=selectedRotation,value=1,command=self.cmdrotation)

        self.Radiobutton2 = tk.Radiobutton(self.Frame3)
        self.Radiobutton2.place(relx=0.036, rely=0.276, relheight=0.214
                , relwidth=0.407)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''Rotate Right''')
        self.Radiobutton2.configure(variable=selectedRotation,value=2,command=self.cmdrotation)

        self.flip = tk.Radiobutton(self.Frame3)
        self.flip.place(relx=0.036, rely=0.483, relheight=0.214, relwidth=0.193)
        self.flip.configure(activebackground="#ececec")
        self.flip.configure(activeforeground="#000000")
        self.flip.configure(background="#d9d9d9")
        self.flip.configure(cursor="fleur")
        self.flip.configure(disabledforeground="#a3a3a3")
        self.flip.configure(foreground="#000000")
        self.flip.configure(highlightbackground="#d9d9d9")
        self.flip.configure(highlightcolor="black")
        self.flip.configure(justify='left')
        self.flip.configure(text='''Flip''')
        self.flip.configure(variable=selectedRotation,value=3,command=self.cmdrotation)
        
        self.none = tk.Radiobutton(self.Frame3)
        self.none.place(relx=0.036, rely=0.69, relheight=0.214, relwidth=0.236)
        self.none.configure(activebackground="#ececec")
        self.none.configure(activeforeground="#000000")
        self.none.configure(background="#d9d9d9")
        self.none.configure(disabledforeground="#a3a3a3")
        self.none.configure(foreground="#000000")
        self.none.configure(highlightbackground="#d9d9d9")
        self.none.configure(highlightcolor="black")
        self.none.configure(justify='left')
        self.none.configure(text='''None''')
        self.none.configure(variable=selectedRotation,value=0,command=self.cmdrotation)

        self.remove_noise = tk.Label(top)
        self.remove_noise.place(relx=0.032, rely=0.79, height=26, width=102)
        self.remove_noise.configure(background="#d9d9d9")
        self.remove_noise.configure(disabledforeground="#a3a3a3")
        self.remove_noise.configure(foreground="#000000")
        self.remove_noise.configure(text='''Remove Noise''')

        self.Frame4 = tk.Frame(top)
        self.Frame4.place(relx=0.032, rely=0.83, relheight=0.15
                , relwidth=0.47)

        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#d9d9d9")

        self.gauss_noise = tk.Radiobutton(self.Frame4)
        self.gauss_noise.place(relx=0.065, rely=0.001, relheight=0.413
                , relwidth=0.329)
        self.gauss_noise.configure(activebackground="#ececec")
        self.gauss_noise.configure(activeforeground="#000000")
        self.gauss_noise.configure(background="#d9d9d9")
        self.gauss_noise.configure(disabledforeground="#a3a3a3")
        self.gauss_noise.configure(foreground="#000000")
        self.gauss_noise.configure(highlightbackground="#d9d9d9")
        self.gauss_noise.configure(highlightcolor="black")
        self.gauss_noise.configure(justify='left')
        self.gauss_noise.configure(text='''Gaussina Noise''')
        self.gauss_noise.configure(variable=selectedNoise,value=1,command=self.cmdnoise)

        self.salt_p_noise = tk.Radiobutton(self.Frame4)
        self.salt_p_noise.place(relx=0.065, rely=0.35, relheight=0.213
                , relwidth=0.49)
        self.salt_p_noise.configure(activebackground="#ececec")
        self.salt_p_noise.configure(activeforeground="#000000")
        self.salt_p_noise.configure(background="#d9d9d9")
        self.salt_p_noise.configure(disabledforeground="#a3a3a3")
        self.salt_p_noise.configure(foreground="#000000")
        self.salt_p_noise.configure(highlightbackground="#d9d9d9")
        self.salt_p_noise.configure(highlightcolor="black")
        self.salt_p_noise.configure(justify='left')
        self.salt_p_noise.configure(text='''Salt and Pepper Noise''')
        self.salt_p_noise.configure(variable=selectedNoise,value=2,command=self.cmdnoise)

        self.noise_none = tk.Radiobutton(self.Frame4)
        self.noise_none.place(relx=0.065, rely=0.59, relheight=0.213
                , relwidth=0.2)
        self.noise_none.configure(activebackground="#ececec")
        self.noise_none.configure(activeforeground="#000000")
        self.noise_none.configure(background="#d9d9d9")
        self.noise_none.configure(disabledforeground="#a3a3a3")
        self.noise_none.configure(foreground="#000000")
        self.noise_none.configure(highlightbackground="#d9d9d9")
        self.noise_none.configure(highlightcolor="black")
        self.noise_none.configure(justify='left')
        self.noise_none.configure(text='''None''')
        self.noise_none.configure(variable=selectedNoise,value=0,command=self.cmdnoise)

        self.process = tk.Button(top)
        self.process.place(relx=0.58, rely=0.44, height=33, width=117)
        self.process.configure(activebackground="#ececec")
        self.process.configure(activeforeground="#000000")
        self.process.configure(background="#d9d9d9")
        self.process.configure(disabledforeground="#a3a3a3")
        self.process.configure(foreground="#000000")
        self.process.configure(highlightbackground="#d9d9d9")
        self.process.configure(highlightcolor="black")
        self.process.configure(pady="0")
        self.process.configure(text='''Start Processing''')
        self.process.bind("<Button-1>",self.looping)
        
        self.Frame5 = tk.Frame(top)
        self.Frame5.place(relx=0.032, rely=0.107, relheight=0.114
                , relwidth=0.442)
        self.Frame5.configure(relief='groove')
        self.Frame5.configure(borderwidth="2")
        self.Frame5.configure(relief="groove")
        self.Frame5.configure(background="#d9d9d9")

        self.width = tk.Entry(self.Frame5)
        self.width.place(relx=0.036, rely=0.471,height=24, relwidth=0.378)
        self.width.configure(background="white")
        self.width.configure(disabledforeground="#a3a3a3")
        self.width.configure(font="TkFixedFont")
        self.width.configure(foreground="#000000")
        self.width.configure(insertbackground="black")
        self.width.configure(textvariable=img_width)

        self.height = tk.Entry(self.Frame5)
        self.height.place(relx=0.545, rely=0.471,height=24, relwidth=0.378)
        self.height.configure(background="white")
        self.height.configure(disabledforeground="#a3a3a3")
        self.height.configure(font="TkFixedFont")
        self.height.configure(foreground="#000000")
        self.height.configure(insertbackground="black")
        self.height.configure(textvariable=img_height)

        self.width_label = tk.Label(self.Frame5)
        self.width_label.place(relx=0.073, rely=0.118, height=26, width=46)
        self.width_label.configure(background="#d9d9d9")
        self.width_label.configure(disabledforeground="#a3a3a3")
        self.width_label.configure(foreground="#000000")
        self.width_label.configure(text='''Width''')

        self.height_label = tk.Label(self.Frame5)
        self.height_label.place(relx=0.582, rely=0.118, height=26, width=51)
        self.height_label.configure(background="#d9d9d9")
        self.height_label.configure(disabledforeground="#a3a3a3")
        self.height_label.configure(foreground="#000000")
        self.height_label.configure(text='''Height''')

        self.resize_label = tk.Label(top)
        self.resize_label.place(relx=0.048, rely=0.08, height=26, width=48)
        self.resize_label.configure(background="#d9d9d9")
        self.resize_label.configure(disabledforeground="#a3a3a3")
        self.resize_label.configure(foreground="#000000")
        self.resize_label.configure(text='''Resize''')



if __name__ == '__main__':
    vp_start_gui()





