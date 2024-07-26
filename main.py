import streamlit as st
from PyPDF2 import PdfReader
import os
import pdflist 
import header_footer as footer
import minimalizer as mini
import bracket_words as bw
import bracket_lang as bl
from supported_languages import SUPPORTED_LANGUAGES
import text_format as ts
import translator_page as tp
import enhance as eh
import split_page as sp

def main():

    # Define a dictionary mapping page names to their corresponding functions
    pages = {
        "Home": home_page,
        "Bracket": bracket_page,
        "Minimalizer": minimalizer_page,
        "Summarizer": summarizer_page,
        "Bracket Language": bracket_language_page,
        "Text Format": text_format_page,
        "Language Translator": language_translator_page
    }

    # Display buttons for each page
    page_selection = st.sidebar.radio("Select a page", list(pages.keys()))

    # Call the selected page function when its corresponding button is clicked
    pages[page_selection]()

def home_page():
    st.markdown(
        """
        <h1 style='text-align: center;'>WHITE ROCK PDF</h1>
        """,
        unsafe_allow_html=True
    )
    st.image("img/intro-1696789529.webp", use_column_width=True)
    st.markdown(
        """
        <h5 style='text-align: center;'>OUR SERVICES</h1>
        """,
        unsafe_allow_html=True
    )
    st.write("1.MAKE THE PDF EASY TO READ ")
    st.write("2.MAKE HARD OR NATIVE ENGLISH BOOKS INTO EASILY READABLE ONE")
    st.write("3.HANDLE PHOTOCOPIED/PHOTO PDF")
    st.write("4.LANGUAGE TRANSLATOR")
def bracket_page():
    st.markdown(
        """
        <h1 style='text-align: center;'> "Bracket the hard english words"</h1>
        """,
        unsafe_allow_html=True
    )
    st.write("Find the hard English words from the pdf book and make easy to read")
    
    # PDF upload button
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    num_pages=1
    start_page=1
    end_page=1
    if uploaded_file:
        # Create a PdfReader object
        reader = PdfReader(uploaded_file)

        # Get the number of pages
        num_pages = len(reader.pages)

        # Display the number of pages
        st.write(f"Number of pages in PDF: {num_pages}")

        start_page = st.number_input(f"Enter the starting page (1 to {num_pages}):", min_value=1, max_value=num_pages,
                                 value=1)
        end_page = st.number_input(f"Enter the ending page ({start_page} to {num_pages}):", min_value=start_page,
                               max_value=num_pages, value=num_pages)

        st.write(f"You selected to process pages from {start_page} to {end_page}.")
    
    if uploaded_file is not None:
        # Create the directory if it doesn't exist
        upload_dir = "uploaded_pdfs"
        os.makedirs(upload_dir, exist_ok=True)
        
        # Save the uploaded PDF file to the directory
        file_path = os.path.join(upload_dir, uploaded_file.name)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.image("img/page_24.png", use_column_width=True)
       # Checkbox for box information
        st.write("like the above image you want the words from the BOX informations click the box checkbox ")
        box = st.checkbox("Box Information")
        

        st.write("If your pdf created by photocopied or image converted pdf select this checkbox for better results ")
        critical_pdf = st.checkbox("It's a photo based pdf")
        st.image("img/columns2-1 (2).png", use_column_width=True)
        double_content = st.checkbox("It's a double content page based pdf")
        st.write("if your pdf is Double columed please select the box")
        st.title(" put the bracket info in")

        printing_options = st.selectbox(
        "put the bracket info in:",
        ("Inttergrate_with_Paragraph", "Footter_of_the_page")
        )

        explanation = st.selectbox(
        "Which type of Explanations:",
        ("Normal_words", "synonymous")
        )


# Dropdown menu for selecting fluency level
        fluency_level = st.selectbox(
        "Choose your fluency level:",
        ("Beginner", "Intermediate")
        )

        # Show a start button if a file is uploaded
        if st.button("Start Processing"):
            # Perform your additional processing or actions here
            st.write("Processing started...")
            # Example: Call a function to process the uploaded file
            pdf_list = pdflist.pdf_to_images(file_path, start_page=start_page, end_page=end_page, dpi=300, box_info=box)
            if critical_pdf:
                pdf_list=eh.enhanced(pdf_list)
            if double_content:
                pdf_list=sp.split_images(pdf_list)

            st.write("done")
            temp=bw.extract_text_from_images(pdf_list,output_file="extracted_text.txt",fluency_level=fluency_level,printing_options=printing_options,explanation=explanation)
            
            st.write(temp)

            # Optionally, you can return or display additional results after processing

def minimalizer_page():
    st.markdown(
        """
        <h1 style='text-align: center;'>PDF BOOK MINIMALISER</h1>
        """,
        unsafe_allow_html=True
    )
    st.write("It Will make your pdf book into simple sentences and make it easier to read")
    
    # PDF upload button
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    num_pages=1
    start_page=1
    end_page=1
    if uploaded_file:
        # Create a PdfReader object
        reader = PdfReader(uploaded_file)

        # Get the number of pages
        num_pages = len(reader.pages)

        # Display the number of pages
        st.write(f"Number of pages in PDF: {num_pages}")

        start_page = st.number_input(f"Enter the starting page (1 to {num_pages}):", min_value=1, max_value=num_pages,
                                 value=1)
        end_page = st.number_input(f"Enter the ending page ({start_page} to {num_pages}):", min_value=start_page,
                               max_value=num_pages, value=num_pages)

        st.write(f"You selected to process pages from {start_page} to {end_page}.")
    
    if uploaded_file is not None:
        # Create the directory if it doesn't exist
        upload_dir = "uploaded_pdfs"
        os.makedirs(upload_dir, exist_ok=True)
        
        # Save the uploaded PDF file to the directory
        file_path = os.path.join(upload_dir, uploaded_file.name)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        #st.write(f"Uploaded file saved successfully to {file_path}")

        st.image("img/page_24.png", use_column_width=True)
        # Checkbox for box information
        st.write("like the above image you want the words from the BOX informations click the box checkbox ")
        box = st.checkbox("Box Information")

        st.write("If your pdf created by photocopied or image converted pdf select this checkbox for better results ")
        critical_pdf = st.checkbox("It's a photo based pdf")
        st.image("img/columns2-1 (2).png", use_column_width=True)
        double_content = st.checkbox("It's a double content page based pdf")
        st.write("if your pdf is Double columed please select the box")



# Dropdown menu for selecting fluency level
        fluency_level = st.selectbox(
        "Choose your fluency level:",
        ("Beginner", "Intermediate")
        )

       # Display the selected fluency level
        st.write(f"You selected: {fluency_level}")
        # Show a start button if a file is uploaded
        if st.button("Start Processing"):
            # Perform your additional processing or actions here
            st.write("Processing started...")
            # Example: Call a function to process the uploaded file
            pdf_list = pdflist.pdf_to_images(file_path, start_page=start_page, end_page=end_page, dpi=300, box_info=box)
            if critical_pdf:
                pdf_list=eh.enhanced(pdf_list)
            if double_content:
                pdf_list=sp.split_images(pdf_list)

            st.write("done")
            temp=mini.extract_text_from_images(pdf_list,output_file="extracted_text.txt",fluency_level=fluency_level)
            
            st.write(temp)

            # Optionally, you can return or display additional results after processing
          # Optionally, you can return or display additional results after processing


def summarizer_page():
    st.header("Summarizer Page")
    st.write("This is the content of the Summarizer page.")
    
    # PDF upload button
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Create the directory if it doesn't exist
        upload_dir = "uploaded_pdfs"
        os.makedirs(upload_dir, exist_ok=True)
        
        # Save the uploaded PDF file to the directory
        file_path = os.path.join(upload_dir, uploaded_file.name)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.write(f"Uploaded file saved successfully to {file_path}")
        
        # Show a start button if a file is uploaded
        if st.button("Start Summarization"):
            # Perform your additional processing or actions here
            st.write("Summarization started...")
            # Example: Call a function to summarize the uploaded file
            summarize_file(file_path)
            st.write("Summarization complete!")
            
            # Optionally, you can return or display 

def bracket_language_page():
    st.markdown(
        """
        <h1 style='text-align: center;'>HARD WORDS INTO YOUR OWN LANGUAGE</h1>
        """,
        unsafe_allow_html=True
    )
    st.write("Create the bracket info in your NATIVE language")

    # PDF upload button
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    num_pages=1
    start_page=1
    end_page=1
    if uploaded_file:
        # Create a PdfReader object
        reader = PdfReader(uploaded_file)

        # Get the number of pages
        num_pages = len(reader.pages)

        # Display the number of pages
        st.write(f"Number of pages in PDF: {num_pages}")

        start_page = st.number_input(f"Enter the starting page (1 to {num_pages}):", min_value=1, max_value=num_pages,
                                 value=1)
        end_page = st.number_input(f"Enter the ending page ({start_page} to {num_pages}):", min_value=start_page,
                               max_value=num_pages, value=num_pages)

        st.write(f"You selected to process pages from {start_page} to {end_page}.")

    if uploaded_file is not None:
        # Create the directory if it doesn't exist
        upload_dir = "uploaded_pdfs"
        os.makedirs(upload_dir, exist_ok=True)

        # Save the uploaded PDF file to the directory
        file_path = os.path.join(upload_dir, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        #st.write(f"Uploaded file saved successfully to {file_path}")
        st.image("img/page_24.png", use_column_width=True)
        # Checkbox for box information
        st.write("like the above image you want the words from the BOX informations click the box checkbox ")
        box = st.checkbox("Box Information")

        st.write("If your pdf created by photocopied or image converted pdf select this checkbox for better results ")
        critical_pdf = st.checkbox("It's a photo based pdf")
        st.image("img/columns2-1 (2).png", use_column_width=True)
        double_content = st.checkbox("It's a double content page based pdf")
        st.write("if your pdf is Double columed please select the box")


        st.title(" put the bracket words in")

        printing_options = st.selectbox(
            "put the bracket info in:",
            ("Inttergrate_with_Paragraph", "Footter_of_the_page")
        )

        explanation = st.selectbox(
            "Which type of Explanations:",
            ("Direct_Words", "Explanation_Words")
        )

        # Dropdown menu for selecting fluency level
        fluency_level = st.selectbox(
            "Choose your fluency level:",
            ("Beginner", "Intermediate")
        )

        # Display the selected fluency level
        st.write(f"You selected: {fluency_level}")

        # Select target language
        target_lang = st.selectbox('Select target language:', list(SUPPORTED_LANGUAGES.keys()),
                                   format_func=lambda x: SUPPORTED_LANGUAGES[x])

        # Show a start button if a file is uploaded
        if st.button("Start Processing"):
            # Perform your additional processing or actions here
            st.write("Processing started...")
            # Example: Call a function to process the uploaded file
            pdf_list = pdflist.pdf_to_images(file_path, start_page=start_page, end_page=end_page, dpi=300, box_info=box)
            if critical_pdf:
                pdf_list=eh.enhanced(pdf_list)
            if double_content:
                pdf_list=sp.split_images(pdf_list)

            st.write("done")
            temp = bl.bracket_language(pdf_list, output_file="extracted_text.txt", fluency_level=fluency_level,
                                               printing_options=printing_options, explanation=explanation,target_lang=target_lang)

            st.write(temp)

            # Optionally, you can return or display additional results after processing


def text_format_page():
    st.markdown(
        """
        <h1 style='text-align: center;'>GET TEXT FORMAT OF YOUR PDF</h1>
        """,
        unsafe_allow_html=True
    )
    st.write("Especially for photocopied pdf ")
    
    # PDF upload button
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    num_pages=1
    start_page=1
    end_page=1
    if uploaded_file:
        # Create a PdfReader object
        reader = PdfReader(uploaded_file)

        # Get the number of pages
        num_pages = len(reader.pages)

        # Display the number of pages
        st.write(f"Number of pages in PDF: {num_pages}")

        start_page = st.number_input(f"Enter the starting page (1 to {num_pages}):", min_value=1, max_value=num_pages,
                                 value=1)
        end_page = st.number_input(f"Enter the ending page ({start_page} to {num_pages}):", min_value=start_page,
                               max_value=num_pages, value=num_pages)

        st.write(f"You selected to process pages from {start_page} to {end_page}.")

    if uploaded_file is not None:
        # Create the directory if it doesn't exist
        upload_dir = "uploaded_pdfs"
        os.makedirs(upload_dir, exist_ok=True)
        
        # Save the uploaded PDF file to the directory
        file_path = os.path.join(upload_dir, uploaded_file.name)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.image("img/page_24.png", use_column_width=True)
        # Checkbox for box information
        st.write("like the above image you want the words from the BOX informations click the box checkbox ")
        box = st.checkbox("Box Information")

        st.write("If your pdf created by photocopied or image converted pdf select this checkbox for better results ")
        critical_pdf = st.checkbox("It's a photo based pdf")
        st.image("img/columns2-1 (2).png", use_column_width=True)
        double_content = st.checkbox("It's a double content page based pdf")
        st.write("if your pdf is Double column please select the box")


        # Show a start button if a file is uploaded
        if st.button("Start Processing"):
            # Perform your additional processing or actions here
            st.write("Processing started...")
            # Example: Call a function to process the uploaded file
            pdf_list = pdflist.pdf_to_images(file_path,start_page=start_page,end_page=end_page, dpi=300, box_info=box)
            if critical_pdf:
                pdf_list=eh.enhanced(pdf_list)
            if double_content:
                pdf_list=sp.split_images(pdf_list)

            st.write("done")
            temp = ts.bracket_language(pdf_list, output_file="extracted_text.txt")
            st.write(temp)


def language_translator_page():
    st.markdown(
        """
        <h1 style='text-align: center;'>TRANSLATE THE PDF INTO YOUR LANGUAGE</h1>
        """,
        unsafe_allow_html=True
    )
    st.write("we have power full way for process the pdf ,so you will translate almost every pdf ")
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    num_pages=1
    start_page=1
    end_page=1
    if uploaded_file:
        # Create a PdfReader object
        reader = PdfReader(uploaded_file)

        # Get the number of pages
        num_pages = len(reader.pages)

        # Display the number of pages
        st.write(f"Number of pages in PDF: {num_pages}")

        start_page = st.number_input(f"Enter the starting page (1 to {num_pages}):", min_value=1, max_value=num_pages,
                                 value=1)
        end_page = st.number_input(f"Enter the ending page ({start_page} to {num_pages}):", min_value=start_page,
                               max_value=num_pages, value=num_pages)

        st.write(f"You selected to process pages from {start_page} to {end_page}.")

    if uploaded_file is not None:
        # Create the directory if it doesn't exist
        upload_dir = "uploaded_pdfs"
        os.makedirs(upload_dir, exist_ok=True)

        # Save the uploaded PDF file to the directory
        file_path = os.path.join(upload_dir, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.image("img/page_24.png", use_column_width=True)
        # Checkbox for box information
        st.write("like the above image you want the words from the BOX informations click the box checkbox ")
        box = st.checkbox("Box Information")

        st.write("If your pdf created by photocopied or image converted pdf select this checkbox for better results ")
        critical_pdf = st.checkbox("It's a photo based pdf")
        st.image("img/columns2-1 (2).png", use_column_width=True)
        double_content = st.checkbox("It's a double content page based pdf")
        st.write("if your pdf is Double columed please select the box")

        st.title(" put the bracket words in")


        # Select target language
        target_lang = st.selectbox('Select target language:', list(SUPPORTED_LANGUAGES.keys()),
                                   format_func=lambda x: SUPPORTED_LANGUAGES[x])

        # Show a start button if a file is uploaded
        if st.button("Start Processing"):
            # Perform your additional processing or actions here
            st.write("Processing started...")
            # Example: Call a function to process the uploaded file
            pdf_list = pdflist.pdf_to_images(file_path, start_page=start_page, end_page=end_page, dpi=300, box_info=box)
            if critical_pdf:
                pdf_list=eh.enhanced(pdf_list)
            if double_content:
                pdf_list=sp.split_images(pdf_list)

            st.write("done")
            temp = tp.translate_page(pdf_list, output_file="extracted_text.txt",target_lang=target_lang)
            st.write(temp)

            # Optionally, you can return or display additional results after processing

if __name__ == "__main__":
    main()
