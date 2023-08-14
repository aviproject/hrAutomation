from project import db
from project.com.vo.DesignationVO import DesignationVO

class AllowanceDeductionVO(db.Model):
    __tablename__ = 'allowancedeductionmaster'
    allowanceDeductionId= db.Column('allowanceDeductionId', db.Integer, primary_key=True, autoincrement=True)
    allowanceDeduction_DesignationId= db.Column('allowanceDeduction_DesignationId',db.Integer, db.ForeignKey(DesignationVO.designationId))
    allowanceDeductionMonth = db.Column('allowanceDeductionMonth', db.String(20))
    allowanceDeductionBasicSalary = db.Column('allowanceDeductionBasicSalary', db.INTEGER)
    allowanceDeductionSelect= db.Column('allowanceDeductionSelect', db.String(200))
    allowanceDeductionType= db.Column('allowanceDeductionType', db.String(200))
    allowanceDeductionLimit=db.Column('allowanceDeductionLimit',db.INTEGER)


    def as_dict(self):
        return {
            'allowanceDeductionId':self.allowanceDeductionId,
            'allowanceDeduction_DesignationId':self.allowanceDeduction_DesignationId,
            'allowanceDeductionMonth': self.allowanceDeductionMonth,
            'allowanceDeductionBasicSalary': self.allowanceDeductionBasicSalary,
            'allowanceDeductionSelect': self.allowanceDeductionSelect,
            'allowanceDeductionType': self.allowanceDeductionType,
            'allowanceDeductionLimit': self.allowanceDeductionLimit,

        }
db.create_all()
