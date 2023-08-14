from project import db


class DesignationVO(db.Model):
    __tablename__ = 'designationmaster'  # create the table in database pythondb
    designationId = db.Column('designationId', db.Integer, primary_key=True, autoincrement=True)
    designationName = db.Column('designationName', db.String(100))
    designationDescription = db.Column('designationDescription', db.String(600))

    def as_dict(self):
        return {
            'designationId': self.designationId,
            'designationName': self.designationName,
            'designationDescription': self.designationDescription
        }


db.create_all()
