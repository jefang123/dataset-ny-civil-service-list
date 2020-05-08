from flask_sqlachemy import SQLALCHEMY

db = SQLALCHEMY()

class Auth(db.Model):
    """Model for user accounts."""

    __tablename__ = 'users'
    id = db.Column(
      db.Integer,
      primary_key=True
    )
    username = db.Column(
      db.String(64),
      index=False,
      unique=True,
      nullable=False
    )
    hash = db.Column(
      db.String(80),
      nullable=False
    )
    email = db.Column(
      db.String(80),
      index=True,
      unique=True,
      nullable=False
    )

    last_login = db.Column(
      db.DateTime,
      index=False,
      unique=False,
      nullable=False
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Session(db.Model):
  __tablename__ = 'sessions'
  uid = db.Column(
    db.Integer,
    foreign_key=True
  )
  session_token=(
    db.String(255),
    nullable=True
  )
  browser=(
    db.String(255),
    nullable=True
  )

class JWT(db.Model):
  __tablename__ = "usertokens"
  uid = db.Column(
    db.Integer,
    foreign_key=True
  )
  uToken=(
    db.String(255),
    nullable=False
  )
  expires=(
    db.DateTime,
    nullable=False
  )
  browser=(
    db.String(255),
    nullable=True
  )