#print mean , median , mode of given numbers 

n = int(input())

int_elements = input()
# Store elements string into an array where each number is a spot in the array
int_elements = [int(elem) for elem in int_elements.split(' ')]
    
sum_of_elements = sum(int_elements)
mean = sum_of_elements / float(n)
print (mean)

sorted_elements = sorted(int_elements)

if len(sorted_elements)%2==0:
    median = (sorted_elements[n//2]+sorted_elements[(n//2)-1])/2
else:
    median = sorted_elements[(n//2)+1]

print(float(median))

highest_freq, highest_freq_elem = 0, 0
for elem in sorted_elements:
    current_count = sorted_elements.count(elem)
    if (current_count > highest_freq):
        highest_freq = current_count
        highest_freq_elem = elem
        
mode = highest_freq_elem
print (mode)
