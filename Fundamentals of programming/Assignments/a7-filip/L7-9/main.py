from business.service import *
from domain.validators import *
from persistenta.repository import *
from prezentare.ui import *
from testare.teste import Teste

validatorStudent = ValidatorStudent()
validatorDisciplina = ValidatorDisciplina()
validatorNota = ValidatorNota()
repoStudenti = RepositoryStudenti()
repoDiscipline = RepositoryDiscipline()
repoNote = RepositoryNote()
serviceStudenti = ServiceStudenti(validatorStudent, repoStudenti)
serviceDiscipline = ServiceDiscipline(validatorDisciplina, repoDiscipline)
serviceNote = ServiceNote(validatorNota, repoNote, repoStudenti, repoDiscipline)
consola = UI(serviceStudenti, serviceDiscipline, serviceNote)

# TESTE
# teste = Teste(validatorStudent, validatorDisciplina, validatorNota, repoStudenti, repoDiscipline, repoNote, serviceStudenti, serviceDiscipline, serviceNote)
# teste.testCreazaStudent()
# teste.testValidatorStudent()
# teste.testEgalStudent()
# teste.testCreazaDisciplina()
# teste.testValidatorDisciplina()
# teste.testEgalDisciplina()
# teste.testCreeazaNota()
# teste.testEgalNota()
# teste.testValidatorNota()
# teste.testStoreStudent()
# teste.testStoreDisciplina()
# teste.testStoreNota()
# teste.testCautaStudent()
# teste.testCautaDisciplina()
# teste.testModificaStudent()
# teste.testModificaDisciplina()
# teste.testStergeStudent()
# teste.testStergeDisc()

consola.run()
