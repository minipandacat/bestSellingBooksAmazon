import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#created venv and installed pandas
#https://code.visualstudio.com/docs/python/environments

df = pd.read_csv('.venv/bestsellingbooks/booksAmazon.csv')

#showing dataframe
print(df)
#showing first and last 10 rows
print(df.head(10))
print(df.tail(10))

#showing information
print(df.info())

#showing statistics for each column
print(df.describe())

#showing columns 
print(df.columns)

#showing number of rows and columns
print(df.shape)

#removing duplicate rows
df.drop_duplicates(inplace=True)

#renaming columns
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

#converting price to float - makes it easier to work with
df["Price"] = df["Price"].astype(float)

#checking data
print(df.head(10))

authorCounts = df["Author"].value_counts()
print(authorCounts)

avgRating = df["Rating"].mean()
print(avgRating)

avgRatingByGenre = df.groupby("Genre")["Rating"].mean()
print(avgRatingByGenre)

avgRatingByAuthor = df.groupby("Author")["Rating"].mean()
print(avgRatingByAuthor)

mostPopularBooks = df.nlargest(10, "Rating")
print(mostPopularBooks)

leastPopularBooks = df.nsmallest(10, "Rating")
print(leastPopularBooks)

# Plotting the different charts
fig, axes = plt.subplots(3, 2, figsize=(15, 15))
# Bar plot for author counts
authorCounts.plot(kind='bar', ax=axes[0, 0])
axes[0, 0].set_title('Author Counts')
axes[0, 0].set_xlabel('Author')
axes[0, 0].set_ylabel('Counts')

# Horizontal bar plot for average rating by genre
avgRatingByGenre.plot(kind='barh', ax=axes[0, 1])
axes[0, 1].set_title('Average Rating by Genre')
axes[0, 1].set_xlabel('Rating')
axes[0, 1].set_ylabel('Genre')

# Bar plot for average rating by author
avgRatingByAuthor.plot(kind='bar', ax=axes[1, 0])
axes[1, 0].set_title('Average Rating by Author')
axes[1, 0].set_xlabel('Author')
axes[1, 0].set_ylabel('Rating')

# Scatter plot for most popular books
axes[1, 1].scatter(mostPopularBooks['Author'], mostPopularBooks['Rating'], color='g')
axes[1, 1].set_title('Most Popular Books')
axes[1, 1].set_xlabel('Author')
axes[1, 1].set_ylabel('Rating')

# Scatter plot for least popular books
axes[2, 0].scatter(leastPopularBooks['Author'], leastPopularBooks['Rating'], color='r')
axes[2, 0].set_title('Least Popular Books')
axes[2, 0].set_xlabel('Author')
axes[2, 0].set_ylabel('Rating')

# Pie chart for genre distribution
genreCounts = df['Genre'].value_counts()
genreCounts.plot(kind='pie', ax=axes[2, 1], autopct='%1.1f%%')
axes[2, 1].set_title('Genre Distribution')
axes[2, 1].set_ylabel('')

plt.tight_layout()
plt.show()

sns.countplot(x="Genre", data=df)
plt.show()

#show genre distribution
df['Genre'].value_counts()

#show genre distribution in percentage
df['Genre'].value_counts() / len(df)*100

#showing distribution
#https://www.kaggle.com/code/ongchoa/bestselling-books-data-exploration/notebook
""" def show_distribution(var_data):
    from matplotlib import pyplot as pyplt

    # Get statistics
    min_val = var_data.min()
    max_val = var_data.max()
    mean_val = var_data.mean()
    med_val = var_data.median()
    mod_val = var_data.mode()[0]

    print(f"{var_data.name}\nMinimum: {min_val:.2f}\nMaximum: {max_val:.2f}\nMean: {mean_val:.2f}\nMedian: {med_val:.2f}\nMode: {mod_val:.2f}\n")

    # Create a figure for 2 subplots (2 rows, 1 column)
    fig, ax = pyplt.subplots(2, 1, figsize = (10, 4))

    # Plot the histogram
    #https://matplotlib.org/stable/gallery/statistics/hist.html#histograms
    ax[0].hist(var_data, color = 'royalblue', edgecolor = 'black')
    ax[0].set_ylabel('Frequency')

    #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html
    #Add vertical lines for the mean, median, and mode
    ax[0].axvline(x=min_val, color = 'gray', linestyle = 'dashed', linewidth = 2)
    ax[0].axvline(x=mean_val, color = 'cyan', linestyle = 'dashed', linewidth = 2)
    ax[0].axvline(x=med_val, color = 'red', linestyle = 'dashed', linewidth = 2)
    ax[0].axvline(x=mod_val, color = 'yellow', linestyle = 'dashed', linewidth = 2)
    ax[0].axvline(x=max_val, color = 'gray', linestyle = 'dashed', linewidth = 2)

    # Plot the boxplot
    ax[1].boxplot(var_data, vert = False)
    ax[1].set_xlabel('Value')

    # Add a title to the Figure
    fig.suptitle(var_data.name)

numericFields = [ "Rating", "Reviews", "Price"]
for col in numericFields:
    show_distribution(df[col])

q1 = {}
q3 = {}
IQR = {}
for col in numericFields:
    q1[col] = df[col].quantile(q=0.25)
    q3[col] = df[col].quantile(q=0.75)
    IQR[col] = q3[col] - q1[col]
    df = df[df[col] > (q1[col] - 1.5 * IQR[col])]
    df = df[df[col] < (q3[col] + 1.5 * IQR[col])]

for col in numericFields:
    show_distribution(df[col])

for col in numericFields:
    show_distribution(df.boxplot(column=col, by='Genre', figsize=(8, 8))) """