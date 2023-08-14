from project import db
from project.com.vo.DesignationVO import DesignationVO
from project.com.vo.LoanDetailVO import LoanDetailVO


class LoanDetailDAO:
    def insertLoanDetail(self,loanDetailVO):
        db.session.add(loanDetailVO)
        db.session.commit()

    def viewLoanDetail(self):
        print("viewLoanDetail")
        loanDetailList = db.session.query(LoanDetailVO, DesignationVO).join(DesignationVO,LoanDetailVO.loanDetail_DesignationId == DesignationVO.designationId).all()
        return loanDetailList

    def deleteLoanDetail(self, loanDetailId):
        loanDetailList = LoanDetailVO.query.get(loanDetailId)

        db.session.delete(loanDetailList)

        db.session.commit()

    def editLoanDetail(self,loanDetailVO):
        loanDetailList = LoanDetailVO.query.filter_by(loanDetailId=loanDetailVO.loanDetailId)

        return loanDetailList

    def updateLoanDetail(self,loanDetailVO):

        db.session.merge(loanDetailVO)

        db.session.commit()