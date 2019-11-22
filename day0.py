n = int(input())

elements = input()
int_elements = []
# Store elements string into an array where each number is a spot in the array
for elem in elements.split(' '):
    int_elements.append(int(elem))

    
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
