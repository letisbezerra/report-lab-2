from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table, TableStyle, colors

path = '/home/leticia/Documentos/Leticia/exemplotable/tabela.pdf'

data = [
    ['ID', 'Name', 'Class', 'Mark', 'Gender'],
    (1, 'John Deo', 'Four', 75, 'female'),
    (2, 'Max Ruin', 'Three', 85, 'male'),
    (3, 'Arnold', 'Three', 85, 'male'),
    (4, 'Arnold', 'Three', 55, 'male'),
    (5, 'Thalles', 'Five', 22, 'nao binare'),
]

my_doc = SimpleDocTemplate(path, pagesize = letter)

c_width = [0.4*inch, 1.5*inch, 1*inch, 1*inch, 1*inch] 
tabela = Table(data, rowHeights=15, repeatRows=1, colWidths= c_width)

tabela.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BACKGROUND', (0, 2), (-1, 3), colors.yellow),
]))

rowNumb = len(data)
for i in range(1, rowNumb):
    if i % 2 == 0:
        rowNumb.setTableStyle(TableStyle[
            ('span', (0, i + 1), (-1, i + 1)),
        ])


elements = []
elements.append(tabela)
my_doc.build(elements)