# agents.md

##### 1. What we're building
An automated sentiment-based news sorter that classifies news articles as "Good News 🎉", "Bad News 👎", or "Just News 🤷" using transformer-based NLP models, enabling mood-based browsing and engagement.

##### 2. How AI helps solve the business problem
- Automates the classification of news articles by sentiment, reducing manual editorial effort and increasing consistency.
- Enables dynamic creation of "Good News" and "Bad News" sections, improving user experience and engagement.
- Helps users quickly find content that matches their mood or interests, driving more traffic and longer sessions.
- Provides scalable, data-driven content curation as the volume of articles grows.


##### 3. Key file locations and data structure
- `./week_05/assignment/mbai448_week05_assignment.ipynb` — main notebook for prototyping and analysis
- `./week_05/assignment/data/news.csv` — source dataset of news articles


##### 4. High-level execution plan
1. Data loading and inspection
	- Load the news dataset and inspect its structure and sample rows.
2. Environment setup and model loading
	- Install and import required libraries; load all required transformer-based models.
3. Sample a single article for exploration
	- Extract and inspect a single article's headline and text for model testing.
4. Load pretrained transformer models
	- Set up pipelines for sentiment analysis, named entity recognition, question answering, and summarization.
5. Test the models on your sample article
	- Run each model (sentiment, NER, QA, summarization) on the sample and review the outputs.
6. Prepare data for scaled processing
	- Sample or preprocess the dataset for efficient batch inference.
7. Classify all articles by sentiment
	- Apply the sentiment model to all articles and map results to categories.
8. Extract named entities as tags
	- Use a NER model to extract unique named entities from each article and add as tags.
9. Generate a FAQ for each article
	- Use a question-answering model to generate a relevant question and answer for each article.
10. Summarize all articles
	- Use a summarization model to create concise summaries for each article.
11. Visualize and review results
	- Display and plot the distribution of enriched features; flag low-confidence or ambiguous cases for review.
12. Export enriched dataset
	- Save the results for downstream use or integration.

##### 5. Code conventions and constraints
- Keep code simple and readable, using standard libraries (pandas, transformers) unless otherwise required.
- Prioritize clarity and reproducibility over optimization or advanced engineering.
- Misclassifications may occur, especially with ambiguous or sarcastic headlines.
