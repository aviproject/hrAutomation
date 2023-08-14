from flask import render_template, request, redirect, url_for
from project import app
from project.com.dao.DepartmentDAO import DepartmentDAO
from project.com.vo.DepartmentVO import DepartmentVO
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession


@app.route('/admin/loadDepartment', methods=['GET'])
def adminLoadDepartment():
    try:
        if adminLoginSession() == 'admin':

            return render_template('admin/addDepartment.html')
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/admin/insertDepartment', methods=['POST'])
def adminInsertDepartment():
    try:
        if adminLoginSession() == 'admin':

            departmentName = request.form['departmentName']
            departmentDescription = request.form['departmentDescription']

            departmentVO = DepartmentVO()
            departmentDAO = DepartmentDAO()

            departmentVO.departmentName = departmentName
            departmentVO.departmentDescription = departmentDescription

            print(departmentVO.departmentName)

            departmentDAO.insertDepartment(departmentVO)

            return redirect(url_for('adminViewDepartment'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/viewDepartment', methods=['GET'])
def adminViewDepartment():
    try:
        if adminLoginSession() == 'admin':
            departmentDAO = DepartmentDAO()
            departmentVOList = departmentDAO.viewDepartment()
            print("__________________", departmentVOList)

            return render_template('admin/viewDepartment.html', departmentVOList=departmentVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/deleteDepartment', methods=['GET'])
def adminDeleteDepartment():
    try:
        if adminLoginSession() == 'admin':
            departmentVO = DepartmentVO()

            departmentDAO = DepartmentDAO()

            departmentId = request.args.get('departmentId')

            departmentVO.departmentId = departmentId

            departmentDAO.deleteDepartment(departmentVO)

            return redirect(url_for('adminViewDepartment'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/editDepartment', methods=['GET'])
def adminEditDepartment():
    try:
        if adminLoginSession() == 'admin':
            departmentVO = DepartmentVO()

            departmentDAO = DepartmentDAO()

            departmentId = request.args.get('departmentId')

            departmentVO.departmentId = departmentId

            departmentVOList = departmentDAO.editDepartment(departmentVO)

            print("=======DepartmentVOList=======", departmentVOList)

            print("=======type of DepartmentVOList=======", type(departmentVOList))

            return render_template('admin/editDepartment.html', departmentVOList=departmentVOList)
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)


@app.route('/admin/updateDepartment', methods=['POST'])
def adminUpdateDepartment():
    try:
        if adminLoginSession() == 'admin':
            departmentId = request.form['departmentId']
            departmentName = request.form['departmentName']
            departmentDescription = request.form['departmentDescription']

            departmentVO = DepartmentVO()
            departmentDAO = DepartmentDAO()

            departmentVO.departmentId = departmentId
            departmentVO.departmentName = departmentName
            departmentVO.departmentDescription = departmentDescription

            departmentDAO.updateDepartment(departmentVO)

            return redirect(url_for('adminViewDepartment'))
        else:
            return redirect(url_for('adminLogoutSession'))

    except Exception as ex:
        print(ex)
