from project.com.vo.LoginVO import LoginVO
from project import db


class LoginDAO:
    def insertLogin(self,loginVO):
        db.session.add(loginVO)
        db.session.commit()


    def validateLogin(self, loginVO):
        loginList = LoginVO.query.filter_by(loginUsername=loginVO.loginUsername, loginPassword=loginVO.loginPassword,
                                            loginStatus=loginVO.loginStatus)

        return loginList

    def deleteLogin(self,loginVO):
        loginList = LoginVO.query.get(loginVO.loginId)

        db.session.delete(loginList)
        db.session.commit()

    def viewLogin(self,loginVO):

        loginList = LoginVO.query.filter_by(loginId = LoginVO.loginId).all()

        return loginList

    def updateLogin(self, loginVO):
        db.session.merge(loginVO)

        db.session.commit()

