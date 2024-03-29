from project import db
from project.com.vo.FeedbackVO import FeedbackVO
from project.com.vo.LoginVO import LoginVO
class FeedbackDAO:

    def userinsertFeedback(self,feedbackVO):
        db.session.add(feedbackVO)
        db.session.commit()

    def userViewFeedback(self,feedbackVO):

        feedbackList = FeedbackVO.query.filter_by(feedbackFrom_loginId=feedbackVO.feedbackFrom_loginId).all()
        return feedbackList

    def deleteFeedback(self,feedbackVO):

        feedbackList = FeedbackVO.query.get(feedbackVO.feedbackId)
        db.session.delete(feedbackList)
        db.session.commit()

    def adminViewFeedback(self):
        feedbackVOList = db.session.query(FeedbackVO, LoginVO). \
            join(LoginVO, FeedbackVO.feedbackFrom_loginId == LoginVO.loginId)

        return feedbackVOList

    def adminReviewFeedback(self,feedbackVO):
        db.session.merge(feedbackVO)
        db.session.commit()