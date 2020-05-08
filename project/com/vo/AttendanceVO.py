from project import db
from project.com.vo.EmployeeVO import EmployeeVO
from project.com.vo.DepartmentVO import DepartmentVO
from project.com.vo.DesignationVO import DesignationVO


class AttendanceVO(db.Model):
    __tablename__ = 'attendancemaster'

    attendanceId = db.Column('attendanceId', db.Integer, primary_key=True, autoincrement=True)
    attendance_EmployeeId = db.Column('attendance_EmployeeId', db.Integer, db.ForeignKey(EmployeeVO.employeeId))
    attendance_DepartmentId = db.Column('attendance_DepartmentId', db.Integer, db.ForeignKey(DepartmentVO.departmentId))
    attendance_DesignationId = db.Column('attendance_DesignationId', db.Integer,
                                         db.ForeignKey(DesignationVO.designationId))
    attendanceMonth = db.Column('attendanceMonth', db.String(20))
    attendanceFileName = db.Column('attendanceFileName', db.String(200))
    attendanceFilePath = db.Column('attendanceFilePath', db.String(200))
    attendanceFileUploadDate = db.Column('attendanceFileUploadDate', db.String(30))
    attendanceFileUploadTime = db.Column('attendanceFileUploadTime', db.String(30))
    attendanceFileObjectURL = db.Column('attendanceFileObjectURL', db.String(300))


def as_dict(self):
    return {
        'attendanceId': self.attendanceId,
        'attendance_EmployeeId': self.attendance_EmployeeId,
        'attendance_DepartmentId': self.attendance_DepartmentId,
        'attendance_DesignationId': self.attendance_DesignationId,
        'attendanceMonth': self.attendanceMonth,
        'attendanceFileName': self.attendanceFileName,
        'attendanceFilePath': self.attendanceFilePath,
        'attendanceFileUploadDate': self.attendanceFileUploadDate,
        'attendanceFileUploadTime': self.attendanceFileUploadTime,
        'attendanceFileObjectURL': self.attendanceFileObjectURL
    }


db.create_all()
