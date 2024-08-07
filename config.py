import os


class Config():
    SECRET_KEY = os.environ.get("TICKETTREK_SECRET_KEY")

    @staticmethod
    def init_app(app):
        pass

