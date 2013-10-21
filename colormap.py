# Homework 4
# For description goto function
# Written by: Arjun Adhikari
# TAMUG

import matplotlib.pyplot as plt
import numpy as np
import urllib    
import matplotlib
    
def colormap(cbar_name):
    ''' This function is amazing because it can input any color scheme
    and plot data according to it
    ''' 
    url= []
    url = 'http://geography.uoregon.edu/datagraphics/color/'+cbar_name
    
    cmp_data = urllib.urlopen(url)
    red = []
    green=[]
    blue=[]
    cbar_length = len(blue)
        
    for line in cmp_data.readlines()[2:]:
        cbar = line.split()
        red.append(float(cbar[0]))
        green.append(float(cbar[1]))
        blue.append(float(cbar[2]))
    
    cmap_length = len(red)    
    # 1=above; 1=below; decreasing sequence; set 3 bars    
    rd_c   = [(float(n)/(cmap_length-1), red[n-1], red[n]) for n in range (cmap_length)] 
    gr_c = [(float(n)/(cmap_length-1), green[n-1],green[n]) for n in range (cmap_length)]
    bu_c  = [(float(n)/(cmap_length-1), blue[n-1], blue[n]) for n in range (cmap_length)]
        
    cdict = {'red' :rd_c,'green':gr_c, 'blue':bu_c}    
    discrete_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,128)
    
    return discrete_cmap

if __name__ == "__main__":    
    ''' This calculates inout and plots data (random points here),
    and saves to directory'''
    
    my_cmap = colormap('BrBu_10.txt')
    plt.pcolor(np.random.rand(25,25),cmap=my_cmap)
    plt.title('Colormap for color scheme Brown to Blue - BrBu_10',style='normal')
    plt.colorbar()
    plt.show()
    plt.savefig("discrete_colormap_br_bu.png")