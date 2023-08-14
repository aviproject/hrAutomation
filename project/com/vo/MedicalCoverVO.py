from  project import db
from project.com.vo.DesignationVO import DesignationVO

class MedicalCoverVO(db.Model):
    __tablename__='medicalcovermaster'
    medicalCoverId=db.Column('medicalCoverId',db.INTEGER,primary_key=True,autoincrement=True)
    medicalCover_DesignationId = db.Column('medicalCover_DesignationId', db.Integer, db.ForeignKey(DesignationVO.designationId))
    medicalCoverAmount=db.Column('medicalCoverAmount',db.INTEGER)

    def as_dict(self):
        return {
            'medicalCoverId': self.medicalCoverId,
            'medicalCover_DesignationId': self.medicalCover_DesignationId,
            'medicalCoverAmount': self.medicalCoverAmount
        }


db.create_all()