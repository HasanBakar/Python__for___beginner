num = int(input("How many numbers? "))
total_sum = 0

for n in range (num):
    numbers = float(input("enter the numbers one by one "))
    total_sum += numbers

avg = total_sum / num

print("Your average is ",avg)