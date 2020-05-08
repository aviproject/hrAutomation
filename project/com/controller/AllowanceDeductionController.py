from flask import render_template, request, redirect, url_for
from project import app
from project.com.dao.DesignationDAO import DesignationDAO
from project.com.dao.AllowanceDeductionDAO import AllowanceDeductionDAO
from project.com.vo.AllowanceDeductionVO import AllowanceDeductionVO
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession

@app.route('/admin/loadAllowanceDeduction', methods=['GET'])
def adminLoadAllowanceDeduction():
    try:
        if adminLoginSession() == 'admin':
            designationDAO = DesignationDAO()
            designationVOList = designationDAO.viewDesignation()

            return render_template('admin/addAllowance-Deduction.html', designationVOList=designationVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/insertAllowanceDeduction', methods=['post'])
def adminInsertAllowanceDeduction():
    try:
        if adminLoginSession() == 'admin':
            allowanceDeduction_DesignationId = request.form['allowanceDeduction_DesignationId']
            allowanceDeductionMonth = request.form['allowanceDeductionMonth']
            allowanceDeductionBasicSalary= request.form['allowanceDeductionBasicSalary']
            allowanceDeductionSelect = request.form['allowanceDeductionSelect']
            allowanceDeductionType = request.form['allowanceDeductionType']
            allowanceDeductionLimit=request.form['allowanceDeductionLimit']


            allowanceDeductionVO = AllowanceDeductionVO()
            allowanceDeductionDAO  = AllowanceDeductionDAO()

            allowanceDeductionVO.allowanceDeduction_DesignationId = allowanceDeduction_DesignationId
            allowanceDeductionVO.allowanceDeductionMonth = allowanceDeductionMonth
            allowanceDeductionVO.allowanceDeductionBasicSalary = allowanceDeductionBasicSalary
            allowanceDeductionVO.allowanceDeductionSelect = allowanceDeductionSelect
            allowanceDeductionVO.allowanceDeductionType = allowanceDeductionType
            allowanceDeductionVO.allowanceDeductionLimit=allowanceDeductionLimit


            allowanceDeductionDAO.insertAllowanceDeduction(allowanceDeductionVO)

            return redirect(url_for('adminViewAllowanceDeduction'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/viewAllowanceDeduction', methods=['GET'])
def adminViewAllowanceDeduction():
    try:
        if adminLoginSession() == 'admin':
            allowanceDeductionDAO = AllowanceDeductionDAO()
            allowanceDeductionVOList = allowanceDeductionDAO.viewAllowanceDeduction()

            return render_template('admin/viewAllowance-Deduction.html', allowanceDeductionVOList=allowanceDeductionVOList)

        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/deleteAllowanceDeduction', methods=['GET'])
def adminDeleteAllowanceDeduction():
    try:
        if adminLoginSession() == 'admin':
            allowanceDeductionDAO  = AllowanceDeductionDAO ()

            allowanceDeductionId = request.args.get('allowanceDeductionId')

            allowanceDeductionDAO.deleteAllowanceDeduction(allowanceDeductionId)

            return redirect(url_for('adminViewAllowanceDeduction'))

        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/editAllowanceDeduction', methods=['GET'])
def adminEditAllowanceDeduction():
    try:
        if adminLoginSession() == 'admin':
            allowanceDeductionVO = AllowanceDeductionVO()

            allowanceDeductionDAO  = AllowanceDeductionDAO ()

            designationDAO = DesignationDAO()

            allowanceDeductionId = request.args.get('allowanceDeductionId')

            allowanceDeductionVO.allowanceDeductionId = allowanceDeductionId

            allowanceDeductionVOList = allowanceDeductionDAO.editAllowanceDeduction(allowanceDeductionVO)

            designationVOList = designationDAO.viewDesignation()
            print("view designation")

            return render_template('admin/editAllowance-Deduction.html', designationVOList=designationVOList,
                                   allowanceDeductionVOList=allowanceDeductionVOList)
        else:
            return redirect(url_for('adminLogoutSession'))


    except Exception as ex:
        print(ex)


@app.route('/admin/updateAllowanceDeduction', methods=['POST'])
def adminUpdateAllowanceDeduction():
    try:
        if adminLoginSession() == 'admin':
            allowanceDeductionId = request.form['allowanceDeductionId']
            allowanceDeduction_DesignationId = request.form['allowanceDeduction_DesignationId']
            allowanceDeductionMonth = request.form['allowanceDeductionMonth']
            allowanceDeductionBasicSalary = request.form['allowanceDeductionBasicSalary']
            allowanceDeductionSelect = request.form['allowanceDeductionSelect']
            allowanceDeductionType = request.form['allowanceDeductionType']
            allowanceDeductionLimit = request.form['allowanceDeductionLimit']


            allowanceDeductionVO = AllowanceDeductionVO()
            allowanceDeductionDAO  = AllowanceDeductionDAO ()

            allowanceDeductionVO.allowanceDeductionId =allowanceDeductionId
            allowanceDeductionVO.allowanceDeduction_DesignationId = allowanceDeduction_DesignationId
            allowanceDeductionVO.allowanceDeductionMonth = allowanceDeductionMonth
            allowanceDeductionVO.allowanceDeductionBasicSalary = allowanceDeductionBasicSalary
            allowanceDeductionVO.allowanceDeductionSelect = allowanceDeductionSelect
            allowanceDeductionVO.allowanceDeductionType = allowanceDeductionType
            allowanceDeductionVO.allowanceDeductionLimit = allowanceDeductionLimit


            print("loandetailupdate")

            allowanceDeductionDAO.updateAllowanceDeduction(allowanceDeductionVO)

            return redirect(url_for('adminViewAllowanceDeduction'))

        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)
