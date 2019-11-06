Ano = int(input('Digite o ano que voce nasceu: '))
Mes = int(input('Digite o mes que voce nasceu: '))
Dia = int(input('Digite o dia que voce nasceu: '))

idadedias = ((365 * (2019 - Ano)) + (30 * Mes) + Dia)

print('Voce tem aproximadamente ' + str(idadedias) + ' dias de idade')