
# YouTube Data Scraper

Welcome to the YouTube Data Scraper – a portfolio project showcasing my exploration into the realm of data analysis using Python. This project is a testament to my interest and proficiency in leveraging data for meaningful insights. As a self-driven individual, I've designed this application to demonstrate my skills in data scraping and analysis, specifically focusing on YouTube data.


## Features

- **YouTube API Integration**: Utilizes the YouTube API to scrape data, including comments, video details, and channel details.
- **User-Friendly Interface**: Implemented with Flask, the project offers a simple web interface where users can select the type of data they want to analyze.
- **Data Options**: Users can choose to retrieve comments, video statistics, or channel statistics based on their preference.
- **Dynamic Input**: The application prompts users to input a YouTube link corresponding to their selected data type.
- **Export to CSV**: A convenient option allows users to save the scraped data as CSV files for further analysis.


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (version >= 3.6)
- Flask
- YouTube API Key (Get one [here](https://console.developers.google.com/))

## Installation

1. **Clone the repository:**

    ```bash
    $ git clone https://github.com/onkar3210/Youtube_Scraper.git
    ```

2. **Install dependencies:**

    ```bash
    $ pip install -r requirements.txt
    ```

3. **Set up your YouTube API key:**

    - Obtain a YouTube API key by following the instructions [here](https://developers.google.com/youtube/registering_an_application).
    - Add your API key to the `config.py` file.

4. **Run the Flask application:**

    ```bash
    $ python app.py
    ```

The application will be accessible at `http://localhost:5000`.

## Usage

 **Run the Flask Application:**

   Navigate to the project directory and run the Flask application:

   ```bash
   $ python app.py
```

The application will be accessible at http://localhost:5000.

1. **Access the Web Interface**:

Open your web browser and go to http://localhost:5000. You will see the home page with options to scrape YouTube data.

2. **Choose Operation**:

- Scrape YouTube Video Comments:

  1. Click on the "Video Comments" link.
  2. Enter the YouTube video URL.
  3. Optionally, select the option to save results as a CSV file.
  4. Click the "Submit" button.  
    
- Retrieve YouTube Video Details:

    1. Click on the "Video Details" link.
    2. Enter the YouTube video URL.
    3. Optionally, select the option to save results as a CSV file.
    4. Click the "Submit" button.

- Fetch YouTube Channel Details:

    1. Click on the "Channel Details" link.
    2. Enter the YouTube channel ID.
    3. Optionally, select the option to save results as a CSV file.
    4. If you don't have the channel ID:
        Search for the YouTube channel on Google.
        Look for a website that provides the channel ID when given the channel link.
    5. Enter the obtained channel ID in the input field.
    6. Click the "Submit" button.
   
3. **Save Results as CSV (Optional)**:
After submitting the form for any operation, you will be prompted to save the results as a CSV file. Choose the desired location on your PC to save the file.

**Note** Ensure you have a valid YouTube API key configured in the config.py file before running the application.



## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Acknowledgements

 - Thanks to the YouTube API for providing a powerful interface for accessing YouTube data.
 - Special thanks to the Flask community for making web development in Python enjoyable.


## Contact

If you want to contact me you can reach me at onkarsbhave@gmail.com 
## License

This project is licensed under the [MIT License](LICENSE).

