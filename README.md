# Quantifying audience likes and dislikes of movies 

![alt text](https://github.com/abhisekswain/movie-user-ratings/blob/master/shawshank_redemption.jpeg)

**Can we predict the audience reception for a movie based on certain factors?**  

This is the question I set out to answer for my second project of Metis. I have always been a fan of low-budget, off-the-beat cinema and my choices incline more towards films that are thought provoking and original than big-budget action films or franchise dramas. Thus, using imdb user ratings as my dependent variable, I wanted to analyze factors that make audiences like or give high ratings to films.

**Scrapy**

I started by getting a sense for what movie data is publicly available for scraping. I scraped IMDB for all movies release in the US between 1973 and 2016, the-numbers.com and downloaded consumer price index(cpi) data from [https://www.bls.gov/cpi](https://www.bls.gov/cpi). This lead me to a relatively comprehensive source for the features I was looking to use.

I started with using BeautifulSoup, but later switched to scrapy, which had a a little longer to learn, but was easier to use once I learnt it. My target variable for this project was the IMDb Rating for each movie. In my opinion, this is a good indicator of audience likeability for any movie. After combining all the scraping data, which was in 3 csv files, I ended up with 1400+ movies.

**Feature selection**  

I created a feature set consisting of a mix of numerical and categorical variables. My numerical features were:  
1. Number of ratings  
2. Meta-critic score (out of 100)  
3. Runtime
4. Budget

The budget was adjusted for inflation using the cpi data as the original data reported budget, the year the movie was released.






