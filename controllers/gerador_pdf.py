from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
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


# Gerar PDF
pdf.build(elementos)