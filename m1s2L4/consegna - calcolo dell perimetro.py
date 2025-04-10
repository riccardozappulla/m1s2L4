import math

def calcola_circonferenza_diametro(diametro):
    circonferenza =math.pi * diametro
    return circonferenza
    
def calcola_circonferenza_raggio(raggio):
    circonferenza =2 * math.pi * raggio
    return circonferenza
print("calcolo del perimetro")
print("Cerchio \t",0)
print("triangolo \t",1)
print("Quadrato \t",2)
print("Rettangolo \t",3)
command = int(input('Inserisci il numero relativo alla tua scelta : ')) 



match command:
    case 0:
        print("hai selezionato il Cerchio")
        print("hai il diametro\t", 0)
        print("hai il raggio \t", 1)
        command = int(input('Inserisci il numero relativo alla tua scelta : '))
        match command:
                case 0:
                    print("hai selezionato il diametro,")
                    diam = float(input('Inserisci il valore : '))
                    circonferenza = calcola_circonferenza_diametro(diam)
                    print("la circonferenza,", circonferenza)
                    
                case 1:
                    print("hai selezionato il raggio,")
                    ragg = float(input('Inserisci il valore : '))
                    circonferenza = calcola_circonferenza_raggio(ragg)
                    print("la circonferenza è,", circonferenza)
                    
                case _:
                    print("Comando non riconosciuto")                   
                    
    case 1:
        print("hai selezionato il triangolo")
        print("inserisci i valori dei lati")
        l1 = float(input('Inserisci il valore : '))
        l2 = float(input('Inserisci il valore : '))
        l3 = float(input('Inserisci il valore : '))
        perimetrot = l1 + l2 + l3 
        print("li perimetro del triangolo è,", perimetrot)
        
    case 2:
        print("hai selezionato il Quadrato")
        print("inserisci il valore del lato")
        l = float(input('Inserisci il valore : '))
        perimetroQ = l*4
        print("li perimetro del Quadrato è,", perimetroQ)        
        
    case 3:
        print("hai selezionato il Rettangolo")
        print("inserisci i valori dei lati")
        lM = float(input('Inserisci il valore del latto maggiore : '))
        lm = float(input('Inserisci il valore del latto minore   : '))
        perimetroR = (lM*2)+(lm*2)
        print("li perimetro del Rettangolo è,", perimetroR)   
        
        
    case _:
        print("Comando non riconosciuto")
        
        