from flask import request, render_template, redirect, url_for
from project import app
from project.com.dao.LeaveDAO import LeaveDAO
from project.com.vo.LeaveVO import LeaveVO
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession

@app.route('/admin/loadLeave', methods=['GET'])
def adminLoadLeave():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/addLeave.html')
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/insertLeave', methods=['POST'])
def adminInsertLeave():
    try:
        if adminLoginSession() == 'admin':
            leaveType = request.form['leaveType']
            noOfDay = request.form['noOfDay']
            leaveDescription = request.form['leaveDescription']

            print(leaveType, noOfDay, leaveDescription)

            leaveVO = LeaveVO()
            leaveDAO = LeaveDAO()

            leaveVO.leaveType = leaveType
            leaveVO.noOfDay = noOfDay
            leaveVO.leaveDescription = leaveDescription

            leaveDAO.insertLeave(leaveVO)

            return redirect(url_for('adminViewLeave'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/viewLeave', methods=['GET'])
def adminViewLeave():
    try:
        if adminLoginSession() == 'admin':
            leaveDAO = LeaveDAO()
            leaveVOList = leaveDAO.viewLeave()
            print("__________________", leaveVOList)
            return render_template('admin/viewLeave.html', leaveVOList=leaveVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/deleteLeave', methods=['GET'])
def adminDeleteLeave():
    try:
        if adminLoginSession() == 'admin':
            leaveVO = LeaveVO()

            leaveDAO = LeaveDAO()

            leaveId = request.args.get('leaveId')

            leaveVO.leaveId = leaveId

            leaveDAO.deleteLeave(leaveVO)

            return redirect(url_for('adminViewLeave'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/editLeave', methods=['GET'])
def adminEditLeave():
    try:
        if adminLoginSession() == 'admin':
            leaveVO = LeaveVO()

            leaveDAO = LeaveDAO()

            leaveId = request.args.get('leaveId')

            leaveVO.leaveId = leaveId

            leaveVOList = leaveDAO.editLeave(leaveVO)

            print("=======leaveVOList=======", leaveVOList)

            print("=======type of leaveVOList=======", type(leaveVOList))

            return render_template('admin/editLeave.html', leaveVOList=leaveVOList)

        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/updateLeave', methods=['POST'])
def adminUpdateLeave():
    try:
        if adminLoginSession() == 'admin':
            leaveId = request.form['leaveId']
            leaveType = request.form['leaveType']
            noOfDay = request.form['noOfDay']
            leaveDescription = request.form['leaveDescription']

            leaveVO = LeaveVO()
            leaveDAO = LeaveDAO()

            leaveVO.leaveId = leaveId
            leaveVO.leaveType = leaveType
            leaveVO.noOfDay = noOfDay
            leaveVO.leaveDescription = leaveDescription

            leaveDAO.updateLeave(leaveVO)

            return redirect(url_for('adminViewLeave'))
        else:
            return redirect(url_for('adminLogoutSession'))


    except Exception as ex:
        print(ex)
