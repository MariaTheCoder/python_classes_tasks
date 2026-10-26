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

    while "(" in calc_copy:
        close_idx = calc_copy.index(")")
        open_idx = close_idx

        while calc_copy[open_idx] != "(":
            open_idx -= 1

        inner_expression = calc_copy[open_idx + 1:close_idx]
        result_sub = evaluate_calculation(inner_expression)
        calc_copy[open_idx:close_idx + 1] = [result_sub]

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

        if len(calculation) != 1:
            is_done = input("Is the calculation done? (yes/no) ")

            if is_done.lower() != "yes" and is_done.lower() != "no":
                break

            if is_done.lower() == "yes":
                res = evaluate_calculation(calculation)
                break

        print("Type 1 for '+'")
        print("Type 2 for '-'")
        print("Type 3 for '*'")
        print("Type 4 for '/'")
        print("Type 5 for '('")
        print("Type 6 for ')'")

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
            case 5:
                calculation.append("(")
            case 6:
                calculation.append(")")

    return res


result = form_calculation()
print("result:", result)
