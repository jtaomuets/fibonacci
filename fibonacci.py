# Recursive code that calculates the nth term in the Fibonacci sequence
# This code accepts positive integers as inputs ONLY

# Main function
def main():
# Recursive function is defined
    def fibonacci(sequence_number):
    # The base case is defined as a value less than or equal to 1
        if sequence_number <= 1:
        # If the user's input is less than or equal to 1, the return function returns the result back to the caller
            return sequence_number 
    # Alternatively (the user's input is > 1), the fibonacci function is recursively called
        else:
            a = fibonacci(sequence_number - 1)
            b = fibonacci(sequence_number - 2)
            return(a + b)

# User input is acquired to determine nth term
    nth_term = int(input("What nth term do you want to determine?"))

# If the user's input is <= 0, they are asked to select another number
    if nth_term <= 0:
        print("Please select an integer greater than zero")
# Alternatively (user's input > 0), the fibonacci sequence is printed
    else:
        print("The Fibonacci sequence for your number is:")
    # The for loop is initiated to provide output in the range of 1 to the user's input
        for i in range(nth_term):
            print(fibonacci(i))

# while loop enables the program to re-apply as long as the user wants to
while True:
    main()
    # Asks user whether they want to determine another term
    if input("Do you want to determine another nth term? (Y/N)").strip().upper() != 'Y':
        # If user does not want to determine another term, the program is terminated
        exit()