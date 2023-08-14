import os
import boto3
from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime
from project import app
from project.com.dao.LetterTypeDAO import LetterTypeDAO
from project.com.vo.LetterTypeVO import LetterTypeVO
from project.com.controller.LoginController import adminLoginSession,adminLogoutSession

ACCESS_KEY = 'AKIAJ2EH6QCWL5NF4HPQ'
SECRET_KEY = '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'
bucketName = 'myhralexa2020avaneesh'



@app.route('/admin/loadLetterType', methods=['GET'])
def adminLoadLetterType():
    try:
        if adminLoginSession() == 'admin':
            print("in load")
            return render_template('admin/addLetterType.html')
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/insertLetterType', methods=['POST'])
def adminInsertLetterType():
    try:
        if adminLoginSession() == 'admin':
            letterTypeVO = LetterTypeVO()
            letterTypeDAO = LetterTypeDAO()

            UPLOAD_FOLDER = 'project/static/adminResources/lettertype/'
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            letterTypeName = request.form['letterTypeName']
            letterTypeDescription = request.form['letterTypeDescription']
            file = request.files['file']

            letterTypeFileName = secure_filename(file.filename)
            letterTypeFilePath = os.path.join(app.config['UPLOAD_FOLDER'])

            now = datetime.now()

            letterTypeFileUploadDate = now.strftime("%d/%m/%Y")
            letterTypeFileUploadTime = now.strftime("%H:%M:%S")

            file.save(os.path.join(letterTypeFilePath, letterTypeFileName))

            s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

            directoryName = "letterType"

            s3_client.put_object(Bucket=bucketName, Key=(directoryName + '/'))

            s3Resource = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

            expiration = 3600

            s3Resource.meta.client.upload_file(Filename=letterTypeFilePath + letterTypeFileName, Bucket=bucketName,
                                               Key='letterType/{}'.format(letterTypeFileName))

            letterTypeFileObjectURL = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucketName,
                                                                                             'Key': letterTypeFileName},
                                                                       ExpiresIn=expiration)
            letterTypeVO.letterTypeName = letterTypeName
            letterTypeVO.letterTypeDescription = letterTypeDescription

            letterTypeVO.letterTypeFileName = letterTypeFileName

            letterTypeVO.letterTypeFilePath = letterTypeFilePath.replace("project", "..")

            letterTypeVO.letterTypeFileUploadDate = letterTypeFileUploadDate
            letterTypeVO.letterTypeFileUploadTime = letterTypeFileUploadTime

            letterTypeVO.letterTypeFileObjectURL = letterTypeFileObjectURL

            letterTypeDAO.insertLetterType(letterTypeVO)

            return redirect(url_for('adminViewLetterType'))

        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/viewLetterType', methods=['GET'])
def adminViewLetterType():
    try:
        if adminLoginSession() == 'admin':

            letterTypeDAO = LetterTypeDAO()
            letterTypeVOList = letterTypeDAO.viewLetterType()

            print("__________________", letterTypeVOList)

            return render_template('admin/viewLetterType.html', letterTypeVOList=letterTypeVOList)
        else:
            return redirect(url_for('adminLogoutSession'))


    except Exception as ex:
        print(ex)


@app.route('/admin/deleteLetterType', methods=['GET'])
def adminDeleteLetterType():
    try:
        if adminLoginSession() == 'admin':
            letterTypeVO = LetterTypeVO()
            letterTypeDAO = LetterTypeDAO()

            letterTypeVO.letterTypeId = request.args.get('letterTypeId')

            letterTypeList = letterTypeDAO.deleteLetterType(letterTypeVO)
            letterTypeFileName = letterTypeList.letterTypeFileName
            letterTypeFilePath = letterTypeList.letterTypeFilePath

            path = letterTypeFilePath.replace("..", "project") + letterTypeFileName

            os.remove(path)

            s3 = boto3.resource("s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

            directoryName = "letterType"

            object = s3.Object(bucketName, directoryName + '/' + letterTypeFileName)

            object.delete()

            return redirect(url_for('adminViewLetterType'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)