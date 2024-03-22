class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:basset@localhost:5432/Immodb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'super-secret key'