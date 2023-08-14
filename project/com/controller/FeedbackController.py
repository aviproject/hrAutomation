from flask import request, render_template, redirect, url_for,session
from project import app
from datetime import datetime
from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.vo.FeedbackVO import FeedbackVO

@app.route('/user/loadFeedback',methods=['GET'])
def userLoadFeedback():
    try:
        return render_template('user/addFeedback.html')
    except Exception as ex:
        print(ex)

@app.route('/user/insertFeedback', methods=['POST'])
def userinsertFeedback():
    try:
        feedbackVO = FeedbackVO()
        feedbackDAO = FeedbackDAO()

        feedbackSubject = request.form['feedbackSubject']
        feedbackDescription = request.form['feedbackDescription']

        feedbackRating = request.form['feedbackRating']

        now = datetime.now()
        feedbackDate = now.strftime("%d/%m/%y")
        feedbackTime = now.strftime("%H/%M/%S")

        feedbackVO.feedbackSubject = feedbackSubject
        feedbackVO.feedbackDescription = feedbackDescription
        feedbackVO.feedbackRating = feedbackRating
        feedbackVO.feedbackDate = feedbackDate
        feedbackVO.feedbackTime = feedbackTime
        feedbackVO.feedbackFrom_loginId = session['session_loginId']

        feedbackDAO.userinsertFeedback(feedbackVO)
        return redirect(url_for('userViewFeedback'))

    except Exception as ex:
        print(ex)

@app.route('/user/viewFeedback', methods=['GET'])
def userViewFeedback():
    try:
        feedbackDAO = FeedbackDAO()
        feedbackVO = FeedbackVO()

        feedbackFrom_loginId = session['session_loginId']
        feedbackVO.feedbackFrom_loginId = feedbackFrom_loginId
        feedbackVOList = feedbackDAO.userViewFeedback(feedbackVO)

        return render_template('user/viewFeedback.html',feedbackVOList=feedbackVOList)
    except Exception as ex:
        print(ex)

@app.route('/user/deleteFeedback', methods=['GET'])
def userDeleteFeedback():
    try:
        print("in feedback")
        feedbackVO = FeedbackVO()
        feedbackDAO = FeedbackDAO()

        feedbackId = request.args.get('feedbackId')
        print(feedbackId + "#####")

        feedbackVO.feedbackId = feedbackId

        feedbackDAO.deleteFeedback(feedbackVO)


        return redirect(url_for('userViewFeedback'))

    except Exception as ex:
        print(ex)



"""/////////////////admin///////////////////////"""


@app.route('/admin/viewFeedback',methods=['GET'])
def adminViewFeedback():
    try:
            feedbackDAO = FeedbackDAO()
            feedbackVOList = feedbackDAO.adminViewFeedback()
            return render_template('admin/viewFeedback.html',feedbackVOList=feedbackVOList)


    except Exception as ex:
        print(ex)

@app.route('/admin/reviewFeedback',methods=['GET'])
def adminReviewFeedback():
    try:
        feedbackId = request.args.get('feedbackId')
        feedbackTo_loginId = session['session_loginId']

        feedbackVO = FeedbackVO()
        feedbackDAO = FeedbackDAO()

        feedbackVO.feedbackId = feedbackId
        feedbackVO.feedbackTo_loginId = feedbackTo_loginId

        feedbackDAO.adminReviewFeedback(feedbackVO)

        return redirect(url_for('adminViewFeedback'))

    except Exception as ex:
        print(ex)