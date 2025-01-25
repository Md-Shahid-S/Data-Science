if __name__ == '__main__':
    def find_percentage(student_marks, query_name):
        student_marks_list = student_marks[query_name]
        percentage = sum(student_marks_list) / len(student_marks_list)
        return "{:.2f}".format(percentage)
        
    # Number of students
    n = int(input("Enter the number of students: "))
    
    student_marks = {}
    # Loop to get student names and their scores
    for _ in range(n):
        # Input format for name and scores of the student
        name, *line = input("Enter the name and scores of the student (separated by spaces): ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    # Query name to find the percentage
    query_name = input("Enter the name of the student to query: ")
    
    # Print the percentage
    print(f"{query_name}'s percentage is: {find_percentage(student_marks, query_name)}")
