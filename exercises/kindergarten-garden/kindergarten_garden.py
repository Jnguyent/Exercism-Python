plant_letters = {'G': 'Grass', 'C': 'Clover', 'R':  'Radishes', 'V': 'Violets'}

student_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 
                'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

class Garden:

    def __init__(self, diagram, students=student_list):
        self.diagram = diagram.split('\n')
        self.students = sorted(students)


    def plants(self, name):
        index = self.students.index(name)
        return [plant_letters[plant] for row in self.diagram for plant in row[index*2:index*2+2]]
        

