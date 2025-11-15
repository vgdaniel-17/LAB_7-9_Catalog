from ui.ui_main import Console
from service.srv_note import Service_Note
from service.srv_student import *
from service.srv_discipline import *

ui = Console(srv_studenti, srv_discipline, srv_note)
ui.run()