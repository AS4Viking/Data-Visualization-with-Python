# -*- coding: utf-8 -*-
"""Ajdin_Salihovic_3_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wjbh9jc8MUwzzONFP7mwbS-SQpO9xln3
"""

# Load the data using Pandas.
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

# Load your new dataset
data = pd.read_csv("coursea_data.csv")

data.head()

# Data cleaning
data = data.dropna()

# Identify the top 5 course providers
top5_organizations = data['course_organization'].value_counts().nlargest(5)

# Plotting the top 5 course providers
plt.figure(figsize=(10, 6))
top5_organizations.plot(kind='bar', color='skyblue')
plt.title('Top 5 Course Providers')
plt.xlabel('Course Organization')
plt.ylabel('Number of Courses')
plt.show()

# Filter data for the top 5 course providers
top5_data = data[data['course_organization'].isin(top5_organizations.index)]

# Convert 'course_difficulty' to categorical
top5_data['course_difficulty'] = pd.Categorical(top5_data['course_difficulty'], categories=['Beginner', 'Intermediate', 'Advanced', 'Mixed'])

# Visualize the most popular difficulty level among the top 5 course providers
plt.figure(figsize=(12, 6))
sns.countplot(x='course_difficulty', data=top5_data, hue='course_organization', order=['Beginner', 'Intermediate', 'Advanced', 'Mixed'])
plt.title('Most Popular Difficulty Level Among Top 5 Course Providers')
plt.xlabel('Difficulty Level')
plt.ylabel('Count')
plt.show()

#  NEW

# ...

# Most Popular Certificate Types
plt.figure(figsize=(12, 6))
sns.countplot(x='course_Certificate_type', data=data, order=data['course_Certificate_type'].value_counts().index, palette='viridis')
plt.title('Most Popular Certificate Types')
plt.xlabel('Certificate Type')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()

# Average Course Ratings for the Most Popular Organizations
avg_ratings_by_organization = data.groupby('course_organization')['course_rating'].mean().sort_values(ascending=False).head(5)
plt.figure(figsize=(10, 6))
avg_ratings_by_organization.plot(kind='bar', color='skyblue')
plt.title('Average Course Ratings for Top Organizations')
plt.xlabel('Course Organization')
plt.ylabel('Average Rating')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()

# Courses with the Best Ratings
best_rated_courses = data.sort_values(by='course_rating', ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x='course_rating', y='course_title', data=best_rated_courses, palette='plasma')
plt.title('Top Best-Rated Courses')
plt.xlabel('Course Rating')
plt.ylabel('Course Title')
plt.show()

# Explanation and Results

# The provided code conducts an exploratory data analysis (EDA) on a dataset containing information about courses, focusing on three key features: course rating, course difficulty, and the number of students enrolled. The analysis aims to uncover patterns and variations across different course organizations.

# Analysis of Course Ratings:
# The box plots display the distribution of course ratings for each organization, allowing us to compare the median, spread, and potential outliers. The accompanying bar chart reveals the number of courses offered by each organization.
# Results: Organizations with higher median ratings and a larger number of courses may be considered more successful or popular.

# Analysis of Course Difficulty:
# Similar to ratings, the code examines the distribution of course difficulty levels across organizations. The goal is to identify organizations that offer courses with varying difficulty levels.
# Results: Organizations catering to diverse difficulty levels may attract a broader audience, addressing the needs of both beginners and advanced learners.

# Analysis of Enrollment:
# The third set of plots explores the number of students enrolled in courses offered by different organizations. This provides insights into the popularity and reach of courses.
# Results: Organizations with higher enrollment counts suggest a larger impact and more widespread appeal.

# Suggestions for Improvement

# 1. **In-depth Rating Analysis:**

#   - Conduct statistical tests to compare ratings between organizations and identify statistically significant differences.
#   - Explore potential correlations between course ratings and other features, such as difficulty or enrollment.

# 2. **Comprehensive Difficulty Analysis:**
#   - Consider categorizing difficulty levels into distinct groups (e.g., easy, intermediate, advanced) for a clearer interpretation.
#   - Analyze the distribution of difficulty levels within each organization to understand their course diversity.

# 3. **Enrollment Trends Over Time:**
#   - If the dataset includes a timestamp, explore enrollment trends over time to identify seasonality or long-term patterns.
#   - Consider time series analysis to uncover any temporal dependencies in course popularity.

# 4. **User Interaction Analysis:**
#   - If available, incorporate additional data on user interactions (e.g., reviews, comments) to gauge user engagement.
#   - Explore sentiment analysis on user reviews to understand the sentiment associated with courses and organizations.

# 5. **Interactive Dashboards:**
#   - Create interactive dashboards for a more user-friendly exploration of data. Users can filter by organization, difficulty, or other relevant factors.
#   - Include dynamic visualizations that update in real-time as users interact with the dashboard.

# 6. **Peer Comparison:**
#   - Extend the analysis to compare organizations directly, highlighting strengths and weaknesses relative to peers.
#   - Consider benchmarking against industry averages or standards to provide context.

# 7. **Collaborative Filtering:**
#   - Implement collaborative filtering techniques to recommend courses based on user preferences and behaviors.
#   - Utilize machine learning models for personalized course recommendations.

# 8. **Data Quality Checks:**
#   - Perform additional checks for data consistency and accuracy to ensure reliable insights.
#   - Address any potential outliers or anomalies that may impact the analysis.

# 9. **Collaborate with Domain Experts:**
#   - Collaborate with experts in the education domain to gain deeper insights and context for the analysis.
#   - Seek feedback from educators or professionals to validate findings and interpretations.

# 10. **Regular Updates:**
#    - If the dataset is regularly updated, schedule periodic analyses to capture evolving trends and patterns over time.
#    - Keep the analysis up-to-date with the latest data to provide relevant insights.

#