class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:basset@localhost:5432/Immodb_2.0'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'super-secret key'