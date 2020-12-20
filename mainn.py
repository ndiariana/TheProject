import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class color:
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'
print()
print(color.BOLD + "Kelompok 12\nAnggota Kelompok:\n1. Gharyni Nurkhair Mulyono (1301194319)\n2. Nadia Ariana (1301190208)\n" +color.END)
 

def swap(A,i,j):
    if i != j:
        A[i], A[j] = A[j], A[i]


def quicksort(A, start, end):
    if start >= end:
        return
    pivot = A[end]
    pivotIdx = start
    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)

#SelectionSort
def selectionsort(A):
   for i in range(len(A)):
       pos=i
       for j in range(i+1,len(A)):
           if A[j]<A[pos]:
               pos=j
           yield A
       A[i],A[pos]=A[pos],A[i]
       yield A



#main
print()
print(color.UNDERLINE + "Quick Sort and Selection Sort Comparison" + color.END)
print()


N = int(input("Enter your lucky number: "))


A = [x + 1 for x in range(N)]
random.seed(time.time())
random.shuffle(A)



print()
speed_msg="Enter speed of sorting:\n\
            1. Fast\n\
            2. Medium\n\
            3. Slow\n\
            4. Manual\n\
Pick a number: "
speed=input(speed_msg)

speedofSort=0
if speed=='1':
	speedofSort=1
elif speed=='2':
	speedofSort=10
elif speed=='3':
	speedofSort=100
elif speed=='4':
    speedofSort=int(input("Enter any value from 1 to 1000 in millisec\n\
                (1 being fastest,1000 being slowest)\n\
    Speed: "))
    if speedofSort<0:
        print("speed cannot be negative")
        exit()
else:
    print("INVALID CHOICE")
    exit()

print()
sortChooser_msg = "Enter sorting method:\n\
                    1. Quick Sort\n\
                    2. Selection Sort\n\
Pick a method: "
sortingSelection = input(sortChooser_msg)


if sortingSelection == "1":
    title = "Quick sort"
    generator = quicksort(A, 0, N-1)

elif sortingSelection == "2":
    title = "Selection sort"
    generator = selectionsort(A)
else:
    print("PLEASE SELECT 1 or 2 NEXT TIME")
    exit()

#matplotlib
fig, ax = plt.subplots()
ax.set_title(title)
bar_rects = ax.bar(range(len(A)), A, align="edge")

ax.set_xlim(0, N)
ax.set_ylim(0, int(1.07 * N))


#labels
noOfOperations = ax.text(0.02, 0.95, "", transform=ax.transAxes)
timeTaken = ax.text(0.02, 0.91, "", transform=ax.transAxes)
interval= ax.text(0.02, 0.87, "Interval duration:"+str(speedofSort)+"ms", transform=ax.transAxes)

i = [0]
start_time=time.time()


#fig
def update_fig(A, rects, i):
    for rect, val in zip(rects, A):
        rect.set_height(val)

    i[0] += 1
    noOfOperations.set_text("No. of operations:"+str(i[0]))
    # timeTaken.set_text("Time taken:"+str(time.time()-start_time)[:4]+"sec")
    time_elapsed=(time.time()-start_time)
    time_elapsed=float("{0:.2f}".format(time_elapsed))
    time_elapsed=str(time_elapsed)
    timeTaken.set_text("Time taken:"+time_elapsed+" sec")


#animating frame
anim = animation.FuncAnimation(fig, func=update_fig,
    fargs=(bar_rects, i), frames=generator, interval=speedofSort,
    repeat=False)
plt.show()