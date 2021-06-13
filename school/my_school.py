# -*- coding: utf-8 -*-
import sys
import uuid
import pandas as pd
from tabulate import tabulate
from functools import cmp_to_key
import operator


class School:

    def __init__(self, students=None, courses=None, scores=None):
        self.id = uuid.uuid4()
        self.students = students
        self.courses = courses
        self.scores = scores

    def exists(self, q="", qt='course'):
        table = self.courses if qt == 'course' else self.students
        return any(x for x in table if x.name == q)

    def get_score(self, student):
        return list(map(lambda x: x.score,
                        filter(lambda x: x.student.id == student.id,
                               filter(lambda x: 0 <= x.score <= 100, self.scores))))

    def get_average(self, student):
        scores = self.get_score(student)
        return sum(scores) / len(scores)

    def generate_results(self):
        res = []
        for student in self.students:
            res.append({student.name: self.get_average(student)})
        res = sorted(res, key=lambda d: list(d.values()), reverse=True)
        return res


class Student(object):

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name


class Course(object):

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name


class Score(object):

    def __init__(self, student, course, score=0):
        self.id = uuid.uuid4()
        self.student = student
        self.course = course
        self.score = score


def read_scores(f="scores.txt"):
    scores = []
    courses = []
    students = []
    school = School(courses=courses, students=students, scores=scores)
    df = pd.read_csv(f, header=0, converters={i: str.strip for i in range(10)})
    for course in df.columns[1:]:
        courses.append(Course(course.strip()))
    for index, row in df.iterrows():
        student = Student(row[0].strip())
        for i, v in enumerate(row[1:]):
            scores.append(Score(student, courses[i], int(v)))
            if int(v) < 0:
                df.iloc[index, i + 1] = ""
            if int(v) == 888:
                df.iloc[index, i + 1] = "--"
        students.append(student)
    df = df.rename(columns={df.columns[0]: ""})
    print(tabulate(df, tablefmt='orgtbl', showindex=False, headers=df.columns))
    res = school.generate_results()
    top = {'name': list(res[0].keys())[0], 'average': res[0].get(list(res[0].keys())[0])}
    print("{students} students, {courses} courses, the top student is {top} average is {average}".format(
        students=len(school.students), courses=len(school.courses), top=top['name'], average=top['average']))
    return False


if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print ("[Usage:] Python my_school.py <scores file> ")
        exit()
    filename = sys.argv[1]
    read_scores(filename)
