import os
import tempfile
from PyPDF2 import PdfMerger, PdfReader
import img2pdf
from PIL import Image
import pathlib

def merge_pdfs_and_images(output_filename, input_folder=f"{pathlib.Path(__file__).parent.resolve()}/input_files"):
    """
    Merge all PDF files and image files in the input folder into a single PDF file.
    Supported image formats: JPG, JPEG, PNG, BMP, TIFF, GIF
    
    Args:
        input_folder (str): The folder containing PDF and image files to merge.
        output_filename (str): The name of the output merged PDF file.
    """
    # Create a PdfMerger object
    merger = PdfMerger()
    
    # Create a temporary directory to store converted images
    temp_dir = tempfile.mkdtemp()
    temp_files = []
    
    # Get all files in the specified folder
    all_files = os.listdir(input_folder)
    
    # Sort files to ensure consistent order
    all_files.sort()
    
    # Supported image extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.gif']
    
    # Keep track of how many files we've processed
    files_added = 0
    
    # Process each file
    for file in all_files:
        file_path = os.path.join(input_folder, file)
        file_extension = os.path.splitext(file)[1].lower()
        
        # Check if it's a PDF file
        if file_extension == '.pdf':
            print(f"Adding PDF: {file}")
            merger.append(file_path)
            files_added += 1
        
        # Check if it's an image file
        elif file_extension in image_extensions:
            try:
                # Convert image to PDF
                temp_pdf = os.path.join(temp_dir, f"{os.path.splitext(file)[0]}.pdf")
                
                # Open and ensure the image is in RGB mode (required for some formats)
                with Image.open(file_path) as img:
                    if img.mode == 'RGBA':
                        img = img.convert('RGB')
                    
                    # For GIF, use only the first frame
                    if file_extension == '.gif':
                        img.seek(0)
                        img = img.convert('RGB')
                        img.save(temp_pdf, format='PDF')
                    else:
                        # Use img2pdf for non-gif images for better quality
                        with open(temp_pdf, "wb") as f:
                            f.write(img2pdf.convert(file_path))
                
                print(f"Converting and adding image: {file}")
                merger.append(temp_pdf)
                temp_files.append(temp_pdf)
                files_added += 1
            
            except Exception as e:
                print(f"Error processing image {file}: {str(e)}")
    
    # Check if any files were added
    if files_added == 0:
        print(f"No valid PDF or image files found in {input_folder}")
        return
    
    # Write the merged PDF to the output file
    print(f"Saving merged document to {output_filename}")
    outputh_file_path = f"{pathlib.Path(__file__).parent.resolve()}/output_files/{output_filename}"
    merger.write(outputh_file_path)
    merger.close()
    
    # Clean up temporary files
    for temp_file in temp_files:
        try:
            os.remove(temp_file)
        except:
            pass
    try:
        os.rmdir(temp_dir)
    except:
        pass
    
    print(f"Successfully merged {files_added} files into {output_filename}")
    print(f"Total pages in merged document: {get_pdf_page_count(outputh_file_path)}")

def get_pdf_page_count(pdf_path):
    """Get the number of pages in a PDF file."""
    with open(pdf_path, 'rb') as f:
        pdf = PdfReader(f)
        return len(pdf.pages)

if __name__ == "__main__":
    # Example usage
    # input_folder = "input_files"  # Folder containing your PDF files
    output_filename = "Pawas-adhar.pdf"  # Name of the output file
    
    merge_pdfs_and_images(output_filename)