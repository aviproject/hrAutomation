from project import db

class DepartmentVO(db.Model):
    __tablename__='Departmentmaster'
    departmentId=db.Column('departmentId',db.Integer,primary_key=True, autoincrement=True)
    departmentName=db.Column('departmentname',db.String(100))
    departmentDescription = db.Column('departmentDescription',db.String(600))

    def as_dict(self):
        return{
            'departmentId':self.departmentId,
            'departmentName':self.departmentName,
            'departmentDescription':self.departmentDescription

        }

db.create_all()