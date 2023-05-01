# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:25:22 2023

@author: Marko
"""
import matplotlib.pyplot as plt
import numpy as np
class Menager():
    def __init__(self, xarray, yarray, xlabel, ylabel, label_font_color, label_font_size, label_fonts, plot_title, title_font_color, title_font_size, title_fonts, linecolors, linestyles, linewidth_number, markers, ms_number, mec_color, mfc_color, axis_choise, grid_linestyle, grid_color, grid_linewidth):
        self.xarray = xarray
        self.yarray = yarray
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.label_font_color = label_font_color
        self.label_font_size = label_font_size
        self.label_fonts = label_fonts
        self.plot_title = plot_title
        self.title_font_color = title_font_color
        self.title_font_size = title_font_size
        self.title_fonts = title_fonts
        self.linecolors = linecolors
        self.linestyles = linestyles
        self.linewidth_number = linewidth_number
        self.markers = markers
        self.ms_number = ms_number
        self.mec_color = mec_color
        self.mfc_color = mfc_color
        self.axis_choise = axis_choise 
        self.grid_linestyle = grid_linestyle 
        self.grid_color = grid_color 
        self.grid_linewidth = grid_linewidth
        
    def plot_arrays(self, xarray = [1,2], yarray = [1,2]):
        self.xarray = []
        self.yarray = []
        while True:
            try:
                anotherpoint = input("Do you want enter x and y points?(y/n): ")
                if anotherpoint == "y":
                    xpoint = input("Enter x point: ")
                    ypoint = input("Enter y point: ")
                    if not (xpoint.isdigit() and ypoint.isdigit()):
                        print("Invalid value. Enter integer velues.")
                    else:
                        self.xarray = np.append(self.xarray, int(xpoint))
                        self.yarray = np.append(self.yarray, int(ypoint))
                        if len(self.xarray) == len(self.yarray) and len(self.xarray) > 0: 
                            self.xarray = np.array(self.xarray)
                            self.yarray = np.array(self.yarray)
                        else:
                            print("Length of arrays is not equals. Type coordinates again.")
                            self.xarray.pop()
                            self.yarray.pop()
                elif anotherpoint == "n":
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)
                
        return self.xarray,self.yarray
                    
    def plot_style(self, label_x="X", label_y="Y", label_font = "serif", labelf_font_color="k", label_font_size = 10, plot_title_name ="Title", plot_title_font = "serif", plot_title_font_size = 15, plot_linestyle = "solid", plot_marker = "o", markersize = 5):
        self.xlabel = input("Enter x axis label: ")
        self.ylabel = input("Enter y axis label: ")
        
        while True:
            try:
                if self.xlabel =="" or self.ylabel =="":
                    again = input("Do you want to input again?(y/n):")
                    if again == "y":
                        self.xlabel = input("Enter x axis label: ")
                        self.ylabel = input("Enter y axis label: ")
                    elif again == "n":
                        self.xlabel = "X"
                        self.ylabel = "Y"
                    else:
                        raise ValueError("Invalid value. Type 'y' or 'n'.")
                else:
                    break
            except ValueError as e:
                print(e)
        while True:
            try:
                label_font_color_desire = input("Do you want to set label font color?(y/n): ")
                if label_font_color_desire == "y":
                    available_colors = ["red","green","blue","cyan","magenta","yellow","black"]
                    print(available_colors)
                    label_font_color_name = input("Enter color(choose from the list above): ") 
                    try:    
                        if label_font_color_name in available_colors:
                            self.label_font_color = label_font_color_name
                            break
                        else:
                            raise ValueError("Invalid value. Choose color from list above, and input it.") 
                    except ValueError as e:
                        print(e)
                elif label_font_color_desire == "n":
                    self.label_font_color = "k"
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)
        while True:
            try:
                label_font_size_desire = input("Do you want to set label font size?(y/n): ")
                if label_font_size_desire == "y":
                    while True:
                        try:
                            label_font_size_numer = int(input("Enter font size ('8' to '30'): "))
                            if label_font_size_numer>=8 and label_font_size_numer<=30:
                                self.label_font_size = label_font_size_numer
                                break
                            else:
                                raise ValueError("Type integer value. '8' to '30'.")
                        except ValueError as e:
                            print(e)
                    break
                elif label_font_size_desire == "n":
                    self.label_font_size = 20
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)
        self.label_fonts = {"family":"serif", "color":"", "size":""}
        self.label_fonts["color"] = self.label_font_color
        self.label_fonts["size"] = self.label_font_size
        self.plot_title = input("Enter plot title: ")
        while True:
            if self.plot_title == "":
                try:
                    again = input("Do you want to input again?(y/n): ")
                    if again == "y":
                        self.plot_title = input("Enter plot title: ")
                    elif again == "n":
                        self.plot_title = "Title"
                    else:
                        raise ValueError("Invalid value. Type 'y' or 'n'.")
                except ValueError as e:
                        print(e)
            else:
                break

        while True:
            try:
                title_font_color_desire = input("Do you want to set title font color?(y/n): ")
                if title_font_color_desire == "y":
                    available_colors = ["red","green","blue","cyan","magenta","yellow","black"]
                    print(available_colors)
                    title_font_color_name = input("Enter color(choose from the list above): ") 
                    if title_font_color_name in available_colors:
                        self.title_font_color = title_font_color_name
                        break
                    else:
                        print("Invalid value. Choose color from list above, and input it.")                       
                elif title_font_color_desire == "n":
                    self.title_font_color = "k"
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)
        while True:
            try:
                title_font_size_desire = input("Do you want to set title font size?(y/n): ")
                if title_font_size_desire == "y":
                    while True:
                        title_font_size_numer = int(input("Enter font size ('8' to '30'): "))
                        if title_font_size_numer>=8 and title_font_size_numer<=30:
                            self.title_font_size = title_font_size_numer
                            break
                        else:
                            print("Type integer value. '8' to '30'.")
                    break
                elif title_font_size_desire == "n":
                    self.title_font_size = 25
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)
        self.title_fonts = {"family":"serif", "color":"", "size":""}
        self.title_fonts["color"] = self.title_font_color
        self.title_fonts["size"] = self.title_font_size
        return self.xlabel, self.ylabel, self.label_fonts, self.plot_title, self.title_fonts, self.title_font_color, self.title_font_size, self.label_font_color, self.label_font_size

    def plot_linestyle(self, linecolors = "b",linestyles = 'solid', linewidth_number = 5.0,markers = "o", ms_number = "10", mec_color = "b", mfc_color = "b"):
        while True:
            try:
                linecolor_desire = input("Do you want to set color for line on plot?(y/n): ")
                if linecolor_desire == "y":
                    linecolor_list = ["red","green","blue","cyan","magenta","yellow","black"]
                    print(linecolor_list)
                    linecolor_choise = input("Enter line color (choose color from list above): ")
                    try:
                        if linecolor_choise in linecolor_list:
                            self.linecolors = linecolor_choise
                            break
                        else:
                            raise ValueError("Invalid value. Type color from color list.")
                    except ValueError as e:
                        print(e)
                elif linecolor_desire == "n":
                    self.linecolors = "blue"
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)
        
        while True:
            try:
                linestyle_desire = input("Do you want to set plot linestyle?(y/n): ")
                if linestyle_desire == "y":
                    linestyle_list = ["solid", "dotted", "dashed", "dashdot"]
                    print(linestyle_list)
                    linestyle_choise = input("Type line style(choose from the list above): ")
                    try:    
                        if linestyle_choise in linestyle_list:
                            self.linestyles= linestyle_choise
                            break
                        else:
                            raise ValueError("Invalid velue. Choose linestyle from linestyle list.")
                    except ValueError as e:
                        print(e)
                elif linestyle_desire == "n":
                    self.linestyles = "solid"
                    break
                else:
                    raise ValueError("invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)
        
        while True:
            try:
                linewidth_desire = input("Do you want to set plot line width?(y/n): ")
                if linewidth_desire == "y":
                    linewidth_number_choise = float(input("Enter width for grid line ('3.0' to '20.0'): "))
                    try:
                        if linewidth_number_choise >= 3.0 and linewidth_number_choise <= 20.0:
                            self.linewidth_number = linewidth_number_choise
                            break
                        else:
                            raise ValueError("Invalid value. Type float number from '3.0' to '20.0'.")
                    except ValueError as e:
                        print(e)
                elif linewidth_desire == "n":
                    self.linewidth_number = "5.0"
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)
                
        while True:
            try:    
                markers_desire = input("Do you want to set marker style?(y/n): ")
                if markers_desire == "y":
                    markers_list = ['o','*','.',',','x','X','+','P','s','D','d','p','H','h','v','^','<','>','1','2','3','4','|','_']
                    print(markers_list)
                    markers_choise = input("Type marker style (choose from list above): ")
                    try:    
                        if markers_choise in markers_list:
                            self.markers = markers_choise
                            break
                        else:
                            raise ValueError("Invalid value. Type marker style. Choose from marker style list.")
                    except ValueError as e:
                        print(e)
                elif markers_desire == "n":
                    self.markers = "o"
                    break
                else:
                    print("Invalid value. Type 'y' or'n'.")
            except ValueError as e:
                print(e)
                
        while True:
            try:
                ms_number_desire = input("Do you want to set marker size?(y/n): ")
                if ms_number_desire == "y":
                    ms_number_choise = int(input("Enter marker size ('5' to '25'): "))
                    try:
                        if ms_number_choise >=5 and ms_number_choise <=25:
                            self.ms_number = ms_number_choise
                            break
                        else:
                            print("Invalid value. Type '5' to '25'.")
                    except ValueError as e:
                        print(e)
                elif ms_number_desire == "n":
                    self.ms_number = 8
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)
                
        while True:
            try:
                mec_color_desire = input("Do you want to set marker edge color?(y/n): ")
                if mec_color_desire == "y":
                    available_colors = ["red","green","blue","cyan","magenta","yellow","black"]
                    print(available_colors)
                    mec_color_choise = input("Enter marker edge color (choose from list above): ")
                    try:
                        if mec_color_choise in available_colors:
                            self.mec_color = mec_color_choise
                            break
                        else:
                            raise ValueError("Invalid value. Type marker edge color. Choose from list above, and input it.")
                    except ValueError as e:
                        print(e)
                elif mec_color_desire == "n":
                    self.mec_color = "b"
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)
                
        while True:
            try:
                mfc_color_desire = input("Do you want to set marker face color?(y/n): ")
                if mfc_color_desire == "y":
                    available_colors = ["red","green","blue","cyan","magenta","yellow","black"]
                    print(available_colors)
                    mfc_color_choise = input("Enter marker face color (choose from list above): ")
                    try:    
                        if mfc_color_choise in available_colors:
                            self.mfc_color = mfc_color_choise
                            break
                        else:
                            print("Invalid value. Enter marker face color. Choose from list above, and input it.")
                    except ValueError as e:
                        print(e)
                elif mfc_color_desire == "n":
                    self.mfc_color = "b"
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")  
            except ValueError as e:
                print(e)
                
        return  self.linecolors, self.linestyles, self.linewidth_number, elf.markers, self.ms_number, self.mec_color, self.mfc_color

    def plot_grid(self, axis_choise = "both", grid_linestyle ="solid", grid_color = "k", grid_linewidth = 0.5):
        while True:
            try:
                axis_choise_desire = input("Do you want to enter which grid axis will be available? (y/n): ")
                if axis_choise_desire == "y":
                    axis_choise_question = input("Type 'x' or 'y' to choose wich axis will be available at plot (x/y): ")
                    try:    
                        if axis_choise_question == "x":
                            self.axis_choise = "x"
                            break
                        elif axis_choise_question == "y":
                            self.axis_choise = "y"
                            break
                        elif axis_choise_question == "":
                            again = input("Do you want to input again?(y/n): ")
                            try:
                                if again == "y":
                                    axis_choise_question = input("Type 'x' or 'y' to choose wich axis will be available at plot (x/y): ")
                                    try:    
                                        if axis_choise_question == "x":
                                            self.axis_choise = "x"
                                            break
                                        elif axis_choise_question == "y":
                                            self.axis_choise = "y"
                                            break
                                        else:
                                            raise ValueError("Invalid value. Type 'x' or 'y'. ")
                                    except ValueError as e:
                                        print(e)
                                elif again == "n":
                                    break
                                else:
                                    raise ValueError("Invalid value. Type 'y' or 'n'.")
                            except ValueError as e:
                                print(e)
                        else:
                            raise ValueError("Invalid value. Type 'x' or 'y' or nothing." )
                    except ValueError as e:
                        print(e)
                elif axis_choise_desire == "n":
                    self.axis_choise = "both"
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)

        while True:
            try:
                grid_linestyle_desire = input("Do you want to enter line style to grid? (y/n): ")
                if grid_linestyle_desire == "y":
                    grid_linestyle_list = ["solid", "dotted", "dashed", "dashdot"]
                    print(grid_linestyle_list)
                    grid_linestyle_choise = input("Enter style for grid line (choose style from list): ")
                    if grid_linestyle_choise in grid_linestyle_list:
                        self.grid_linestyle = grid_linestyle_choise
                        break
                elif grid_linestyle_desire == "n":
                    self.grid_linestyle = "solid"
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)
                
        while True:
            try:
                grid_color_desire = input("Do you want to set color to grid line?(y/n): ")
                if grid_color_desire == "y":
                    available_colors = ["red","green","blue","cyan","magenta","yellow","black"]
                    print(available_colors)
                    grid_color_choise = input("Enter color for line (choose from list above): ")
                    if grid_color_choise in available_colors:
                        self.grid_color = grid_color_choise
                        break
                    else:
                        print("Invalid value. Enter color name from list.")
                elif grid_color_desire == "n":
                    self.grid_color = "black"
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)
                
        while True:
            try:
                grid_linewidth_desire = input("Do you want to enter grid line width?(y/n): ")
                if grid_linewidth_desire == "y":
                    grid_linewidth_number = float(input("Enter width for grid line ('0.5' to '1.0'): "))
                    try:
                        if grid_linewidth_number >= 0.5 and grid_linewidth_number <= 1.0:
                            self.grid_linewidth = grid_linewidth_number
                            break
                        else:
                            raise ValueError("Invalid value. Enter width for line. From '0.5' to '1.0'.")
                    except ValueError as e:
                        print(e)
                elif grid_linewidth_desire == "n":
                    self.grid_linewidth = "0.5"
                    break
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)
                    
        return self.axis_choise, self.grid_linestyle, self.grid_color, self.grid_linewidth
        
    def plot_plt(self, xarray, yarray, label_font_color="k", label_font_size=10, title_font_color="k", title_font_size=15, plot_title="Example", xlabel="X", ylabel="Y", linecolor = "blue", linestyles = "dotted", markers = "o", ms_number = 8, mec_color = "b", mafc_color = "b", axis_choise = "both", grid_linestyle ="solid", grid_color = "k", grid_linewidth = 0.1 ):
        
        plt.title(self.plot_title, fontdict = self.title_fonts)
        plt.xlabel(self.xlabel, fontdict = self.label_fonts)
        plt.ylabel(self.ylabel, fontdict = self.label_fonts)
        
        plt.plot(self.xarray, self.yarray, c = self.linecolors, linestyle = self.linestyles, marker = self.markers, ms = self.ms_number, mec = self.mec_color, mfc = self.mfc_color)
        
        plt.grid(axis = self.axis_choise, linestyle = self.grid_linestyle, color = self.grid_color, linewidth = self.grid_linewidth)
        
        plt.show()
        
        exiting_choise = input("do you want to exit?(y/n):")
        while True:
            try:
                if exiting_choise == "y":
                    print("Exiting program.")
                    break
                elif exiting_choise == "n":
                    print("This is end.")
                else:
                    raise ValueError("Invalid value. Type 'y' or 'n'.")
            except ValueError as e:
                print(e)

title = "Title"
markers = "o"
ms_number = 8
mec_color = "blue"
mfc_color = "blue"
xarray = [1,2] 
yarray = [1,2] 
xlabel = "X" 
ylabel = "Y" 
label_font_color = "k" 
label_font_size = 20 
label_fonts = () 
plot_title = "Example" 
title_font_color = "k" 
title_font_size = 25 
title_fonts = () 
linecolors = "b" 
linestyles = "solid" 
linewidth_number = 5.0
markers = "o" 
ms_number = 8 
mec_color = "b" 
mfc_color = "b"
axis_choise = "both" 
grid_linestyle = "solid" 
grid_color = "k"
grid_linewidth = 0.5
menager = Menager(xarray, yarray, xlabel, ylabel, label_font_color, label_font_size, label_fonts, plot_title, title_font_color, title_font_size, title_fonts, linecolors, linestyles, linewidth_number, markers, ms_number, mec_color, mfc_color, axis_choise, grid_linestyle, grid_color, grid_linewidth)
plot_arrays = menager.plot_arrays()
plot_style = menager.plot_style()
plot_linestyle = menager.plot_linestyle()
plot_grid = menager.plot_grid()
menager.plot_plt(plot_arrays, plot_style, plot_linestyle, plot_grid)
