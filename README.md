# PDF Generator from CSV

## Overview

This repository contains a Python script that reads data from a CSV file and generates a PDF file based on the information provided. The generated PDF can be used for a variety of purposes, such as creating reports, documents, or any other structured content.

## How It Works

The PDF generator script utilizes the `fpdf` library to create PDF files. Here's how the script works:

1. The script reads data from a CSV file (in this case, "topics.csv") using the Pandas library.

2. It sets up the PDF document with specified page orientation, size, and other formatting options.

3. For each row in the CSV file, it creates a new page in the PDF and adds content such as a title, lines, and footer.

4. If the CSV data indicates that multiple pages are required for a single topic, it generates additional blank pages with the same title and lines.

5. The resulting PDF file is saved as "output_lined.pdf."

## Prerequisites

Before using the script, make sure you have the following library installed:

- [fpdf](https://pypi.org/project/fpdf/)
- [pandas](https://pypi.org/project/pandas/)

## Usage

1. Clone this repository to your local machine or download the script.

2. Make sure you have a CSV file (e.g., "topics.csv") with the data you want to include in the PDF. Ensure that the CSV file has the necessary columns (e.g., "Topic" and "Pages") as expected by the script.

3. Run the script using Python (e.g., `python pdf_generator.py`).

4. The script will read the data from the CSV file and generate the PDF file with the specified content and formatting.

5. The generated PDF file will be saved as "output_lined.pdf" in the same directory as the script.

## Customization

- You can modify the script to adapt it to different CSV structures or to change the formatting of the generated PDFs.

- Adjust the `pdf` object's settings to control the page orientation, size, and other formatting options according to your requirements.

That's it! You can use this script to create PDF files from CSV data, making it a versatile tool for generating structured documents.

### License
This project is licensed under the MIT License. You are free to use and modify the code for your own purposes.
