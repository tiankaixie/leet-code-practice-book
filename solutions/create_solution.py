# create_solution.py

import os

def create_solution_file(problem_number, problem_name):
    template_path = 'template.py'
    problem_file_name = f"{problem_number:04d}_{problem_name.replace(' ', '')}.py"
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    problem_file_path = os.path.join(parent_dir, problem_file_name)

    with open(template_path, 'r') as template:
        template_content = template.read()

    with open(problem_file_path, 'w') as problem_file:
        problem_file.write(f"# {problem_file_name}\n")
        problem_file.write(template_content)

    print(f"Created new solution file: {problem_file_path}")

if __name__ == "__main__":
    problem_number = int(input("Enter the problem number: "))
    problem_name = input("Enter the problem name: ")
    create_solution_file(problem_number, problem_name)
