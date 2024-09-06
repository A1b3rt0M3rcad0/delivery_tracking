from dataclasses import dataclass

@dataclass
class Config():

    engine = 'sqlite:///db/entregas.db'