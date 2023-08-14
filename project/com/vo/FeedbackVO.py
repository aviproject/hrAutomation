from project import db
from project.com.vo.LoginVO import LoginVO

class FeedbackVO(db.Model):
    __tablename__ = 'feedbackmaster'
    feedbackId = db.Column('feedbackId',db.Integer,primary_key=True,autoincrement=True)
    feedbackSubject = db.Column('feedbackSubject',db.String(100),nullable=False)
    feedbackDescription = db.Column('feedbackDescription',db.String(700),nullable=False)
    feedbackRating = db.Column('feedbackRating',db.String(30),nullable=False)
    feedbackDate = db.Column('feedbackDate',db.String(30),nullable=False)
    feedbackTime = db.Column('feedbackTime', db.String(30), nullable=False)
    feedbackTo_loginId = db.Column('feedbackTo_loginId',db.Integer,db.ForeignKey(LoginVO.loginId))
    feedbackFrom_loginId = db.Column('feedbackFrom_loginId',db.Integer,db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'feedbackId': self.feedbackId,
            'feedbackSubject':self.feedbackSubject,
            'feedbackDescription': self.feedbackDescription,
            'feedbackRating': self.feedbackRating,
            'feedbackDate': self.feedbackDate,
            'feedbackTime': self.feedbackTime,
            'feedbackTo_loginId': self.feedbackTo_loginId,
            'feedbackFrom_loginId':self.feedbackFrom_loginId
        }
db.create_all()