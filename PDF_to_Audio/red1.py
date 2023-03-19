import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename


def convertir_audio():
    # Abre el PDF con filedialog
    book = askopenfilename()

    with open(book, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Numero de paginas del pdf
        pages = len(pdf_reader.pages)

        # extrae el texto de cada pagina
        for num in range(0, pages):
            page = pdf_reader.pages[num]
            text = page.extract_text()

            # Usa pyttsx3 para leer el texto
            player = pyttsx3.init()
            player.say(text)
            player.runAndWait()
