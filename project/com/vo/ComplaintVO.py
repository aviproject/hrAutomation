from project import db
from project.com.vo.LoginVO import LoginVO


class ComplaintVO(db.Model):
    __tablename__ = 'complaintmaster'
    complaintId = db.Column('complaintId',db.Integer,primary_key=True,autoincrement=True)
    complaintSubject = db.Column('complaintSubject',db.String(30),nullable=False)
    complaintDescription = db.Column('complaintDescription', db.String(600),nullable=False)
    complaintDate = db.Column('complaintDate', db.String(30),nullable=False)
    complaintTime = db.Column('complaintTime', db.String(30),nullable=False)
    complaintStatus = db.Column('complaintStatus', db.String(30),nullable=False)
    complaintFileName = db.Column('complaintFileName', db.String(50),nullable=False)
    complaintFilePath = db.Column('complaintFilePath', db.String(200),nullable=False)
    complaintTo_loginId = db.Column('complaintTo_loginId', db.Integer,db.ForeignKey(LoginVO.loginId))
    complaintFrom_loginId = db.Column('complaintFrom_loginId', db.Integer,db.ForeignKey(LoginVO.loginId))
    replySubject = db.Column('replySubject',db.String(30))
    replyMessage = db.Column('replyMessage',db.String(200))
    replyFileName = db.Column('replyFileName',db.String(50))

    replyFilePath = db.Column('replyFilePath',db.String(200))

    replyDate = db.Column('replyDate',db.String(20))
    replyTime = db.Column('replyTime',db.String(20))

    def as_dict(self):
        return {
            'complaintId': self.complaintId,
            'complaintSubject': self.complaintSubject,
            'complaintDescription': self.complaintDescription,
            'complaintDate': self.complaintDate,
            'complaintTime': self.complaintTime,
            'complaintStatus': self.complaintStatus,
            'complaintFileName': self.complaintFileName,
            'complaintFilePath': self.complaintFilePath,
            'complaintTo_loginId': self.complaintTo_loginId,
            'complaintFrom_loginId': self.complaintFrom_loginId,
            'replySubject': self.replySubject,
            'replyMessage': self.replyMessage,
            'replyFileName': self.replyFileName,
            'replyFilePath': self.replyFilePath,
            'replyDate': self.replyDate,
            'replyTime': self.replyTime
        }
db.create_all()


