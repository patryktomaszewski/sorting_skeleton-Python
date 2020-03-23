from sort import bubblesort, quicksort, quicksort_used_in_quicksort
from timeit import timeit
import random


sorted_list = [x for x in range(1,500)]
not_sorted_list = [x for x in range(500,0,-1)]
equal_list = 500*[1]

rnd = random.sample(range(1, 1001), 1000)

t1_bubble = timeit ( str(bubblesort(sorted_list)) , number =1 , globals = globals ())
t2_bubble = timeit ( str(bubblesort(not_sorted_list)) , number =1 , globals = globals ())
t3_bubble = timeit ( str(bubblesort(equal_list)) , number =1 , globals = globals ())
t4_bubble = timeit ( str(bubblesort(rnd)) , number =1 , globals = globals ())


t1_quicksort = timeit ( str(quicksort(sorted_list)) , number =1 , globals = globals ())
t2_quicksort = timeit ( str(quicksort(not_sorted_list)) , number =1 , globals = globals ())
t3_quicksort = timeit ( str(quicksort(equal_list)) , number =1 , globals = globals ())
t4_quicksort = timeit ( str(quicksort(rnd)) , number =1 , globals = globals ())

print("lista uporzadkowana")
print("bubble: ",t1_bubble)
print("quick: ",t1_quicksort)

print("lista malejąca")
print("bubble: ",t2_bubble)
print("quick: ",t2_quicksort)

print("lista stalych elementow")
print("buuble: ",t3_bubble)
print("quick: ",t3_quicksort)

print("lista losowych elementow")
print("bubble: ",t4_bubble)
print("quick: ",t4_quicksort)


#Bubblesort jest wydajenieszy od quicksorta tylko w przypadku listy uporządkowanej, jednak w pozostałych przypadkach
#quicksort działa szybciej i wydajniej