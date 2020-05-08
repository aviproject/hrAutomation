from  project import db
from project.com.vo.DesignationVO import DesignationVO


class LoanDetailVO(db.Model):
    __tablename__ = 'loandetailmaster'
    loanDetailId = db.Column('loanDetailId', db.INTEGER, primary_key=True, autoincrement=True)
    loanDetail_DesignationId = db.Column('loanDetail_DesignationId', db.Integer,
                                         db.ForeignKey(DesignationVO.designationId))
    maximumLoanLimit = db.Column('maximumLoanLimit', db.INTEGER)
    loanTimeLimit = db.Column('loanTimeLimit', db.INTEGER)
    loanInterestRate = db.Column('loanInterestRate', db.INTEGER)

    def as_dict(self):
        return {
            'loanDetailId': self.loanDetailId,
            'loanDetail_DesignationId': self.loanDetail_DesignationId,
            'maximumLoanLimit': self.maximumLoanLimit,
            'loanTimeLimit': self.loanTimeLimit,
            'loanInterestRate': self.loanInterestRate
        }


db.create_all()
