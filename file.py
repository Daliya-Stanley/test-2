# line = None
# # don't know how many times loop have to run...... after : is loop body
# while line != 'done':
#     line = input("Enter a message to echo or type 'done' to complete: ")
#     print('<', line, '>')
# learnt about debugging button


numbers = [23, 67, 32, 9, 77]

# while is true, not empty
# pop is a method= removes last element from the list multiply with 2 and keep going on
# remember to press red button
while numbers:
    print(numbers.pop() * 2)
print("Empty list")
print("Carry on from here onnn...")