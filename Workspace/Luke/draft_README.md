# Tweet Sentiment Analysis Using NLP

<!--- Wordcloud header image --->

# Authors

- Luke Dowker: 
[LinkedIn](https://www.linkedin.com/in/luke-dowker/) |
[GitHub](https://github.com/toastdeini) |
[Email](mailto:lhdowker@gmail.com)
- Will Norton: 
[LinkedIn](https://www.linkedin.com/in/william-norton-jr-43232745/) |
[GitHub](https://github.com/Noptov) |
[Email](mailto:noptov52@yahoo.com)
- Saad Saeed: 
[LinkedIn](https://www.linkedin.com/in/saadsaeed85/) |
[GitHub](https://github.com/ssaeed85) |
[Email](mailto:saadsaeed85@gmail.com)
- Marshall Wylder: 
[LinkedIn](https://www.linkedin.com/in/marshall-wylder-172582159/) |
[GitHub](https://github.com/MarshallWylder) |
[Email](mailto:marshall.wylder@gmail.com)

# Overview

- Can we use natural language processing (NLP) to 
- Tweets tagged by human users as containing positive, negative, or no emotional sentiment. Also recorded: if applicable, what product/company is being referenced in the tweet?
- Use NLP to predict if a tweet will contain positive or negative sentiment based on the tokens it contains
- Figure out which words are most likely to be associated with a certain sentiment (?) to improve SXSW ability to respond to user feedback (??)

## Business Problem



# Data

The data used in this project is [hosted on data.world](https://data.world/crowdflower/brands-and-product-emotions) and was sourced by the machine learning/AI company CrowdFlower, which has since been acquired by [Appen](https://appen.com/datasets-resource-center/). Per the dataset summary:

> "Contributors evaluated tweets about multiple brands and products. The crowd was asked if the tweet expressed positive, negative, or no emotion towards a brand and/or product. If some emotion was expressed they were also asked to say which brand or product was the target of that emotion."

The dataset consists of just under 9,100 rows and three columns:
- `tweet_text` - the full text of a tweet. The primary feature used in this analysis.
- `emotion_in_tweet_is_directed_at` - if applicable, what product or brand (e.g. Apple, iPhone app, Google, Android app, etc.) the emotion in the tweet is "targeted" at.
- `is_there_an_emotion_directed_at_a_brand_or_product` - The target variable for our analysis, the values in this column indicate whether a human contributor determined the content of the `tweet_text` to contain a positive sentiment, a negative sentiment, or no clear judgmental stance.

The majority of the tweets in the dataset were neutral in sentiment - that is, they did not express a positive or negative emotion *toward a brand or product* 

<!--- Graph of target distribution image ---> 

- Additional data/purpose
- Data itself - what it represents, its constituents, etc

# Methodology

- To prepare the data (text) for modeling, we used two vectorization techniques - a simple bag-of-words approach with sklearn's `CountVectorizer` and a term-importance approach using the same library's `TfidfVectorizer`.
- Which features and why?
- Overall journey

<!--- Bar graph of most common words after appending new stopwords --->

# Modeling

- Techniques
- Details 
- Scores/results

<!--- Normalized confusion matrix image --->

# Conclusions

- Recommendation 1
- Recommendation 2
- Recommendation 3

## Next Steps

- Refine **upsampling techiques** to better predictive on imbalanced classes, i.e. positive or negative emotion.
- Next Step 2
- Next Step 3

# Repository Structure
```
├── Workspace  
│     ├── Luke
│     │   ├── draft_README.md
│     │   └── Initial_Cleaning.ipynb
│     ├── Marshall
│     │   ├── Notes.md
│     │   └── *.ipynb
│     ├── Saad
│     │   ├── Notes.md
│     │   └── DataCleaning.ipynb
│     └── Will
│         ├── Notes.md
│         └── *.ipynb
│
├── data
│     ├── datapackage.json
│     └── judge_1377884607_tweet_product_company.csv
├── images
├── README.md
├── **Project_Presentation_Slides**.pdf
└── **Project_Final_Notebook**.ipynb
```
## Citations and Further Reading