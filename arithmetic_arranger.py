def arithmetic_arranger(problems, show_answers=False):
  # Check if problems exceeds the max allowed (5)
  if len(problems) > 5:
    return ('Error: Too many problems.')
  top = ''
  bottom = ''
  lines = ''
  results = ''

  for p in problems:
    operand1 = p.split()[0]
    operator = p.split()[1]
    operand2 = p.split()[2]

    # Check if operator is + or -
    if operator != '+' and operator != '-':
      return ("Error: Operator must be '+' or '-'.")

    # Check if operand1 and operand2 are digits
    if not operand1.isdigit() or not operand2.isdigit():
      return ('Error: Numbers must only contain digits.')

    # Check if operand1 and operand2 are < 4 digits
    if len(operand1) > 4 or len(operand2) > 4:
      return ('Error: Numbers cannot be more than four digits.')

    # Get total of correct function
    if operator == '+':
      total = str(int(operand1) + int(operand2))
    elif operator == '-':
      total = str(int(operand1) - int(operand2))

    # Determine the width of the problem
    width = max(len(operand1), len(operand2)) + 2

    # Create problem display
    operand2 = operator + operand2.rjust(width - 1)
    top = top + operand1.rjust(width) + (4 * " ")
    bottom = bottom + operand2 + (4 * " ")
    lines = lines + len(operand2) * "-" + (4 * " ")
    results = results + str(total).rjust(width) + (4 * " ")

  # Remove excess whitespace
  top = top.rstrip()
  bottom = bottom.rstrip()
  lines = lines.rstrip()
  results = results.rstrip()

  if show_answers == True:
    arranged_problems = top + '\n' + bottom + '\n' + lines + '\n' + results
  elif show_answers == False:
    arranged_problems = top + '\n' + bottom + '\n' + lines
  return (arranged_problems)
