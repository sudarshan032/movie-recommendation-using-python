
# Movie Recommendation System

  

This project implements a movie recommendation system using content-based filtering. The system suggests movies based on their similarity to a given movie, considering factors such as genre, director, and cast.

  

## Table of Contents

  

- [Introduction](#introduction)

- [Dataset](#dataset)

- [Implementation](#implementation)

- [Usage](#usage)

- [Dependencies](#dependencies)

- [Contributors](#contributors)

  

## Introduction

  

The movie recommendation system is designed to provide personalized movie suggestions to users. It utilizes a content-based approach, analyzing features such as movie genres, directors, and casts to recommend movies with similar characteristics.

  

## Dataset

  

 1. Heres the link to download the dataset   
    https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows/download?datasetVersionNumber=1
 2.  Heres the link for website of dataset https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows

The recommendation system uses the IMDb Top 1000 dataset (`imdb_top_1000.csv`). This dataset contains information about various movies, including their titles, release years, genres, directors, stars, ratings, and more.

  

## Implementation

  

The core of the recommendation system is implemented in Python using the scikit-learn library. The system calculates cosine similarity between movies based on their textual information (title, overview, director, genre), providing relevant recommendations.

  

## Usage

  

To use the recommendation system:

  

1. Clone the repository: `git clone https://github.com/your-username/movie-recommendation.git`

2. Navigate to the project directory: `cd movie-recommendation`

3. Run the recommendation script: `python recommend.py`

4. Enter the title of a movie when prompted.

5. Receive a list of recommended movies based on content similarity.

  

## Dependencies

  

The following Python libraries are required to run the recommendation system:

  

```bash

pip  install  pandas  scikit-learn statsmodels matplotlib seaborn

```

Ensure you have a Python environment set up with these dependencies installed.

  

## Contributors

-   G SUDARSHAN SASTRY

Ensure you have a Python environment set up with these dependencies installed.

## Contributors

-   G SUDARSHAN SASTRY

## Files

1.  eda.py
    
    -   Exploratory Data Analysis notebook containing analysis and visualizations of the IMDb Top 1000 dataset.
2.  recommendation.py
    
    -   Recommendation script implementing the content-based filtering algorithm for suggesting movies.

Feel free to contribute, report issues, or suggest improvements. We welcome your input to enhance the functionality of the recommendation system.  

***

> Happy movie watching!

***
