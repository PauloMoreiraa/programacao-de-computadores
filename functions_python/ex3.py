def Saudacao(Nome, Hora, Titulo=""):
    if Hora < 12:
        Aux = "Bom dia"
    elif Hora >= 12 and Hora < 19:
        Aux = "Boa tarde"
    else:
        Aux = "Boa noite"
    print(f"{Aux}, {Titulo} {Nome}!")

Saudacao("Pedro", 15)
Saudacao("Pedro", 15, "Dr.")
Saudacao("Pedro", 15, "São")

Saudacao(Hora=15, Nome="Pedro")
Saudacao(Titulo="Dr.", Nome="Pedro", Hora=15)
Saudacao(Titulo="São", Hora=15, Nome="Pedro")

