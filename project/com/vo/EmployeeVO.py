from project import db
from project.com.vo.DepartmentVO import DepartmentVO
from project.com.vo.DesignationVO import DesignationVO
from project.com.vo.LoginVO import LoginVO

class EmployeeVO(db.Model):

    __tablename__='employeemaster'
    employeeId=db.Column('employeeId',db.INTEGER,primary_key=True,autoincrement=True,nullable=False)
    employeeFirstName=db.Column('employeeFirstName',db.String(200),nullable=False)
    employeeLastName=db.Column('employeeLastName',db.String(200),nullable=False)
    employee_DepartmentId= db.Column('employee_DepartmentId', db.Integer,
                                       db.ForeignKey(DepartmentVO.departmentId))
    employee_DesignationId= db.Column('employee_DesignationId', db.Integer,
                                         db.ForeignKey(DesignationVO.designationId))
    employeeSalary = db.Column('employeeSalary', db.INTEGER, nullable=False)

    employeeContactNumber = db.Column('employeeContactNumber', db.BigInteger, nullable=False)
    employeeAddress = db.Column('employeeAddress', db.String(200), nullable=False)
    employeeBirthDate = db.Column('employeeBirthDate', db.DATE, nullable=False)
    employeeBloodGroup=db.Column('employeeBloodGroup',db.String(10))
    employeeMaritalStatus=db.Column('employeeMaritalStatus',db.String(30))
    employee_loginId = db.Column('employee_loginId',db.Integer,db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'employeeId':self.employeeId,
            'employeeFirstName':self.employeeFirstName,
            'employeeLastName':self.employeeLastName,
            'employee_DepartmentId':self.employee_DepartmentId,
            'employee_DesignationId':self.employee_DesignationId,
            'employeeSalary':self.employeeSalary,
            'employeeContactNumber':self.employeeContactNumber,
            'employeeAddress':self.employeeAddress,
            'employeeBirthDate':self.employeeBirthDate,
            'employeeBloodGroup':self.employeeBloodGroup,
            'employeeMaritalStatus':self.employeeMaritalStatus,
            'employee_loginId':self.employee_loginId

        }
db.create_all()