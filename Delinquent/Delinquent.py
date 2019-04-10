
class ConfigHandler:
    def __init__(self):
        self.filename = None
        self.data = dict()

    def __str__(self):
        return str(self.data)

    def loadFile(self, filename):
        self.filename = filename
        for line in open(self.filename):
            sep = line.split(' ')
            if sep[0][-1]!=':':
                print("[E] Fehler beim Laden der Zeile:", line)
                return
            firstWord = sep[0][:-1]
            rest = ' '.join(sep[1:])
            if rest[-1]=='\n':
                self.data[firstWord.lower()] = rest[:-1]
            else:
                self.data[firstWord.lower()] = rest

    def get(self, what):
        try:
            return self.data[what.lower()]
        except:
            return "Keine Informationen gefunden"

    def getFile(self):
        return self.filename


handler = ConfigHandler()
handler.loadFile("data.txt")

while True:
    inp = input("Informationen über Spieler: ")
    print(handler.get(inp).lower())