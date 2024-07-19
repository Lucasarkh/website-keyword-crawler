# 🌐 Website Keyword Crawler 🔍

This Python script is designed to crawl through a specified website, search for keywords, and export the results to an Excel file. It's a handy tool for SEO experts, content creators, and web developers who need to analyze the presence of specific keywords on a website.

## 📋 Features

- Crawl through a specified website starting from a given URL
- Search for keywords in various HTML tags (`title`, `h1`, `h2`, `h3`, `p`, `span`, `li`) and you can add a tag
- Export results to an Excel file with detailed information about the found keywords
- Track and list all visited pages
- Exclude URL parameters not in link (such as "?", "upload", "#", "http://")

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Lucasarkh/website-keyword-crawler.git
    cd website-keyword-crawler
    ```

2. Install the required packages:
    ```bash
    pip install requests beautifulsoup4 pandas ansicolors
    ```

## 🛠 Usage

1. Open the `app.py` file and set the `site_url` and `wanted_key_words` variables:
    ```python
    site_url = "https://example.com" # INSERT URL HERE
    wanted_key_words = ["example_1", "example_2"] # ARRAY OF KEYWORDS
    ```

2. Run the script:
    ```bash
    python app.py
    ```

3. The script will crawl through the website, search for the specified keywords, and export the results to an `results.xlsx` file.

### Example Output

The Excel file will contain two sheets:
- **Pages with keywords**: List of URLs where the keywords were found, along with the tag and context.
- **All pages**: List of all visited pages during the crawl.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## 🌟 Support

If you like this project, please consider giving it a ⭐ on GitHub!

## 📧 Contact

Feel free to open an issue if you have any questions or suggestions. You can also contact me via [email](mailto:lucasarchanjo1010@gmail.com).

---

Made with ❤️ by [Lucas](https://github.com/Lucasarkh)
