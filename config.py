import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    FLATPAGES_ROOT = os.path.join(basedir, "app", "pages")
    FLATPAGES_AUTO_RELOAD = True
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_ENCODING = 'utf-8'
    FLATPAGES_MIMA = "cz650520"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    SERVER_NAME = "iiecon.cz"

config = {
    "develop": DevelopmentConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}
