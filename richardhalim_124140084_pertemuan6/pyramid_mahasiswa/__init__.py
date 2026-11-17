from pyramid.config import Configurator
from sqlalchemy.orm import sessionmaker

from .models.meta import buat_engine


def main(global_config, **settings):
    with Configurator(settings=settings) as config:
        sessions = sessionmaker(bind=buat_engine())
        config.registry.sessions = sessions
        config.include(".routes")
        return config.make_wsgi_app()
