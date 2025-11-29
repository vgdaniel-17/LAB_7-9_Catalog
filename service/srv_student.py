import random

from Error.Repo_Error import RepoError
from domain.studenti import Student
from repository.repository_studenti import RepoStudent


class service_student:
    def __init__(self, repo_studenti, validator_studenti):
        self.__repo = repo_studenti
        self.__validator = validator_studenti

    # ADD --------------------------------------------------------------------------------------------------------------

    def adauga_student(self, id_student, nume):
        self.__validator.validare_student(id_student, nume)
        self.__repo.adauga_student(Student(id_student, nume))

    # DEL --------------------------------------------------------------------------------------------------------------

    def sterge_student(self, id_student):
        self.__validator.validare_id(id_student)
        self.__repo.sterge_student(id_student)

    # UPDATE -----------------------------------------------------------------------------------------------------------

    def modifica_student(self, id_student, nume_nou):
        #Modifica student
        self.__validator.validare_student(id_student, nume_nou)
        student_nou = self.__repo.cauta_student(id_student)
        student_nou.set_nume_student(nume_nou)
        self.__repo.modifica_student(student_nou)

    # FIND -------------------------------------------------------------------------------------------------------------
    def cauta_student(self, id_student):
        """
        Cauta un stundent
        :param id_student:
        :return: stundet activ cu 'id' dat
        """
        return self.__repo.cauta_student(id_student)

    # GEN --------------------------------------------------------------------------------------------------------------

    def generare(self, nr_studenti):
        """
        Genereaza un numar 'nr_studenti' de stundenti si ii adauga in repo
        :param nr_studenti: numar intreg, pozitiv
        :return:
        """

        prenume = ["Nechifor", "Haralambie", "Sergiuț", "Baptist", "Gherasim", "Titus_Liviu", "Ravel", "Codrinel", "Zotic", "Samson", "Sebald", "Geluț", "Ludovic", "Simeonel", "Timoftei", "Prisilia", "Paraschiva", "Domnica", "Catrina", "Smaranda", "Varvara", "Zenovia", "Agripina", "Gențiana", "Melania_Ruxandra", "Florimonda", "Pulheria", "Sevastiana", "Steluța", "Zinaida", "Alex", "Maria", "Andrei", "Ioana", "Mihai", "Elena", "Cristian", "Ana", "Gabriel", "Laura", "George", "Bianca", "Robert", "Diana", "Paul", "Alexandra", "Daniel", "Cristina", "Radu", "Raluca", "Vlad", "Anca", "Stefan", "Monica", "Florin", "Oana", "Dorin", "Simona", "Sergiu", "Alina", "Ciprian", "Carmen", "Lucian", "Adriana", "Ionut", "Denisa", "Tudor", "Camelia", "Cosmin", "Claudia", "Razvan", "Loredana", "Valentin", "Sorina", "Petru", "Georgiana", "Bogdan", "Nicoleta", "Eduard", "Andreea", "Catalin", "Roxana", "Sebastian", "Teodora", "Emanuel", "Madalina", "Horia", "Alice", "Darius", "Paula", "Marius", "Viviana", "Octavian", "Delia", "Iulian", "Silvia", "Calin", "Mirela", "Victor", "Izabela", "Ovidiu", "Patricia", "Dragos", "Veronica", "Rares", "Marina", "Emil", "Cristiana", "Denis", "Erika", "Filip", "Melisa", "Matei", "Carla", "Sorin", "Ingrid", "Nicholas", "Amalia", "David", "Irina", "Eric", "Larisa", "Kevin", "Sonia"]

        nume = ["Ciubotariu", "Hagiu", "Bârloagă", "Rânjea", "Moțoc", "Făgărășanu", "Papadopol", "Țicleanu", "Zăgan","Cireșar", "Mălăiescu", "Plopeanu", "Urziceanu", "Popescu", "Ionescu", "Stan", "Dumitru", "Marinescu", "Tudor", "Georgescu", "Barbu", "Pavel", "Savu", "Radu", "Dobre", "Matei", "Toma", "Enache", "Dragan", "Lazar", "Sima", "Moldovan", "Ilie", "Stoica", "Vasile", "Neagu", "Sorescu", "Popa", "Preda", "Luca", "Costache", "Albu", "Moraru", "Nistor", "Mihai", "Lupu", "Sandu", "Parvu", "Munteanu", "Petrescu", "Dinu", "Serban", "Manole", "Oprea", "Rosu", "Davidescu", "Voicu", "Savin", "Baciu", "Diaconu", "Rusu", "Balan", "Cristea", "Avram", "Marcu", "Bejan", "Zaharia", "Nita", "Dinescu", "Constantin", "Sorin", "Jianu", "Movila", "Neacsu", "Badea", "Racovitan", "Carp", "Turcu", "Cojocaru", "Iorga", "Nedelcu", "Suciu", "Olaru", "Tiron", "Chiriac", "Bologa", "Ignat", "Basarab", "Nicolau", "Mazilu", "Rizescu", "Curtis", "Coltea", "Savulet", "Sava", "Oancea", "Anghel", "Zamfir", "Manea", "Gheorghiu", "Barbat", "Roman", "Codreanu", "Neamtu", "Ungureanu", "Costin", "Badeanu", "Tiron", "Varzaru"]

        count_gen = 0
        while count_gen < nr_studenti:

            id_student = random.randint(100000, 999999)
            nume_nou = random.choice(nume) + " " + random.choice(prenume)
            student_gen = Student(id_student, nume_nou)
            try:
                self.__repo.adauga_student(student_gen)
                count_gen += 1
            except RepoError:
                continue


    # ALL-LIST-ACTIVE --------------------------------------------------------------------------------------------------

    def get_all_student_active(self):
        return self.__repo.get_all()

    # ALL-LIST ---------------------------------------------------------------------------------------------------------

    def get_all_student(self):
        return self.__repo.get_all_all()

    # DEL-LIST ---------------------------------------------------------------------------------------------------------

    def golire_lista_student(self):
        self.__repo.sterge_tot()

