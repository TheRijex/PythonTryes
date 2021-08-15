first_elem = 1
sec_elem = 1
total_sum = 0
for x in range(4000000):
    if x == first_elem + sec_elem :
        sec_elem = first_elem
        first_elem = x
        if x % 2 == 0:
            total_sum = total_sum + x 
print(total_sum)