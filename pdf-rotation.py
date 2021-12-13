from PyPDF2 import PdfFileReader, PdfFileWriter
from tqdm import tqdm
import os

def rotate_pages(pdf_path):
    #create a pdf reader and writer objects
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    
    #getting pdf page count
    pdf_size = pdf_reader.getNumPages()
    print(f'pdf size:{pdf_size}')
    
    #creating new directory and new pdf file
    if "Transformed PDF" not in os.listdir():
        os.mkdir('Transformed PDF')
    trf_path = os.path.join('Transformed PDF', 'Transformed.pdf')
    
    #input from users for page number and rotation
    get_page = int(input("Enter the page number: "))
    #checker for page number
    if get_page> pdf_size-1:
        raise "Page number doesn't exist!"
    rotate_degree = int(input("Enter the degree of rotation in [90,180,270]: "))
    
    #rotating the pages
    for page in tqdm(range(pdf_size)):
        if page == get_page:
            page_obj = pdf_reader.getPage(page)
            page_obj.rotateClockwise(rotate_degree)
            pdf_writer.addPage(page_obj)
            with open(trf_path, 'wb') as file:
                pdf_writer.write(file)
        else:
            pdf_writer.addPage(pdf_reader.getPage(page))
            with open(trf_path, 'wb') as file:
                pdf_writer.write(file)

if __name__ == '__main__':
    path = 'linux.pdf'
    rotate_pages(path)