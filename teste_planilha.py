import xlsxwriter, time

def gerar_planilha(dados, nome): 
    workbook = xlsxwriter.Workbook(nome)
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0

    for campo, dado in (dados):
        worksheet.write(row, col, campo)
        worksheet.write(row, col + 1, dado)
        row += 1
    
    workbook.close()

if __name__ == "__main__":
    p1 = (
        ['Data', time.strftime("%x")],
        ['Especialização', input("Selecione o especialista na qual desejaria ser atendido(a) por:\n")],
        ['DataSolicitacao', input("Informe a data disponível para consulta:\n")],
        ['CPF', input("Digite o seu CPF:\n")],
    )
    nome = 'planilha.xlsx'
    gerar_planilha(p1, nome)
    #enviar_arq_googledrive(nome)