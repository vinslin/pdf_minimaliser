import fitz  # PyMuPDF
from PIL import Image
import header_footer as ft
import image_table as mt


def pdf_to_images(pdf_path, start_page, end_page, dpi=300, box_info=False):
    # Open the provided PDF file
    pdf_document = fitz.open(pdf_path)

    # Ensure the start_page and end_page are within the valid range
    num_pages = len(pdf_document)
    if start_page < 1 or start_page > num_pages:
        raise ValueError(f"start_page must be between 1 and {num_pages}")
    if end_page < start_page or end_page > num_pages:
        raise ValueError(f"end_page must be between {start_page} and {num_pages}")

    # Convert to zero-based indexing for internal processing
    start_page -= 1
    end_page -= 1

    # List to store the image objects for the whole PDF
    image_list = []

    # Iterate through each page of the PDF
    for page_number in range(num_pages):
        # Get the page
        page = pdf_document.load_page(page_number)

        # Render the page to an image (PIL.Image) with higher resolution
        zoom_x = dpi / 72.0
        zoom_y = dpi / 72.0
        mat = fitz.Matrix(zoom_x, zoom_y)
        pix = page.get_pixmap(matrix=mat)

        # Convert the pixmap to an image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Append the image object to the list
        image_list.append(img)

    # Close the PDF document
    pdf_document.close()

    # Extract the specified range of images
    selected_images = image_list[start_page:end_page + 1]

    # Apply the blur functions to the selected images
    processed_images = []
    for img in selected_images:
        img_blurred = ft.blur_image_with_yolo(img)
        img_blurred = mt.blur_objects_in_image(img_blurred, box_info)
        processed_images.append(img_blurred)

    return processed_images