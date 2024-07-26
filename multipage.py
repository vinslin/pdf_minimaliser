import streamlit as st
from PIL import Image
import os

# Function to load an image
def load_image(image_path):
  return Image.open(image_path)

# Define functions for each page
def bracket_page():
  st.title("Bracket Page")
 
  st.write("This is the Bracket Page.")
  pdf_path  = st.file_uploader("Upload a PDF file", type="pdf")

  output_folder = "uploaded_pdf"
  if not os.path.exists(output_folder):
     os.makedirs(output_folder)

  if st.button("Back to Home"):
    st.session_state["page"] = "home"  # Use session_state for navigation

def minimalizer_page():
  st.title("Minimalizer Page")
  st.write("This is the Minimalizer Page.")
  if st.button("Back to Home"):
    st.session_state["page"] = "home"

def summarizer_page():
  st.title("Summarizer Page")
  st.write("This is the Summarizer Page.")
  if st.button("Back to Home"):
    st.session_state["page"] = "home"

def backet_language_page():
  st.title("Backet Language Page")
  st.write("This is the Backet Language Page.")
  if st.button("Back to Home"):
    st.session_state["page"] = "home"

def text_format_page():
  st.title("Text Format Page")
  st.write("This is the Text Format Page.")
  if st.button("Back to Home"):
    st.session_state["page"] = "home"

def language_translator_page():
  st.title("Language Translator Page")
  st.write("This is the Language Translator Page.")
  if st.button("Back to Home"):
    st.session_state["page"] = "home"

# Dictionary to map page names to functions
pages = {
  "bracket": bracket_page,
  "minimalizer": minimalizer_page,
  "summarizer": summarizer_page,
  "backet_language": backet_language_page,
  "text_format": text_format_page,
  "language_translator": language_translator_page
}

# Main content based on session state (avoid query_params for navigation)
if "page" not in st.session_state:
  st.session_state["page"] = "home"  # Default page on first run

page = st.session_state["page"]

if page == "home":
  st.title("Homepage")
  st.write("Welcome to the Multi-page Streamlit App!")

  # Load images for buttons and logo (assuming you have images in the same directory)
  images = {
    "Bracket": load_image("logo.png"),
    "Minimalizer": load_image("logo.png"),
    "Summarizer": load_image("logo.png"),
    "Backet Language": load_image("logo.png"),
    "Text Format": load_image("logo.png"),
    "Language Translator": load_image("logo.png")
  }
  logo_image = load_image("logo.png")

  # Display logo
  st.image(logo_image, width=200)

  # Display images, titles, and navigation buttons
  for page_name in pages.keys():
    st.image(images[page_name.replace('_', ' ').title()], width=100)
    st.write(page_name.replace('_', ' ').title())
    if st.button(f"Go to {page_name.replace('_', ' ').title()}"):
      st.session_state["page"] = page_name  # Update session state for navigation

else:
  if page in pages:
    pages[page]()
  else:
    st.error("Page not found.")
