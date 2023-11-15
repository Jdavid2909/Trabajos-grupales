
              #Student: Muñoz Yanacallo Jhonattan David
              #Subject: Computer architecture 
              #Date: 15th November 2023

# logical gate AND
def and_gate(input1, input2):
    return input1 and input2

# logical gate OR   
def or_gate(input1, input2):
    return input1 or input2

# logical gate NOT
def not_gate(input):
    return not input

# logical gate XOR
def xor_gate(input1, input2):
    return input1 != input2

# electrical circuit
def circuit(input1, input2):
    result_and = and_gate(input1, input2)
    result_or = or_gate(input1, input2)
    result_not = not_gate(input1)
    result_xor = xor_gate(input1, input2)

    print(f'Inputs: Input1: {input1}, Input2: {input2}')
    print(f'AND: {input1} AND {input2} = {result_and} (Representation circuit: {"O" if result_and else "X"})')
    print(f'OR: {input1} OR {input2} = {result_or} (Representation circuit:: {"O" if result_or else "X"})')
    print(f'NOT: NOT {input1} = {result_not} (Representation circuit:: {"O" if result_not else "X"})')
    print(f'XOR: {input1} XOR {input2} = {result_xor} (Representation circuit:: {"O" if result_xor else "X"})')

# draw imagen in an matrix
def draw_image():
    
    width = 5
    height = 5

    # logical values for the matrix cell
    input_matrix = [
        [True, False, True, False, True],
        [False, True, False, True, False],
        [True, False, True, False, True],
        [False, True, False, True, False],
        [True, False, True, False, True]
    ]

    # create an empty matrix to plot the result
    image_matrix = [[' ' for _ in range(width)] for _ in range(height)]

    # Loops through each cell of the matrix and assigns the resultant value of the logic gates
    for i in range(height):
        for j in range(width):
            input1 = input_matrix[i][j]
            input2 = input_matrix[i][(j + 1) % width]  # Value of the next column (circular)
            result_xor = xor_gate(input1, input2)
            result_or = or_gate(input1, input2)
        
            if result_xor:
                image_matrix[i][j] = 'X'
            elif result_or:
                image_matrix[i][j] = 'O'

    # Prints the image drawn in the matrix
    for i in range(height):
        print(' '.join(image_matrix[i]))

# principal main
if __name__ == "__main__":

    inputOne = input("\n1: Tipe True or False: ")
    inputTwo = input("\n2: Tipe True or False: ")
    print('\n========================================')
    circuit (inputOne, inputTwo)
    print('\n========================================')
    draw_image()