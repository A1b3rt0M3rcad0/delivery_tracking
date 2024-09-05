from sqlalchemy.exc import IntegrityError, ProgrammingError, ArgumentError
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.orm import sessionmaker
from db.engine import Engine
from sqlalchemy import select as sqlalchemy_select
from sqlalchemy import and_
from typing import Dict, List, Any



class BaseController:

    def __init__(self, model, input_contract=None) -> bool:
        self.engine = Engine.engine
        self.model = model
        self.session = sessionmaker(bind = self.engine)
        self.input_contract = input_contract

    def create(self, **kwargs) -> None:
        with self.session() as session:
            try:
                instance = self.model(**kwargs)
                session.add(instance)
                session.commit()
                print(f"{self.model.__name__} - {kwargs} registry created")
                return True
            except IntegrityError:
                print(f"{self.model.__name__} - {kwargs} registry already exists")
                return False
            except ProgrammingError:
                print(f"{self.model.__name__} - {kwargs} incompatible argument")
                return False
    
    ## OLD SELECT
    #
    # def select(self, **kwargs) -> List[object]:
    #     with self.session() as session:
    #         try:
    #             if not all(isinstance(v, list) for v in kwargs.values()):
    #                 raise ArgumentError("All arguments must be lists")
    #            
    #             stmt = sqlalchemy_select(self.model).where(getattr(self.model, list(kwargs.keys())[0]).in_(list(kwargs.values())[0]))
    #             result = [item for item in session.scalars(stmt)]
    #             if len(result) > 0:
    #                 print(f"{self.model.__name__} - {kwargs} registry found")
    #                 return result
    #             else:
    #                 print(f"{self.model.__name__} - {kwargs} registry not found")
    #                 return []
    #         except ArgumentError as e:
    #             print(f"{self.model.__name__} - {kwargs} passed argument is not a list: {e}")
    #             return []
    #         except ProgrammingError:
    #             print(f"{self.model.__name__} - {kwargs} incompatible argument")
    #             return []
    
    def select(self, **kwargs) -> List[object]:
        with self.session() as session:
            try:
                # Verifica se todos os argumentos são listas
                if not all(isinstance(v, list) for v in kwargs.values()):
                    raise ValueError("All arguments must be lists")
                
                # Construção dinâmica das condições WHERE usando AND
                conditions = [
                    getattr(self.model, key).in_(value)
                    for key, value in kwargs.items()
                ]

                # Cria a consulta SELECT com as condições WHERE
                stmt = sqlalchemy_select(self.model).where(and_(*conditions))
                result = session.scalars(stmt).all()

                # Verifica se algum registro foi encontrado
                if result:
                    print(f"{self.model.__name__} - {len(result)} registry(ies) found for {kwargs}")
                    return result
                else:
                    print(f"{self.model.__name__} - {kwargs} registry not found")
                    return []

            except ValueError as e:
                print(f"{self.model.__name__} - Invalid argument: {e}")
                return []
            except ProgrammingError:
                print(f"{self.model.__name__} - Incompatible argument")
                return []
            except Exception as e:
                print(f"{self.model.__name__} - Unexpected error: {e}")
                return []
            
    def delete(self, **kwargs) -> bool:
        with self.session() as session:
            try:
                records = self.select(**kwargs)
                
                if records:
                    for record in records:
                        session.delete(record)
                    session.commit()
                    print(f"{self.model.__name__} - {kwargs} registry(ies) deleted")
                    return True
                else:
                    print(f"{self.model.__name__} - No registry found for {kwargs} to delete")
                    return False
                    
            except UnmappedInstanceError:
                print(f"{self.model.__name__} - Argument passed is not a model")
                return False
            except Exception as e:
                print(f"{self.model.__name__} - Error during deletion: {e}")
                return False
    
    def update(self, column_updates:Dict[str, Any], **kwargs) -> bool:
        with self.session() as session:
            try:
                registers = session.query(self.model).filter_by(**kwargs).all()
                for register in registers:
                    for key, value in column_updates.items():
                        setattr(register, key, value)
                session.commit()
                print(f"{self.model.__name__} - {registers} registry(s) updated")
                return True
            except ProgrammingError:
                print(f"{self.model.__name__} - {kwargs} incompatible argument")
                return False

    def select_all(self) -> List[object]:
        with self.session() as session:
            try:
                stmt = sqlalchemy_select(self.model)
                result = [item for item in session.scalars(stmt)]
                print(f"{self.model.__name__} - all registries found")
                return result
            except ProgrammingError:
                print(f"{self.model.__name__} - incompatible argument")
                return []