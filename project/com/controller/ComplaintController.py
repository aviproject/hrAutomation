import os
from flask import request, render_template, redirect, url_for,session
from werkzeug.utils import secure_filename
from project import app
from datetime import datetime
from project.com.vo.ComplaintVO import ComplaintVO
from project.com.dao.ComplaintDAO import ComplaintDAO
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession




@app.route('/user/loadComplaint',methods=['GET'])
def userLoadComplaint():
    try:
        return render_template('user/addComplaint.html')
    except Exception as ex:
        print(ex)

@app.route('/user/insertComplaint', methods=['POST'])
def userInsertComplaint():
    try:
        print("in complaint controller")
        complaintVO = ComplaintVO()
        complaintDAO = ComplaintDAO()

        UPLOAD_FOLDER = 'project/static/adminResources/complaintFile/'
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

        complaintSubject = request.form['complaintSubject']
        complaintDescription = request.form['complaintDescription']

        now = datetime.now()
        complaintDate = now.strftime("%d/%m/%y")
        complaintTime = now.strftime("%H/%M/%S")

        file = request.files['file']
        print(file)

        complaintFileName = secure_filename(file.filename)
        print(complaintFileName)

        complaintFilePath = os.path.join(app.config['UPLOAD_FOLDER'])
        print("===complaintFilePath===")

        file.save(os.path.join(complaintFilePath, complaintFileName))

        complaintVO.complaintSubject = complaintSubject
        complaintVO.complaintDescription= complaintDescription
        complaintVO.complaintDate = complaintDate
        complaintVO.complaintTime = complaintTime
        complaintVO.complaintStatus = "Pending"
        complaintVO.complaintFileName = complaintFileName

        complaintVO.complaintFilePath = complaintFilePath.replace("project", "..")
        print(":::::::::::::::::::::::::::::::::::::::")

        complaintVO.complaintFrom_loginId = session['session_loginId']
        print("<<<<<<<<<<<>>>>>>>>>>>>>")

        complaintDAO.userInsertComplaint(complaintVO)

        return redirect(url_for('userViewComplaint'))
    except Exception as ex:
        print(ex)

@app.route('/user/viewComplaint')
def userViewComplaint():
    try:
        complaintDAO = ComplaintDAO()
        complaintVO = ComplaintVO()

        complaintFrom_loginId = session['session_loginId']
        print(complaintFrom_loginId)
        complaintVO.complaintFrom_loginId = complaintFrom_loginId
        print("AAAAAAAAAA")
        complaintVOList = complaintDAO.userViewComplaint(complaintVO)

        print("__________________", complaintVOList)
        return render_template('user/viewComplaint.html', complaintVOList=complaintVOList)

    except Exception as ex:
        print(ex)


@app.route("/user/deleteComplaint")
def userDeleteComplaint():
    try:
            complaintDAO = ComplaintDAO()

            complaintId = request.args.get('complaintId')

            complaintVO = ComplaintVO()

            complaintVO.complaintId = complaintId

            complaintList = complaintDAO.userDeleteComplaint(complaintVO)

            complaintFileName = complaintList.complaintFileName
            complaintFilePath = complaintList.complaintFilePath
            path = complaintFilePath.replace("..", "project") + complaintFileName
            os.remove(path)
            if complaintList.complaintStatus == "Replied":
                replyFilePath = complaintList.replyFilePath
                replyFileName = complaintList.replyFileName
                replyPath = replyFilePath.replace("..", "project") + replyFileName
                os.remove(replyPath)
            return redirect(url_for('userViewComplaint'))

    except Exception as ex:
        print(ex)

@app.route('/user/viewComplaintReply',methods=['GET'])
def userViewComplaintReply():
    try:
        complaintVO = ComplaintVO()
        complaintDAO = ComplaintDAO()

        complaintId = request.args.get('complaintId')
        complaintVO.complaintId = complaintId

        complaintReplyList = complaintDAO.viewComplaintReply(complaintVO)

        return render_template('user/viewComplaintReply.html',complaintReplyList=complaintReplyList)
    except Exception as ex:
        print(ex)






'''<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<admin>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''


@app.route('/admin/viewComplaint')
def adminViewComplaint():
    try:
        complaintDAO = ComplaintDAO()
        complaintVO = ComplaintVO()
        complaintVO.complaintStatus = "Pending"

        complaintVOList = complaintDAO.adminViewComplaint(complaintVO)


        return render_template('admin/viewComplaint.html',complaintVOList=complaintVOList)


    except Exception as ex:
        print(ex)

@app.route('/admin/loadComplaintReply',methods=['GET'])
def adminLoadComplaintReply():
    try:
        complaintId = request.args.get("complaintId")
        return render_template('admin/addComplaintReply.html',complaintId=complaintId)

    except Exception as ex:
        print(ex)

@app.route("/admin/insertComplaintReply", methods=['POST'])
def adminInsertComplaintReply():
    try:
        UPLOAD_FOLDER = 'project/static/adminResources/reply/'
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

        complaintDAO = ComplaintDAO()
        complaintVO = ComplaintVO()

        complaintId = request.form['complaintId']
        replySubject = request.form['replySubject']
        replyMessage = request.form['replyMessage']
        replyFile = request.files['replyFile']
        replyFileName = secure_filename(replyFile.filename)
        replyFilePath = os.path.join(app.config['UPLOAD_FOLDER'])
        replyFile.save(os.path.join(replyFilePath, replyFileName))

        now = datetime.now()
        replyDate = now.strftime("%d/%m/%y")
        replyTime = now.strftime("%H:%M:%S")

        complaintVO.complaintId = complaintId
        complaintVO.replySubject = replySubject
        complaintVO.replyMessage = replyMessage
        complaintVO.replyFileName = replyFileName
        complaintVO.replyFilePath = replyFilePath.replace("project", "..")
        complaintVO.replyDate = replyDate
        complaintVO.replyTime = replyTime

        complaintVO.complaintTo_loginId = session['session_loginId']
        complaintVO.complaintStatus = "Replied"

        complaintDAO.adminInsertComplaintReply(complaintVO)

        return redirect(url_for('adminViewComplaint'))
    except Exception as ex:
        print(ex)






