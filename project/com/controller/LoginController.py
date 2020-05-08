from flask import request, render_template, redirect, url_for, session
from project import app
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO


@app.route('/',methods=['GET'])
def adminLoadLogin():
    try:
        session.clear()
        return render_template('admin/login.html')
    except Exception as ex:
        print(ex)


@app.route('/admin/validateLogin', methods=['POST'])
def adminValidateLogin():
    try:
        loginUsername = request.form['loginUsername']

        loginPassword = request.form['loginPassword']

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        loginVO.loginUsername = loginUsername
        loginVO.loginPassword = loginPassword
        loginVO.loginStatus = "active"

        print("in active")

        loginVOList = loginDAO.validateLogin(loginVO)

        print(loginVOList)

        loginDictList = [i.as_dict() for i in loginVOList]

        print("loginDictList", loginDictList)

        lenLoginDictList = len(loginDictList)

        if lenLoginDictList == 0:

            msg = 'Username Or Password is Incorrect !'

            return render_template('admin/login.html', error=msg)

        else:
            for row1 in loginDictList:

                loginId = row1['loginId']

                loginUsername = row1['loginUsername']

                loginRole = row1['loginRole']

                session['session_loginId'] = loginId

                session['session_loginUsername'] = loginUsername

                session['session_loginRole'] = loginRole

                session.permanent = True

                if loginRole == 'admin':
                    return redirect(url_for('adminLoadDashboard'))
                elif loginRole == 'employee':
                    return redirect(url_for('userLoadDashboard'))
                else:
                    return render_template('admin/login.html')

    except Exception as ex:
        print(ex)


@app.route('/admin/loadDashboard', methods=['GET'])
def adminLoadDashboard():
    try:
        if adminLoginSession() == 'admin':

            return render_template('admin/index.html')
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)

@app.route('/user/loadDashboard', methods=['GET'])
def userLoadDashboard():
    try:
        return render_template('user/index.html')
    except Exception as ex:
        print(ex)

@app.route('/admin/loginSession')

def adminLoginSession():
    try:
        if 'session_loginId' and 'session_loginRole' in session:

            if session['session_loginRole'] == 'admin':
                return 'admin'
            elif session['session_loginRole'] == 'user':
                return 'user'

            print("<<<<<<<<True>>>>>>>")

        else:

            print("<<<<<<False>>>>>>")

            return False
    except Exception as ex:
        print(ex)

@app.route("/admin/logoutSession", methods=['GET'])
def adminLogoutSession():
    try:
        session.clear()
        return redirect(url_for('adminLoadLogin'))
    except Exception as ex:
        print(ex)