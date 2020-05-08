from project import db
from project.com.vo.DesignationVO import DesignationVO
from project.com.vo.AllowanceDeductionVO import AllowanceDeductionVO

class AllowanceDeductionDAO:
    def insertAllowanceDeduction(self,allowanceDeductionVO):
        db.session.add(allowanceDeductionVO)
        db.session.commit()

    def viewAllowanceDeduction(self):
        print("viewallowanceDeduction")
        allowanceDeductionList = db.session.query(AllowanceDeductionVO, DesignationVO).join(DesignationVO,AllowanceDeductionVO.allowanceDeduction_DesignationId == DesignationVO.designationId).all()
        return allowanceDeductionList
    def deleteAllowanceDeduction(self, allowanceDeductionId):
        allowanceDeductionList = AllowanceDeductionVO.query.get(allowanceDeductionId)

        db.session.delete(allowanceDeductionList)

        db.session.commit()

    def editAllowanceDeduction(self,allowanceDeductionVO):
        allowanceDeductionList = AllowanceDeductionVO.query.filter_by(allowanceDeductionId=allowanceDeductionVO.allowanceDeductionId)

        return allowanceDeductionList

    def updateAllowanceDeduction(self,allowanceDeductionVO):

        db.session.merge(allowanceDeductionVO)

        db.session.commit()