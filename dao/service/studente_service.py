from DAO.dao.studente_dao import StudenteDAO
from DAO.dto.studente_dto import StudenteDTO

class StudenteService:
    @staticmethod
    def insert_studente(studente: StudenteDTO):
        #studente = StudenteDTO(matricola=matricola, nome_studente=nome_studente)
        return StudenteDAO.insert_studente(studente)

    @staticmethod
    def select_studente(matricola: int, nome_studente: str):
        studente = StudenteDTO(matricola, nome_studente)
        return StudenteDAO.select_studente(studente)

    @staticmethod
    def update_studente(matricola: int, nome_studente: str):
        studente = StudenteDTO(matricola=matricola, nome_studente=nome_studente)
        StudenteDAO.update_studente(studente)

    @staticmethod
    def delete_persona(matricola: int, nome_studente: str):
        studente = StudenteDTO(matricola=matricola, nome_studente=nome_studente)
        StudenteDAO.delete_studente(studente)

    @staticmethod
    def select_studente_all():
        return StudenteDAO.select_studente_all()