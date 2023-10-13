# Write a program that creates a list named step_lengths, that contains the length of every step.
# The first step length would be y[1] - y[0], the second would be y[2] - y[1], etc.
# In this specific example, we recorded nine steps, but your code must work on any number of steps.

# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]

step_lengths = []

i = 0

while i < len(y)-1:
    step_lengths.append(y[i+1] - y[i])
    i += 1

print(step_lengths)

