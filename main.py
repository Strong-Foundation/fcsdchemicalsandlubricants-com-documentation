import pypdf
import os


def split_pdf(input_pdf_path: str, output_dir: str) -> None:
    os.makedirs(name=output_dir, exist_ok=True)

    reader = pypdf.PdfReader(stream=input_pdf_path)
    total_pages: int = len(reader.pages)

    for i in range(total_pages):
        writer = pypdf.PdfWriter()
        writer.add_page(page=reader.pages[i])

        output_path: str = os.path.join(output_dir, f"page_{i+1}.pdf")
        with open(file=output_path, mode="wb") as output_file:
            writer.write(stream=output_file)

        print(f"Saved: {output_path}")


# Example usage
split_pdf(input_pdf_path="PDFs/MotorcraftSDS_US_En.pdf", output_dir="PDFs/")
