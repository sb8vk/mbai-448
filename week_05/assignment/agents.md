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
- Sentiment is determined using a transformer-based model applied to the article headline (or full text if available).
- Model outputs are mapped to categories: 'Good News 🎉', 'Bad News 👎', or 'Just News 🤷' based on label and confidence threshold.
1. Data loading and inspection
2. Environment setup and model loading
3. Sentiment classification of headlines/articles
4. Mapping sentiment to news categories (Good, Bad, Just News)
5. Adding results to the dataset and reviewing outputs
6. (Optional) Visualizing or exporting categorized news

##### 5. Code conventions and constraints
- Keep code simple and readable, using standard libraries (pandas, transformers) unless otherwise required.
- Prioritize clarity and reproducibility over optimization or advanced engineering.
- Misclassifications may occur, especially with ambiguous or sarcastic headlines.
