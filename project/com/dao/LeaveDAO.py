from project import db
from project.com.vo.LeaveVO import LeaveVO

class LeaveDAO:

    def insertLeave(self,leaveVO):
        db.session.add(leaveVO)
        db.session.commit()


    def viewLeave(self):
	
        leaveVOList = LeaveVO.query.all()

        return leaveVOList


    def deleteLeave(self,leaveVO):

        leaveList = LeaveVO.query.get(leaveVO.leaveId)

        db.session.delete(leaveList)

        db.session.commit()


    def editLeave(self,leaveVO):

        leaveList = LeaveVO.query.filter_by(leaveId=leaveVO.leaveId).all()

        return leaveList

    def updateLeave(self,leaveVO):

        db.session.merge(leaveVO)

        db.session.commit()