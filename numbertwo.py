import sys
import matplotlib.pyplot as plt
import os
import numpy as np

def read_values_from_file(filename, x_min=-512, x_max=512):
    x_values=[]
    y_values=[]
    try:
        with open(filename,'r') as file:
            file.readline()
            for line in file:
                for i in range(len(line)):
                    if line[i]==' ':
                         x=float(line[0:i])
                         if (x>=float(x_min) and x<=float(x_max)):
                             y=float(line[i+4:len(line)+1])
                             x_values.append(x)
                             y_values.append(y)
                         break
        return x_values, y_values
    except FileNotFoundError:
        print("File not Found")
        sys.exit(1)
    except Exception as e:
        print("Error while reading: ",e)
        sys.exit(1)
        
def plot_with_values(x_values,y_values):
    plt.plot(x_values, y_values,'r')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('График функции')
    plt.grid(True)
    plt.show()
    
if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите имя файла с данными в качестве аргумента командной строки.")
        sys.exit(1)
        
    file_name = sys.argv[1]
    x_arr, y_arr = [],[]
    if (args_lentgh>1):
        x_min=sys.argv[2]
        x_max=sys.argv[3]
        x_arr, y_arr = read_values_from_file(file_name,x_min,x_max)
    else:
        x_arr, y_arr = read_values_from_file(file_name)
    #Построение графика
    plot_with_values(x_arr,y_arr)

