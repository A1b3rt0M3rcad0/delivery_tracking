from config.config import Config
from models.models import Base
from sqlalchemy import create_engine
from dataclasses import dataclass


@dataclass
class Engine:

    engine = create_engine(Config.engine)


class Db:
    
    def __init__(self) -> None:
        Base.metadata.create_all(Engine.engine)