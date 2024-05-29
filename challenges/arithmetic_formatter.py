def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # Set spacing between problems
    spaces = " " * 4

    row1, row2, dashes, answers = [], [], [], []
    for i, problem in enumerate(problems):
        # Suppress spacing for final problem
        if i == len(problems) - 1:
            spaces = ""

        problem_split = problem.split()
        operand1, operand2, operator = problem_split[0], problem_split[2], problem_split[1]
        len1, len2 = len(operand1), len(operand2)

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not all(char.isdigit() for char in operand1 + operand2):
            return 'Error: Numbers must only contain digits.'
        row2.append(f"{operator} ")
        if len1 > 4 or len2 > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Problem width is longest operand plus operator plus a space
        problem_width = max(len1, len2) + 2
        # Define padding for shorter operand
        padding = " " * abs(len1 - len2)

        # Define what's printed on each line
        row1.append("  ")
        dashes.append("-" * problem_width + spaces)
        if len1 > len2:
            row1.append(operand1 + spaces)
            row2.append(padding + operand2 + spaces)
        else:
            row1.append(padding + operand1 + spaces)
            row2.append(operand2 + spaces)
        
        # Evaluate problems
        answer = eval(problem)
        answer_padding = " " * abs(problem_width - len(str(answer)))
        answers.append(f"{answer_padding}{answer}{spaces}")
    
    if show_answers:
        return ''.join(row1) + "\n" + ''.join(row2) + "\n" + ''.join(dashes) + "\n" + ''.join(answers)
    return ''.join(row1) + "\n" + ''.join(row2) + "\n" + ''.join(dashes)