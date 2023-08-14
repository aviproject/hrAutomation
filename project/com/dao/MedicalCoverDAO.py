from project import db
from  project.com.vo.MedicalCoverVO import MedicalCoverVO
from  project.com.vo.DesignationVO import DesignationVO

class MedicalCoverDAO():
    def insertMedicalCover(self,medicalCoverVO):

        db.session.add(medicalCoverVO)

        db.session.commit()

    def viewMedicalCover(self):

        medicalCoverList = db.session.query(MedicalCoverVO,DesignationVO).join(DesignationVO,MedicalCoverVO.medicalCover_DesignationId == DesignationVO.designationId).all()
        print(medicalCoverList)
        return medicalCoverList

    def deleteMedicalCover(self,medicalCoverId):

        medicalCoverList = MedicalCoverVO.query.get(medicalCoverId)

        db.session.delete(medicalCoverList)

        db.session.commit()

    def editMedicalCover(self, medicalCoverVO):

        medicalCoverList = medicalCoverVO.query.filter_by(medicalCoverId=medicalCoverVO.medicalCoverId)

        return medicalCoverList

    def updateMedicalCover(self, medicalCoverVO):

        db.session.merge(medicalCoverVO)

        db.session.commit()





