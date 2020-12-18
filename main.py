
# ini fix


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm
from matplotlib.colors import Normalize

class color:
   DARKCYAN = '\033[36m'
   PURPLE = '\033[95m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
print()
print(color.BOLD + "Kelompok 12\nAnggota Kelompok:\n1. Gharyni Nurkhair Mulyono (1301194319)\n2. Nadia Ariana (1301190208)\n" +color.END)
print(color.UNDERLINE + "Quick Sort and Selection Sort Comparison\n" + color.END)

#QuickSort
def partition(y,low,high):
    pivot=y[low]
    i=low+1
    j=high
    while True:
        while i<=j and y[i]<=pivot:
            i+=1
            yield y
        while i<=j and y[j]>pivot:
            j-=1
            yield y
        if i<j:
            y[i],y[j]=y[j],y[i]
        else:
            break
    y[low],y[j]=y[j],y[low]
    yield y
    return j

def quicksort(y,low,high):
    if low<high:
        j=yield from partition(y,low,high)
        yield from quicksort(y,low,j-1)
        yield from quicksort(y,j+1,high)


#SelectionSort
def selectionsort(y):
    for i in range(len(y)):
        pos=i
        for j in range(i+1,len(y)):
            if y[j]<y[pos]:
                pos=j
            yield y
        y[i],y[pos]=y[pos],y[i]
        yield y

if __name__=="__main__":
    while True:
        n=int(input(color.PURPLE + "Enter your lucky number: " + color.END))
        
        print('1. Quick Sort')
        print('2. Selection Sort')
        ch=int(input("Enter your choice: "))
        
        y = np.random.randint(1,n+1,n)
        fig,axes = plt.subplots()
        
        if ch==1:
            title='QUICK SORT O(n**2)'
            generator = quicksort(y,0,n-1)
        elif ch==2:
            title='SELECTION SORT O(n**2)'
            generator = selectionsort(y)
    
        mycmap= cm.get_cmap('rainbow')

        my_norm = Normalize(vmin=0, vmax=100)
        
        
        barr = axes.bar(np.arange(1,n+1),y,align='edge',color=mycmap(my_norm(y)))
        axes.set_xticks(range(0,n+1,n//5))
        axes.set_yticks(range(0,n+1,n//5))

        text = axes.text(0.02, 0.95, "", transform=axes.transAxes)
        axes.set_title(title)


        count=0
        def outp(y,r):
            global count
            for a,b in zip(r,y):
                a.set_height(b)
            count+=1
            text.set_text("Number of Operations: "+str(count))
        

        anim = FuncAnimation(fig, outp, fargs=(barr,) ,frames = generator, interval=1, repeat=False)
        plt.show()
        repeat = input("DO YOU WANT TO CONTINUE(y/n): ")
        if repeat!='y' and repeat!='Y':
            break
