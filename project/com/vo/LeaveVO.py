from project import db


class LeaveVO(db.Model):
    __tablename__ = 'Leavemaster'
    leaveId = db.Column('leaveId', db.Integer, primary_key=True, autoincrement=True)
    leaveType = db.Column('leaveType', db.String(50))
    noOfDay = db.Column('noOfDay', db.Numeric(30))
    leaveDescription = db.Column('leaveDescription', db.String(600))

    def as_dict(self):
        return {
            'leaveId': self.leaveId,
            'leaveType': self.leaveType,
            'noOfDay': self.noOfDay,
            'leaveDescription': self.leaveDescription
        }


db.create_all()
