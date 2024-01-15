
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
![Screenshot 2024-01-15 230720](https://github.com/onkar3210/Youtube_Scraper/assets/95028927/48843e81-458c-40fd-8ea9-371cf0d0ec95)

  1. Click on the "Video Comments" link.
  2. Enter the YouTube video URL.
  3. Optionally, select the option to save results as a CSV file.
  4. Click the "Submit" button.  
    
- Retrieve YouTube Video Details:
![Screenshot 2024-01-15 230619](https://github.com/onkar3210/Youtube_Scraper/assets/95028927/ac2a31bf-b2f9-4341-93da-3f9adc6bea4d)

    1. Click on the "Video Details" link.
    2. Enter the YouTube video URL.
    3. Optionally, select the option to save results as a CSV file.
    4. Click the "Submit" button.

- Fetch YouTube Channel Details:
![Screenshot 2024-01-15 231943](https://github.com/onkar3210/Youtube_Scraper/assets/95028927/0ce6399f-496a-4796-8cb8-b96b0caa0c5a)

    1. Click on the "Channel Details" link.
    2. Enter the YouTube channel ID.
    3. Optionally, select the option to save results as a CSV file.
    4. If you don't have the channel ID:
        Search for the YouTube channel on Google.
        Look for a website that provides the channel ID when given the channel link.
    5. Enter the obtained channel ID in the input field.
    6. Click the "Submit" button.
   
3. **Save Results as CSV (Optional)**:
   
   ![image](https://github.com/onkar3210/Youtube_Scraper/assets/95028927/61bf4aa7-df84-4460-8cf6-dacc65d532a7)
After submitting the form for any operation, you will be prompted to save the results as a CSV file. Choose the desired location on your PC to save the file.
![Screenshot 2024-01-15 232613](https://github.com/onkar3210/Youtube_Scraper/assets/95028927/2de6f5ea-ef8f-4250-a200-454e175acab9)
![Screenshot 2024-01-15 232547](https://github.com/onkar3210/Youtube_Scraper/assets/95028927/f92410a0-a7bc-4116-9d9a-44e9308a595c)
![Screenshot 2024-01-15 232630](https://github.com/onkar3210/Youtube_Scraper/assets/95028927/1e423521-9894-411c-bc06-a8a213845c15)



**Note** Ensure you have a valid YouTube API key configured in the config.py file before running the application.


## Acknowledgements

 - Thanks to the YouTube API for providing a powerful interface for accessing YouTube data.
 - Special thanks to the Flask community for making web development in Python enjoyable.


## Contact

If you want to contact me you can reach me at onkarsbhave@gmail.com 
## License

This project is licensed under the [MIT License](LICENSE).

