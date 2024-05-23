def Abastecer():
    global tanque
    tanque = "Cheio"
    print("- Frentista: abastecimento realizado. Seu tanque ficou", tanque)

tanque = "Vazio"
print("Você: Chegando no posto meu tanque estava", tanque)
Abastecer()
print("Você: Saindo do posto meu tanque estava", tanque)