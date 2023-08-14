from project import app
from flask import render_template, session,redirect,url_for
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession


'''@app.route('/user/loadComplaint',methods=['GET'])
def userLoadComplaint():
    try:
        return render_template('user/addComplaint.html')
    except Exception as ex:
        print(ex)'''


'''@app.route('/admin/viewComplaint')
def adminViewComplaint():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/viewComplaint.html')
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)

@app.route('/admin/replyComplaint')
def adminReplyComplaint():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/addComplaintReply.html')
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)
@app.route('/admin/viewFeedback')
def adminViewFeedback():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/viewFeedback.html')
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)'''


'''/////////////////////////user side///////////////////////////////'''




'''@app.route('/user/loadComplaint',methods=['GET'])
def userLoadComplaint():
    try:
        return render_template('user/addComplaint.html')
    except Exception as ex:
        print(ex)'''

'''@app.route('/user/viewComplaint', methods=['GET'])
def userViewComplaint():
    try:
        return render_template('user/viewComplaint.html')
    except Exception as ex:
        print(ex)

@app.route('/user/loadFeedback',methods=['GET'])
def userLoadFeedback():
    try:
        return render_template('user/addFeedback.html')
    except Exception as ex:
        print(ex)

@app.route('/user/viewFeedback', methods=['GET'])
def userViewFeedback():
    try:
        return render_template('user/viewFeedback.html')
    except Exception as ex:
        print(ex)'''

'''@app.route('/user/complaintReply',methods=['get'])
def userComplaintReply():
    try:
        return render_template('user/viewComplaintReply.html')
    except Exception as ex:
        print(ex)'''