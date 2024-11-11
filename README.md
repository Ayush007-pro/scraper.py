# Scraper

This Python script allows you to scrape a webpage by entering its URL. It extracts various elements from the page, such as the title, paragraphs, links, images, and more. The script uses the `requests` library to fetch the webpage content and `BeautifulSoup` from the `bs4` library to parse the HTML.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Notes](#notes)
- [License](#license)

## Features

- **User Input for URL**: Prompt the user to enter the URL of the webpage to scrape.
- **Custom Headers**: Uses custom headers to mimic a real browser request.
- **Error Handling**: Includes try-except blocks to handle HTTP and network errors gracefully.
- **Page Title Extraction**: Retrieves and displays the title of the webpage.
- **First `<p>` and `<div>` Tag Extraction**: Finds and displays the first `<p>` and `<div>` tags, along with their attributes and text content.
- **Cleaned Text Extraction**: Cleans and displays the text from the first `<div>` tag.
- **All `<p>` and `<a>` Tags**: Finds and displays all `<p>` and `<a>` tags in the webpage.
- **Class-Specific Tag Extraction**: Finds `<p>` tags with the class `description` and elements with specific classes.
- **Option Tags with Specific Values**: Finds `<option>` tags with specified `value` attributes.
- **Unique Links Extraction**: Gathers and displays all unique hyperlinks on the page.
- **Image URLs Extraction**: Gathers and displays all image source URLs from the page.

## Prerequisites

- **Python 3.x**: Ensure that Python 3 is installed on your system.
- **Required Python Libraries**:
  - `requests`
  - `beautifulsoup4`

You can install the required libraries using `pip`:

```bash
pip install requests beautifulsoup4
```

## Installation

1. **Clone the Repository or Download the Script**:

   - Clone the repository:
     ```bash
     git clone https://github.com/yourusername/web-scraping-script.git
     cd web-scraping-script
     ```
   - Or simply download the `script.py` file to your local machine.

2. **Install the Required Libraries**:

   Ensure you have the necessary Python libraries installed:

   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

1. **Run the Script**:

   Navigate to the directory containing the script and run:

   ```bash
   python script.py
   ```

2. **Enter the URL**:

   When prompted, enter the URL of the webpage you want to scrape:

   ```bash
   Enter the url: https://www.example.com
   ```

3. **View the Output**:

   The script will display various elements extracted from the webpage in the console.

## Example Output

```
Enter the url: https://www.example.com
Page Title: Example Domain

First <p> Tag:
<p>This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.</p>

Prettified <p> Tag:
<p>
 This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.
</p>

Classes of <p> Tag: No class attribute.

Text within <p> Tag:
This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.

First <div> Tag:
<div>
<h1>Example Domain</h1>
<p>This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.</p>
<p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>

Prettified <div> Tag:
<div>
 <h1>
  Example Domain
 </h1>
 <p>
  This domain is for use in illustrative examples in documents. You may use this
  domain in literature without prior coordination or asking for permission.
 </p>
 <p>
  <a href="https://www.iana.org/domains/example">
   More information...
  </a>
 </p>
</div>

Classes of <div> Tag: No class attribute.

Text within <div> Tag:
Example Domain
This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.
More information...

Cleaned Text from <div> Tag:
Example Domain
This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.
More information...

Total <p> Tags Found: 2

<p> Tag 1:
<p>This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.</p>

<p> Tag 2:
<p><a href="https://www.iana.org/domains/example">More information...</a></p>

Total <a> Tags Found: 1

<a> Tag 1:
Href: https://www.iana.org/domains/example
Link Text: More information...

Total <p> Tags with class 'description': 0

Total Elements with specified classes: 0

<option> Tags with value='91': 0

<option> Tags with value='380': 0

Total Unique Links Found: 1
https://www.iana.org/domains/example

Total Images Found: 0
```

*Note: The output will vary depending on the webpage you choose to scrape.*

## Notes

- **Ethical Considerations**: Ensure you have permission to scrape the website. Always respect the website's `robots.txt` file and terms of service.
- **Dynamic Content**: This script may not work properly with websites that load content dynamically using JavaScript. For such sites, consider using tools like Selenium or Playwright.
- **Error Handling**: The script includes basic error handling for network requests. Additional error checks can be added as needed.
- **Extensibility**: Feel free to modify and extend the script to suit your specific scraping needs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Created by [Your Name](https://github.com/Ayush007-pro).*
