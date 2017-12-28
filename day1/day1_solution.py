# returns the current digit if it matches the subsequent one, 0 otherwise
def matching_result(current_digit, next_digit):
    if current_digit == next_digit:
        return current_digit
    else:
        return 0


# stores the input digits into an array
def get_input_from_file(filename):
    input = []
    with open(filename,'r') as f:
        for line in f.readlines():
            input.append(list(line))
    flattened_input = [y for x in input for y in x]

    return flattened_input


def main():
    pass

if __name__ == '__main__':
    main()
