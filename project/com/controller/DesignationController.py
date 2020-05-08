from project import app
from flask import render_template, request, redirect, url_for
from project.com.vo.DesignationVO import DesignationVO  # import the DesignationVO class
from project.com.dao.DesignationDAO import DesignationDAO  # import the DesignationVO class
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession


# load the addDesignation page
@app.route('/admin/loadDesignation', methods=['GET'])
def adminLoadDesignation():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/addDesignation.html')
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


# insert the designationName and designationDescription in the addDesignation page
@app.route('/admin/insertDesignation', methods=['POST'])
def adminInsertDesignation():
    try:
        if adminLoginSession() == 'admin':
            designationName = request.form['designationName']  # create the variable designationName
            designationDescription = request.form[
                'designationDescription']  # create the variable designationDescription

            designationVO = DesignationVO()  # create the object of DesignationVO
            designationDAO = DesignationDAO()  # create the object of DesignationDAO

            designationVO.designationName = designationName
            designationVO.designationDescription = designationDescription

            designationDAO.insertDesignation(designationVO)  # go on insertDesignation

            return redirect(url_for('adminViewDesignation'))  # go on adminViewDesignation method of DesignationDAO class
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


# view the designationName and designationDescription on viewDesignation page
@app.route('/admin/viewDesignation', methods=['GET'])
def adminViewDesignation():
    try:
        if adminLoginSession() == 'admin':

            designationDAO = DesignationDAO()
            designationtVOList = designationDAO.viewDesignation()  # viewDesignation is function of DesignationVO class
            print("__________________", designationtVOList)
            return render_template('admin/viewDesignation.html', designationVOList=designationtVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:

        print(ex)


# delete the designationName and designationDescription
@app.route('/admin/deleteDesignation', methods=['GET'])
def adminDeleteDesignation():
    try:
        if adminLoginSession() == 'admin':

            designationVO = DesignationVO()
            designationDAO = DesignationDAO()

            designationId = request.args.get('designationId')
            print(designationId)
            designationVO.designationId = designationId

            designationDAO.deleteDesignation(designationVO)
            print("delete ok")
            # go on deleteDesignation method of DesignationDAO class

            return redirect(url_for('adminViewDesignation'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


# edit the designationName and designationDescription
@app.route('/admin/editDesignation', methods=['GET'])
def adminEditDesignation():
    try:
        if adminLoginSession() == 'admin':
            designationVO = DesignationVO()
            designationDAO = DesignationDAO()

            designationId = request.args.get('designationId')
            designationVO.designationId = designationId
            designationVOList = designationDAO.editDesignation(designationVO)

            print("=======designationVOList=======", designationVOList)

            print("=======type of designationVOList=======", type(designationVOList))

            return render_template('admin/editDesignation.html', designationVOList=designationVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


# update the designationName and designationDescription
@app.route('/admin/updateDesignation', methods=['POST'])
def adminUpdateDesignation():
    try:
        if adminLoginSession() == 'admin':
            designationId = request.form['designationId']
            designationName = request.form['designationName']
            designationDescription = request.form['designationDescription']

            designationVO = DesignationVO()
            designationDAO = DesignationDAO()

            designationVO.designationId = designationId
            designationVO.designationName = designationName
            designationVO.designationDescription = designationDescription

            designationDAO.updateDesignation(designationVO)

            return redirect(url_for('adminViewDesignation'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)
