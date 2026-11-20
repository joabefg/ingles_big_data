from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
# criar documento
pdf = SimpleDocTemplate("relatorio.pdf")
# Carregar estilos
estilos = getSampleStyleSheet()
# Criar título
titulo = Paragraph("Sales Performance Report",estilos["Title"])
# Organizar elementos
elementos = [titulo]
# Subtitulo
elementos.append( Paragraph("Sales Summary",estilos["Heading2"]))
# Texto
elementos.append(Paragraph("Segundo os dados...",estilos["Normal"]))
elementos.append(Spacer(1, 20))
elementos.append(Paragraph("Ao analisar...",estilos["Normal"]))

# Table
dados = [
    ["Produto", "Quantidade", "Valor"],
    ["Notebook", 10, "R$ 2.500,00"],
    ["Mouse", 25, "R$ 50,00"],
    ["Teclado", 15, "R$ 75,00"],
]
tabela = Table(dados)
# from reportlab.platypus import Table, TableStyle
# from reportlab.lib import colors
tabela.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("GRID", (0,0), (-1,-1), 0.5, colors.gray),
    ("ALIGN", (0,0), (-1,0), "CENTER")
]))
elementos.append(tabela)


# Gerar PDF
pdf.build(elementos)