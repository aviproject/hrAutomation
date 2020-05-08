from project import db
from project.com.vo.LetterTypeVO import LetterTypeVO


class LetterTypeDAO:

    def insertLetterType(self, letterTypeVO):
        db.session.add(letterTypeVO)
        db.session.commit()

    def viewLetterType(self):
        letterTypeVOList = LetterTypeVO.query.all()

        return letterTypeVOList

    def deleteLetterType(self,letterTypeVO):

        letterTypeList = letterTypeVO.query.get(letterTypeVO.letterTypeId)

        db.session.delete(letterTypeList)

        db.session.commit()

        return letterTypeList