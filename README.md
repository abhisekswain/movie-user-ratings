# Quantifying audience likes and dislikes of movies 

![alt text](https://github.com/abhisekswain/movie-user-ratings/blob/master/shawshank_redemption.jpeg)

**Can we predict the audience reception for a movie based on certain factors?**  

This is the question I set out to answer for my second project of Metis. I have always been a fan of low-budget, off-the-beat cinema and my choices incline towards films that are thought provoking and original than big-budget action films or franchise dramas. Thus, using imdb user ratings as my dependent variable, I wanted to analyze factors that make audiences like or give high ratings to films.

**Scrapy**

I started by getting a sense for what movie data is publicly available for scraping. I scraped IMDB for all movies released in the US between 1973 and 2016, the-numbers.com and downloaded consumer price index(cpi) data from [https://www.bls.gov/cpi](https://www.bls.gov/cpi). This lead me to a relatively comprehensive source for the features I was looking to use.

I started with using BeautifulSoup, but later switched to Scrapy, which took longer to learn, but was easier to use once I learnt it. My target variable for this project was the IMDb Rating for each movie. In my opinion, this is a good indicator of audience likeability for any movie. After combining all the scraping data, which was in 3 csv files, I ended up with 1400+ movies.

**Feature selection**  

I created a feature set consisting of a mix of numerical and categorical variables. My numerical features were:  
1. Number of ratings  
2. Meta-critic score (out of 100)  
3. Runtime
4. Budget

The budget was adjusted for inflation using the cpi data as the original data reported budget for the year the movie was released. My categorical features consisted of the following:
1. Top 20 grossing actors from 1970-2016
2. Top 10 grossing directors from 1970-2016
3. Year of release
4. MPAA rating

In the end I had exactly 100 features. The ipython notebook "movie_user_rating_modelling.ipynb" shows how I created the feature list.  

**Modeling with Linear Regression**

The data munging and cleaning took quite a while, so I was excited when I got all the data ready for modelling. I first ran Oridinary Least Squares (OLS) regression, which yielded an R-squared value of 0.72. But there were a number of p-values greater than 0.05. I also looked at the residuals, the output and the Q-Q plot to do a sanity check and confirm that there was no heteroskedasticity present. Below are 3 plots:

![alt text](https://github.com/abhisekswain/movie-user-ratings/blob/master/plots/residuals_ols.png "Residuals")  
![alt text](https://github.com/abhisekswain/movie-user-ratings/blob/master/plots/predicted_vs_actual.png "Predicted vs Actuals")  

After the intial analysis, I decided to use Lassor regression with cross-validation. I chose Lasso over Ridge as there were a large number of categorical variables in my dataset and Lasso does a good job of seeting those to zero. The score I obtained for Lasso, was 0.62 and the top features are shown below:
1. ratingnum - number of people who rated the movie
2. meta_score
3. Drama
4. runtime
5. mpaa_rating[T.R]

![alt text](https://github.com/abhisekswain/movie-user-ratings/blob/master/plots/features.png)

**Conclusion**

While it appears that highly rated movies and movies with higher critics ratings seems to have higher IMDb ratings, it is not obvious as the correlation matrix would have indicated. It is interesting to note that genres that contain Drama and movie runtime have a large affect on how much the audience likes a movie.




