from pypdf import PdfReader, PdfWriter
import os
import sys

# Detecta a pasta onde o .exe estiver
if getattr(sys, 'frozen', False):
    pasta = os.path.dirname(sys.executable)
else:
    pasta = os.path.dirname(os.path.abspath(__file__))

arquivo_saida = os.path.join(pasta, "PDF_FINAL_UNIDO.pdf")

writer = PdfWriter()

arquivos_pdf = sorted(
    [f for f in os.listdir(pasta) if f.lower().endswith(".pdf") and f != "PDF_FINAL_UNIDO.pdf"]
)

if not arquivos_pdf:
    print("❌ Nenhum PDF encontrado na pasta.")
    input("Pressione Enter para sair...")
else:
    for arquivo in arquivos_pdf:
        caminho = os.path.join(pasta, arquivo)
        print(f"Adicionando: {arquivo}")

        reader = PdfReader(caminho)
        for pagina in reader.pages:
            writer.add_page(pagina)

    with open(arquivo_saida, "wb") as f:
        writer.write(f)

    print("\n✅ PDFs unidos com sucesso!")
    print(f"📄 Arquivo final criado em: {arquivo_saida}")
    input("\nPressione Enter para sair...")