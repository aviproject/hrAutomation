from project import app
from flask import request, render_template, redirect, url_for
import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from project.com.controller.LoginController import adminLoginSession, adminLogoutSession
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO
from project.com.dao.DesignationDAO import DesignationDAO
from project.com.dao.DepartmentDAO import DepartmentDAO
from project.com.vo.EmployeeVO import EmployeeVO
from project.com.dao.EmployeeDAO import EmployeeDAO


@app.route('/admin/loadEmployee', methods=['GET'])
def adminLoadEmployee():
    try:
        if adminLoginSession() == 'admin':
            designationDAO = DesignationDAO()
            designationVOList = designationDAO.viewDesignation()

            departmentDAO = DepartmentDAO()
            departmentVOList = departmentDAO.viewDepartment()

            return render_template('admin/addEmployee.html', departmentVOList=departmentVOList,
                                   designationVOList=designationVOList)

        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/insertEmployee', methods=['POST'])
def adminInsertEmployee():
    try:
        if adminLoginSession() == 'admin':
            loginVO = LoginVO()
            loginDAO = LoginDAO()

            loginUsername = request.form['loginUsername']
            loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))


            print("loginPassword=" + loginPassword)

            sender = "enterpriseautomation2020@gmail.com"

            receiver = loginUsername

            msg = MIMEMultipart()

            msg['From'] = sender

            msg['To'] = receiver

            msg['Subject'] = "Enterprise Automation with Conversational Intelligence PASSWORD"

            msg.attach(MIMEText(loginPassword, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()

            server.login(sender, "hrautomation@2020")

            text = msg.as_string()

            server.sendmail(sender, receiver, text)

            loginVO.loginUsername = loginUsername
            loginVO.loginPassword = loginPassword
            loginVO.loginRole = "employee"
            loginVO.loginStatus = "active"

            loginDAO.insertLogin(loginVO)

            employeeFirstName = request.form['employeeFirstName']
            print(employeeFirstName)
            employeeLastName = request.form['employeeLastName']
            employee_DepartmentId = request.form['employee_DepartmentId']
            employee_DesignationId = request.form['employee_DesignationId']
            employeeSalary = request.form['employeeSalary']
            print(employeeSalary)
            employeeContactNumber = request.form['employeeContactNumber']
            employeeAddress = request.form['employeeAddress']
            employeeBirthDate = request.form['employeeBirthDate']
            employeeBloodGroup = request.form['employeeBloodGroup']
            print(employeeBloodGroup)
            employeeMaritalStatus = request.form['employeeMaritalStatus']
            print(employeeMaritalStatus)

            employeeVO = EmployeeVO()
            employeeDAO = EmployeeDAO()

            employeeVO.employeeFirstName = employeeFirstName
            employeeVO.employeeLastName = employeeLastName
            employeeVO.employee_DepartmentId = employee_DepartmentId
            employeeVO.employee_DesignationId = employee_DesignationId
            employeeVO.employeeSalary = employeeSalary
            employeeVO.employeeContactNumber = employeeContactNumber
            employeeVO.employeeAddress = employeeAddress
            employeeVO.employeeBirthDate = employeeBirthDate
            employeeVO.employeeBloodGroup = employeeBloodGroup
            employeeVO.employeeMaritalStatus = employeeMaritalStatus
            employeeVO.employee_loginId = loginVO.loginId

            print("in Login")

            employeeDAO.insertEmployee(employeeVO)

            server.quit()
            return redirect(url_for('adminViewEmployee'))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/viewEmployee', methods=['GET'])
def adminViewEmployee():
    try:
        if adminLoginSession() == 'admin':
            employeeDAO = EmployeeDAO()
            employeeVOList = employeeDAO.viewEmployee()
            return render_template('admin/viewEmployee.html', employeeVOList=employeeVOList)
        else:
            print("@@@@@@@@@@@@@@@@@@@@@")
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/deleteEmployee', methods=['GET'])
def adminDeleteEmployee():
    try:
        if adminLoginSession() == 'admin':

            employeeDAO = EmployeeDAO()
            employeeVO = EmployeeVO()


            employeeId = request.args.get('employeeId')
            employeeVO.employeeId = employeeId

            loginDAO = LoginDAO()
            loginVO = LoginVO()

            loginId = request.args.get('loginId')
            loginVO.loginId = loginId

            employeeDAO.deleteEmployee(employeeVO)
            loginDAO.deleteLogin(loginVO)

            return redirect(url_for('adminViewEmployee'))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/editEmployee', methods=['GET'])
def adminEditEmployee():
    try:
        if adminLoginSession() == 'admin':
            employeeVO = EmployeeVO()

            employeeDAO = EmployeeDAO()

            departmentDAO = DepartmentDAO()

            designationDAO = DesignationDAO()

            employeeId = request.args.get('employeeId')

            employeeVO.employeeId = employeeId

            employeeVOList = employeeDAO.editEmployee(employeeVO)
            departmentVOList = departmentDAO.viewDepartment()
            designationVOList = designationDAO.viewDesignation()
            print("view designation")

            return render_template('admin/editEmployee.html', departmentVOList=departmentVOList,
                                   designationVOList=designationVOList,
                                   employeeVOList=employeeVOList)
        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/admin/updateEmployee', methods=['POST'])
def adminUpdateEmployee():
    try:
        if adminLoginSession() == 'admin':

            loginUsername = request.form['loginUsername']
            loginId = request.form['loginId']

            employeeId = request.form['employeeId']
            employeeFirstName = request.form['employeeFirstName']
            employeeLastName = request.form['employeeLastName']
            employee_DepartmentId = request.form['employee_DepartmentId']
            employee_DesignationId = request.form['employee_DesignationId']
            employeeSalary = request.form['employeeSalary']


            employeeContactNumber = request.form['employeeContactNumber']
            employeeAddress = request.form['employeeAddress']
            employeeBirthDate = request.form['employeeBirthDate']
            employeeBloodGroup = request.form['employeeBloodGroup']
            employeeMaritalStatus = request.form['employeeMaritalStatus']

            employeeVO = EmployeeVO()
            employeeDAO = EmployeeDAO()
            loginVO = LoginVO()
            loginDAO = LoginDAO()

            loginVO.loginId = loginId
            loginList = loginDAO.viewLogin(loginVO)

            if loginList[0].loginUsername == loginUsername:
                pass
            else:
                loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))

                print("loginPassword=" + loginPassword)

                sender = "enterpriseautomation2020@gmail.com"

                receiver = loginUsername

                msg = MIMEMultipart()

                msg['From'] = sender

                msg['To'] = receiver

                msg['Subject'] = "Enterprise Automation with Conversational Intelligence PASSWORD"

                msg.attach(MIMEText(loginPassword, 'plain'))

                server = smtplib.SMTP('smtp.gmail.com', 587)

                server.starttls()

                server.login(sender, "hrautomation@2020")

                text = msg.as_string()

                server.sendmail(sender, receiver, text)

                loginVO.loginUsername = loginUsername
                loginVO.loginPassword = loginPassword

                loginDAO.updateLogin(loginVO)


            employeeVO.employeeId = employeeId
            employeeVO.employeeFirstName = employeeFirstName
            employeeVO.employeeLastName = employeeLastName
            employeeVO.employee_DepartmentId = employee_DepartmentId
            employeeVO.employee_DesignationId = employee_DesignationId
            employeeVO.employeeSalary = employeeSalary

            employeeVO.employeeContactNumber = employeeContactNumber
            employeeVO.employeeAddress = employeeAddress
            employeeVO.employeeBirthDate= employeeBirthDate
            employeeVO.employeeBloodGroup = employeeBloodGroup
            employeeVO.employeeMaritalStatus = employeeMaritalStatus
            print("loandetailupdate")

            employeeDAO.updateEmployee(employeeVO)

            return redirect(url_for('adminViewEmployee'))
        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)
