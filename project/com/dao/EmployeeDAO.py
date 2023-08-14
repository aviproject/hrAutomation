from project import db
from project.com.vo.DepartmentVO import DepartmentVO
from project.com.vo.DesignationVO import DesignationVO
from project.com.vo.EmployeeVO import  EmployeeVO
from project.com.vo.LoginVO import LoginVO

class EmployeeDAO:

    def insertEmployee(self, EmployeeVO):
        db.session.add(EmployeeVO)
        db.session.commit()

    def viewEmployee(self):

        EmployeeList = db.session.query(EmployeeVO,DepartmentVO,DesignationVO,LoginVO)\
            .join(DepartmentVO,EmployeeVO.employee_DepartmentId == DepartmentVO.departmentId)\
            .join(DesignationVO,EmployeeVO.employee_DesignationId == DesignationVO.designationId)\
            .join(LoginVO, EmployeeVO.employee_loginId == LoginVO.loginId).all()

        return EmployeeList

    def deleteEmployee(self, employeeVO):

        employeeList = EmployeeVO.query.get(employeeVO.employeeId)

        db.session.delete(employeeList)

        db.session.commit()

    def editEmployee(self,employeeVO):

        employeeList = db.session.query(EmployeeVO, LoginVO) \
            .join(LoginVO, EmployeeVO.employee_loginId == LoginVO.loginId) \
            .filter(EmployeeVO.employeeId == employeeVO.employeeId).all()

        return employeeList

    def updateEmployee(self,employeeVO):

          db.session.merge(employeeVO)

          db.session.commit()


    def viewAttendanceEmployee(self,employeeVO):
        employeeList = db.session.query(EmployeeVO,LoginVO)\
            .join(LoginVO,EmployeeVO.employee_loginId == LoginVO.loginId)\
            .filter(EmployeeVO.employeeId == employeeVO.employeeId).all()
        return employeeList


