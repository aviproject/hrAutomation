from project import db


class LetterTypeVO(db.Model):
    __tablename__ = 'lettertypemaster'
    letterTypeId = db.Column('letterTypeId', db.Integer, primary_key=True, autoincrement=True)
    letterTypeName = db.Column('letterTypeName', db.String(100))
    letterTypeDescription = db.Column('letterTypeDescription', db.String(600))
    letterTypeFileName = db.Column('letterTypeFileName', db.String(200))
    letterTypeFilePath = db.Column('letterTypeFilePath', db.String(200))
    letterTypeFileUploadDate = db.Column('letterTypeFileUploadDate', db.String(30))
    letterTypeFileUploadTime = db.Column('letterTypeFileUploadTime', db.String(30))
    letterTypeFileObjectURL = db.Column('letterTypeFileObjectURL', db.String(500))

    def as_dict(self):
        return {
            'letterTypeId': self.letterTypeId,
            'letterTypeName': self.letterTypeName,
            'letterTypeDescription': self.letterTypeDescription,
            'letterTypeFileName': self.letterTypeFileName,
            'letterTypeFilePath': self.letterTypeFilePath,
            'letterTypeFileUploadDate': self.letterTypeFileUploadDate,
            'letterTypeFileUploadTime': self.letterTypeFileUploadTime,
            'letterTypeFileObjectURL': self.letterTypeFileObjectURL
        }


db.create_all()
