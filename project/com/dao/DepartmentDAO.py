from project import db
from project.com.vo.DepartmentVO import DepartmentVO

class DepartmentDAO:

    def insertDepartment(self,departmentVO):
        db.session.add(departmentVO)
        db.session.commit()

    def viewDepartment(self):
        DepartmentList = DepartmentVO.query.all()

        return DepartmentList

    def deleteDepartment(self,departmentVO):
        departmentList=DepartmentVO.query.get(departmentVO.departmentId)
        db.session.delete(departmentList)
        db.session.commit()

    def editDepartment(self,departmentVO):
        departmentList=departmentVO.query.filter_by(departmentId=departmentVO.departmentId).all()
        return departmentList

    def updateDepartment(self,departmentVO):
        db.session.merge(departmentVO)
        db.session.commit()

