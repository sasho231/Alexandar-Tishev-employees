from collections import namedtuple
import datetime
import itertools

Employee = namedtuple("Employee", ["EmpID", "ProjectID", "DateFrom", "DateTo"])
JointWork = namedtuple("JointWork", ["project", "emp1", "emp2", "worktime"])

employees = []

with open("employees.csv", "r") as file:
    employees = [Employee(*line.strip().split(",")) for line in file.readlines()[1:]]

work = itertools.combinations(employees, r=2)

same_project_work = [w for w in work if w[0].ProjectID == w[1].ProjectID]


def time_worked_together(emp1, emp2):
    datefrom = max(datetime.datetime.strptime(emp1.DateFrom, "%Y-%m-%d"), datetime.datetime.strptime(emp2.DateFrom,
                                                                                                     "%Y-%m-%d"), )

    if emp1.DateTo == "NULL" or emp2.DateTo == "NULL":
        dateto = datetime.datetime.today()
    else:
        dateto = min(datetime.datetime.strptime(emp1.DateTo, "%Y-%m-%d"), datetime.datetime.strptime(emp2.DateTo,
                                                                                                     "%Y-%m-%d"), )
    return dateto - datefrom


work_instances = [JointWork(w[0].ProjectID, w[0].EmpID, w[1].EmpID,
                            time_worked_together(w[0], w[1])) for w in same_project_work]

print(max(work_instances, key=lambda x: x.worktime))
