from project import db
from project.com.vo.AttendanceVO import AttendanceVO
from project.com.vo.EmployeeVO import EmployeeVO
from project.com.vo.DepartmentVO import DepartmentVO
from project.com.vo.DesignationVO import DesignationVO
from project.com.vo.LoginVO import LoginVO


class AttendanceDAO:
    def insertAttendance(self, attendanceVO):
        db.session.add(attendanceVO)
        db.session.commit()

    def viewAttendance(self):
        print("inside attendance DAO............!!!!!!!!!!!!!")
        attendanceVOList = db.session.query(AttendanceVO, DesignationVO, DepartmentVO, EmployeeVO, LoginVO) \
            .join(DepartmentVO, AttendanceVO.attendance_DepartmentId == DepartmentVO.departmentId) \
            .join(DesignationVO, AttendanceVO.attendance_DesignationId == DesignationVO.designationId) \
            .join(EmployeeVO, AttendanceVO.attendance_EmployeeId == EmployeeVO.employeeId) \
            .join(LoginVO, EmployeeVO.employee_loginId == LoginVO.loginId).all()
        print("complete attendance")
        return attendanceVOList

    def deleteAttendance(self, attendanceVO):
        attendanceList = attendanceVO.query.get(attendanceVO.attendanceId)

        db.session.delete(attendanceList)

        db.session.commit()

        return attendanceList
