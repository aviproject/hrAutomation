from  project import db
from  project.com.vo.DesignationVO import DesignationVO

class DesignationDAO:
    def insertDesignation(self,designationVO):
        db.session.add(designationVO)
        db.session.commit()

    def viewDesignation(self):
        designationList=DesignationVO.query.all()
        return designationList

    def deleteDesignation(self,designationVO):
        designationList = DesignationVO.query.get(designationVO.designationId)
        db.session.delete(designationList)
        print("????????")
        db.session.commit()

    def editDesignation(self,designationVO):
        designationList=designationVO.query.filter_by(designationId=designationVO.designationId).all()
        return designationList

    def updateDesignation(self,designationVO):

        db.session.merge(designationVO)
        db.session.commit()