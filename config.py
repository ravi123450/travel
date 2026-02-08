class Config:

    SECRET_KEY = "supersecret"

    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "jwtsecretkey"


    # 🔥 EMAIL CONFIG (GMAIL SMTP)

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME = "merakanapalliraviteja86@gmail.com"   # 🔴 CHANGE
    MAIL_PASSWORD = "evgn dckm jpaw lrub"      # 🔴 CHANGE

    MAIL_DEFAULT_SENDER = "merakanapalliraviteja86@gmail.com"
