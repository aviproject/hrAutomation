import os
from datetime import datetime
from datetime import date



from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import boto3
from project import app
from project.com.dao.AttendanceDAO import AttendanceDAO
from project.com.vo.AttendanceVO import AttendanceVO
from project.com.dao.DesignationDAO import DesignationDAO
from project.com.dao.DepartmentDAO import DepartmentDAO
from project.com.dao.EmployeeDAO import EmployeeDAO
from project.com.vo.EmployeeVO import EmployeeVO

from project.com.controller.LoginController import adminLoginSession, adminLogoutSession

ACCESS_KEY = 'AKIAJ2EH6QCWL5NF4HPQ'
SECRET_KEY = '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'
bucketName = 'myhralexa2020avaneesh'




@app.route('/admin/loadAttendance', methods=['GET'])
def adminLoadAttendance():
    try:
        if adminLoginSession() == 'admin':
            print("in load")

            departmentDAO = DepartmentDAO()
            departmentVOList = departmentDAO.viewDepartment()
            print("GGGGGGGGGG")

            designationDAO = DesignationDAO()
            designationVOList = designationDAO.viewDesignation()
            print("KKKKKKKKKKK")

            employeeDAO = EmployeeDAO()
            employeeVOList = employeeDAO.viewEmployee()


            print("MMMMMMMMMM")

            return render_template('admin/addAttendance.html',departmentVOList=departmentVOList,
                                                              designationVOList=designationVOList,
                                                              employeeVOList=employeeVOList)
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/admin/insertAttendance', methods=['POST'])
def adminInsertAttendance():
    try:
        if adminLoginSession() == 'admin':
            attendanceVO = AttendanceVO()
            attendanceDAO = AttendanceDAO()

            #UPLOAD_FOLDER = 'project/static/adminResources/attendance/'
            #app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            attendance_DepartmentId = request.form['attendance_DepartmentId']
            attendance_DesignationId = request.form['attendance_DesignationId']

            attendance_EmployeeId = request.form['attendance_EmployeeId']
            print("IDIDIDIDIDI")
            print(attendance_EmployeeId)


            employeeVO = EmployeeVO()
            employeeDAO = EmployeeDAO()

            employeeVO.employeeId = attendance_EmployeeId
            employeeVOList = employeeDAO.viewAttendanceEmployee(employeeVO)
            print("employeeVOList",employeeVOList)

            username = employeeVOList[0][1].loginUsername
            UPLOAD_FOLDER = "project/static/adminResources/{}/attendance/".format(username)
            path1 = 'project/static/adminResources/{}'.format(username)
            if not os.path.exists(UPLOAD_FOLDER):

                os.mkdir(path1)
                path2 = '{}/attendance/'.format(path1)
                os.mkdir(path2)

            UPLOAD_FOLDER = "project/static/adminResources/{}/attendance/".format(username)
            #UPLOAD_FOLDER=os.mkdir('{}/{}/'.format(UPLOAD_FOLDER,username))
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            attendanceMonth = request.form['attendanceMonth']
            print(attendanceMonth)

            file = request.files['file']
            print(file)

            attendanceFileName = secure_filename(file.filename)
            print(attendanceFileName)

            attendanceFilePath = os.path.join(app.config['UPLOAD_FOLDER'])
            print(attendanceFilePath)

            now = datetime.now()

            attendanceFileUploadDate = now.strftime("%d/%m/%y")
            print(attendanceFileUploadDate)

            attedanceFileUploadTime = now.strftime("%H/%M/%S")
            print(attedanceFileUploadTime)

            file.save(os.path.join(attendanceFilePath, attendanceFileName))
            print("??????????????????")

            s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

            directoryName = username + "/attendance"

            s3_client.put_object(Bucket=bucketName, Key=(directoryName + '/'))

            s3Resource = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

            expiration = 3600

            s3Resource.meta.client.upload_file(Filename=attendanceFilePath + attendanceFileName, Bucket=bucketName,
                                               Key='{}/attendance/{}'.format(username ,attendanceFileName))

            attendanceFileObjectURL = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucketName,
                                                                                             'Key': attendanceFileName},
                                                                       ExpiresIn=expiration)


            attendanceVO.attendance_DepartmentId = attendance_DepartmentId
            attendanceVO.attendance_DesignationId = attendance_DesignationId
            attendanceVO.attendance_EmployeeId = attendance_EmployeeId
            attendanceVO.attendanceMonth = attendanceMonth
            attendanceVO.attendanceFileName = attendanceFileName
            attendanceVO.attendanceFilePath = attendanceFilePath.replace("project", "..")
            attendanceVO.attendanceFileUploadDate = attendanceFileUploadDate
            attendanceVO.attendanceFileUploadTime = attedanceFileUploadTime
            attendanceVO.attendanceFileObjectURL = attendanceFileObjectURL

            attendanceDAO.insertAttendance(attendanceVO)
            print("UUUUUUUUUU")

            return redirect(url_for('adminViewAttendance'))

        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/viewAttendance', methods=['GET'])
def adminViewAttendance():
    try:
        if adminLoginSession() == 'admin':

            print("in attendanceView ")

            attendanceDAO = AttendanceDAO()

            print("just before search queryyyy........1!!!!")
            attendanceVOList = attendanceDAO.viewAttendance()

            print("in viewAttendance")

            return render_template('admin/viewAttendance.html', attendanceVOList=attendanceVOList)

        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/deleteAttendance', methods=['GET'])
def adminDeleteAttendance():
    try:
        if adminLoginSession() == 'admin':

            print("delete Attedance")

            attendanceVO = AttendanceVO()
            attendanceDAO = AttendanceDAO()

            employeeVO = EmployeeVO()
            employeeDAO = EmployeeDAO()


            attendanceVO.attendanceId = request.args.get('attendanceId')
            print("attendance Id",attendanceVO.attendanceId)

            attendanceVOList = attendanceDAO.deleteAttendance(attendanceVO)

            print("complete deleteattendance",attendanceVOList)
            attendance_EmployeeId = attendanceVOList.attendance_EmployeeId


            employeeVO.employeeId = attendance_EmployeeId
            employeeVOList  = employeeDAO.viewAttendanceEmployee(employeeVO)
            username = employeeVOList[0][1].loginUsername

            print("attendance path")

            attendanceFileName = attendanceVOList.attendanceFileName
            attendanceFilePath = attendanceVOList.attendanceFilePath

            path = attendanceFilePath.replace("..", "project") + attendanceFileName
            print("my attendance path")

            os.remove(path)
            print("remove localpath")

            s3 = boto3.resource("s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

            directoryName = username + "/attendance"

            object = s3.Object(bucketName,directoryName + '/' + attendanceFileName)
            print("object",object)

            object.delete()

            return redirect(url_for('adminViewAttendance'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)
