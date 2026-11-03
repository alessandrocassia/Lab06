import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def mostraStrumenti(self, e):
        self._view.lista_strumenti.controls.clear()

        lista_nuova = self._model.get_strumenti() #chiamo la funzione del model per prendere gli strumenti
        for strumento in lista_nuova:
            testo_strumento = ft.Text(str(strumento))
            self._view.lista_strumenti.controls.append(testo_strumento)

        self._view.update()

    def cercaPerTipo(self, e):
        self._view.lista_strumenti_ricerca.controls.clear()

        lista_nuova_ricerca = self._model.cerca_strumenti_per_tipo(self._view.input_tipo_strumento.value)
        for strumento in lista_nuova_ricerca:
            testo_strumento_ricerca = ft.Text(str(strumento))
            self._view.lista_strumenti_ricerca.controls.append(testo_strumento_ricerca)

        self._view.update()



