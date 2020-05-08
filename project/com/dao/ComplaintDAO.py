from project import db
from project.com.vo.ComplaintVO import ComplaintVO
from project.com.vo.LoginVO import LoginVO

class ComplaintDAO:
    def userInsertComplaint(self,complaintVO):
        db.session.add(complaintVO)
        db.session.commit()


    def userViewComplaint(self,complaintVO):
        complaintList = ComplaintVO.query.filter_by(complaintFrom_loginId=complaintVO.complaintFrom_loginId).all()
        return complaintList

    def userDeleteComplaint(self,complaintVO):
        complaintList = complaintVO.query.get(complaintVO.complaintId)
        db.session.delete(complaintList)
        db.session.commit()

        return complaintList

    def viewComplaintReply(self,complaintVO):
        complaintReplyList = ComplaintVO.query.filter_by(complaintId=complaintVO.complaintId).all()
        return complaintReplyList

#admin side

    def adminViewComplaint(self,complaintVO):
        complaintList = db.session.query(ComplaintVO, LoginVO). \
            join(LoginVO, ComplaintVO.complaintFrom_loginId == LoginVO.loginId)\
            .filter(ComplaintVO.complaintStatus == complaintVO.complaintStatus).all()

        return complaintList


    def adminInsertComplaintReply(self,complaintVO):
        db.session.merge(complaintVO)
        db.session.commit()
