from flask import render_template, request, redirect, url_for
from project import app
from project.com.dao.DesignationDAO import DesignationDAO
from project.com.dao.LoanDetailDAO import LoanDetailDAO
from project.com.vo.LoanDetailVO import LoanDetailVO
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession

@app.route('/admin/loadLoanDetail', methods=['GET'])
def adminLoadLoanDetail():
    try:
        if adminLoginSession() == 'admin':
            designationDAO = DesignationDAO()
            designationVOList = designationDAO.viewDesignation()

            return render_template('admin/addLoanDetail.html',designationVOList=designationVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/insertLoanDetail', methods=['post'])
def adminInsertLoanDetail():
    try:
        if adminLoginSession() == 'admin':
            loanDetail_DesignationId = request.form['loanDetail_DesignationId']
            maximumLoanLimit = request.form['maximumLoanLimit']
            loanTimeLimit = request.form['loanTimeLimit']
            print(loanTimeLimit)
            loanInterestRate = request.form['loanInterestRate']

            loanDetailVO = LoanDetailVO()
            loanDetailDAO = LoanDetailDAO()

            loanDetailVO.loanDetail_DesignationId = loanDetail_DesignationId
            loanDetailVO.maximumLoanLimit = maximumLoanLimit
            loanDetailVO.loanTimeLimit = loanTimeLimit
            loanDetailVO.loanInterestRate = loanInterestRate

            loanDetailDAO.insertLoanDetail(loanDetailVO)

            return redirect(url_for('adminViewLoanDetail'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/viewLoanDetail', methods=['GET'])
def adminViewLoanDetail():
    try:
        if adminLoginSession() == 'admin':
            loanDetailDAO = LoanDetailDAO()
            loanDetailVOList = loanDetailDAO.viewLoanDetail()

            return render_template('admin/viewLoanDetail.html', loanDetailVOList=loanDetailVOList)
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/admin/deleteLoanDetail', methods=['GET'])
def adminDeleteLoanDetail():
    try:
        if adminLoginSession() == 'admin':
            loanDetailDAO = LoanDetailDAO()

            loanDetailId = request.args.get('loanDetailId')

            loanDetailDAO.deleteLoanDetail(loanDetailId)

            return redirect(url_for('adminViewLoanDetail'))

        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/admin/editLoanDetail', methods=['GET'])
def adminEditLoanDetail():
    try:
        if adminLoginSession() == 'admin':

            loanDetailVO = LoanDetailVO()
            loanDetailDAO = LoanDetailDAO()
            designationDAO = DesignationDAO()

            loanDetailId = request.args.get('loanDetailId')

            loanDetailVO.loanDetailId = loanDetailId

            loanDetailVOList = loanDetailDAO.editLoanDetail(loanDetailVO)

            designationVOList = designationDAO.viewDesignation()

            return render_template('admin/editLoanDetail.html', designationVOList=designationVOList,
                                   loanDetailVOList=loanDetailVOList)

        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/admin/updateLoanDetail', methods=['POST'])
def adminUpdateLoanDetail():
    try:
        if adminLoginSession() == 'admin':

            print("adminUpdateLoanDetail")

            loanDetail_DesignationId = request.form['loanDetail_DesignationId']
            print(loanDetail_DesignationId)

            loanDetailId = request.form['loanDetailId']
            print(loanDetailId)

            maximumLoanLimit = request.form['maximumLoanLimit']
            print(maximumLoanLimit)

            loanTimeLimit = request.form['loanTimeLimit']
            print(loanTimeLimit)

            loanInterestRate = request.form['loanInterestRate']
            print(loanInterestRate)



            loanDetailVO = LoanDetailVO()
            loanDetailDAO = LoanDetailDAO()

            loanDetailVO.loanDetailId = loanDetailId
            loanDetailVO.loanDetail_DesignationId = loanDetail_DesignationId
            loanDetailVO.maximumLoanLimit = maximumLoanLimit
            loanDetailVO.loanTimeLimit = loanTimeLimit
            loanDetailVO.loanInterestRate = loanInterestRate

            loanDetailDAO.updateLoanDetail(loanDetailVO)

            return redirect(url_for('adminViewLoanDetail'))

        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)
