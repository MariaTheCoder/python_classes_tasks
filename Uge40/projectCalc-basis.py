def evaluate_precedence(calc, operators):
    calc_copy = calc.copy()

    while any(op in calc_copy for op in operators):
        for i, item in enumerate(calc_copy):
            if item in operators:
                res = 0

                match item:
                    case "+":
                        res = calc_copy[i - 1] + calc_copy[i + 1]
                    case "-":
                        res = calc_copy[i - 1] - calc_copy[i + 1]
                    case "*":
                        res = calc_copy[i - 1] * calc_copy[i + 1]
                    case "/":
                        res = calc_copy[i - 1] / calc_copy[i + 1]

                # Replace part of list which has been calculated with its calculated result
                calc_copy[i - 1:i + 2] = [res]
                break

    return calc_copy


def evaluate_calculation(calc):
    # introduce order of operations:
    # 1) Parentheses
    # 2) Exponentiation - exponentiation is out of scope for this assignment
    # 3) Multiplication and division
    # 4) Addition and subtraction

    print("The calculation is: ", calc)

    calc_copy = calc.copy()

    calc_copy = evaluate_precedence(calc_copy, ["*", "/"])
    calc_copy = evaluate_precedence(calc_copy, ["+", "-"])

    print("new calc_copy:", calc_copy)
    return calc_copy[0]


def form_calculation():
    calculation = []
    res = 0

    while True:
        num = float(input("Gimme a number: "))
        calculation.append(num)

        is_done = input("Is the calculation done? (yes/no) ")

        if is_done.lower() != "yes" and is_done.lower() != "no":
            break

        if is_done.lower() == "yes":
            res = evaluate_calculation(calculation)
            break

        print("Type 1 for addition")
        print("Type 2 for subtraction")
        print("Type 3 for multiplication")
        print("Type 4 for division")

        operator = int(input("Would operation would you like to do? "))

        match operator:
            case 1:
                calculation.append("+")
            case 2:
                calculation.append("-")
            case 3:
                calculation.append("*")
            case 4:
                calculation.append("/")

    return res


result = form_calculation()
print("result:", result)
