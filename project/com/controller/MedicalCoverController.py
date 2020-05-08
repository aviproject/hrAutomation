from flask import request, render_template, redirect, url_for
from project import app
from project.com.dao.DesignationDAO import DesignationDAO
from project.com.dao.MedicalCoverDAO import MedicalCoverDAO
from project.com.vo.MedicalCoverVO import MedicalCoverVO
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession

@app.route('/admin/loadMedicalCover', methods=['GET'])
def adminLoadMedicalCover():
    try:
        if adminLoginSession() == 'admin':

            designationDAO = DesignationDAO()
            designationVOList = designationDAO.viewDesignation()

            return render_template('admin/addMedicalCover.html', designationVOList=designationVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/insertMedicalCover', methods=['POST'])
def adminInsertMedicalCover():
    try:
        if adminLoginSession() == 'admin':

            medicalCover_DesignationId = request.form['medicalCover_DesignationId']
            medicalCoverAmount = request.form['medicalCoverAmount']

            medicalCoverVO = MedicalCoverVO()
            medicalCoverDAO = MedicalCoverDAO()

            medicalCoverVO.medicalCover_DesignationId = medicalCover_DesignationId
            medicalCoverVO.medicalCoverAmount = medicalCoverAmount

            medicalCoverDAO.insertMedicalCover(medicalCoverVO)

            return redirect(url_for('adminViewMedicalCover'))

        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/viewMedicalcover', methods=['GET'])
def adminViewMedicalCover():
    try:
        if adminLoginSession() == 'admin':

            medicalCoverDAO = MedicalCoverDAO()

            medicalCoverVoList = medicalCoverDAO.viewMedicalCover()
            print("in medical")

            return render_template('admin/viewMedicalCover.html', medicalCoverVoList=medicalCoverVoList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/deletemedicalCover', methods=['GET'])
def adminDeleteMedicalCover():
    try:
        if adminLoginSession() == 'admin':

            medicalCoverDAO = MedicalCoverDAO()

            medicalCoverId = request.args.get('medicalCoverId')

            medicalCoverDAO.deleteMedicalCover(medicalCoverId)

            return redirect(url_for('adminViewMedicalCover'))
        else:
            return redirect(url_for('adminLogoutSession'))


    except Exception as ex:
        print(ex)


@app.route('/admin/editMedicalCover', methods=['GET'])
def adminEditMedicalCover():
    try:
        if adminLoginSession() == 'admin':
            print("in adminEditMedicalCover")

            medicalCoverVO = MedicalCoverVO()
            medicalCoverDAO = MedicalCoverDAO()

            designationDAO = DesignationDAO()

            medicalCoverId = request.args.get('medicalCoverId')
            print(medicalCoverId)

            medicalCoverVO.medicalCoverId = medicalCoverId

            medicalCoverVOList = medicalCoverDAO.editMedicalCover(medicalCoverVO)

            designationVOList = designationDAO.viewDesignation()

            return render_template('admin/editMedicalCover.html', designationVOList=designationVOList,
                                   medicalCoverVOList=medicalCoverVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/updateMedicalCover', methods=['POST'])
def adminUpdateMedicalCover():
    try:
        if adminLoginSession() == 'admin':
            print("in adminUpdateMedicalCover")

            medicalCover_DesignationId = request.form['medicalCover_DesignationId']
            print(medicalCover_DesignationId)

            medicalCoverId = request.form['medicalCoverId']
            print(medicalCoverId)

            medicalCoverAmount = request.form['medicalCoverAmount']
            print(medicalCoverAmount)

            medicalCoverVO = MedicalCoverVO()
            medicalCoverDAO = MedicalCoverDAO()

            medicalCoverVO.medicalCover_DesignationId = medicalCover_DesignationId

            medicalCoverVO.medicalCoverId = medicalCoverId

            medicalCoverVO.medicalCoverAmount = medicalCoverAmount

            medicalCoverDAO.updateMedicalCover(medicalCoverVO)

            return redirect(url_for('adminViewMedicalCover'))

        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)
