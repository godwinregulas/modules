# ASSIGNMENT 1

1. Simulate Sales Data using NumPy:
   - Create arrays for 100 sales transactions:
     - product_ids: Random integers from 1001 to 1010
     - quantities: Random integers between 1 and 5
     - prices: Random floats between 10 and 100 (rounded to 2 decimals)
     - dates: 100 random dates between Jan 1 and Jan 10, 2025

2. Create a DataFrame using Pandas:
   - Combine the arrays into a DataFrame called sales_df with columns:
     - ProductID, Quantity, Price, Date

3. Add Total Sale Column:
   - Create a new column: TotalSale = Quantity * Price

4. Introduce Missing Data:
   - Randomly set 5 Price values to NaN
   - Fill missing prices with the mean price

5. Group and Aggregate:
   - Group by ProductID and calculate:
     - Total quantity sold
     - Total revenue

6. Visualize using Matplotlib:
   - Bar chart: Total revenue per ProductID
   - Histogram: Distribution of TotalSale values
   - (Bonus) Subplot: One subplot with the bar chart, another with the histogram
  

# ASSIGNMENT 2

  1.	Generate Data (Pandas + NumPy)
	•	Create a dataset of 500 employees with the following columns:
	•	Employee_ID (1–500)
	•	Department (Random choice: HR, IT, Finance, Sales)
	•	Salary (10k to 50k)
	•	Experience_Years (Random integers between 1–20)
	•	Performance_Score (Random integers 1–5)
	•	Randomly introduce missing values in 10% of Salary and Experience_Years.
	2.	Data Cleaning
	•	Identify missing values
	•	Fill missing Salary with the median of that department.
	•	Fill missing Experience_Years with the overall mean.
	3.	Analysis
	•	Group employees by Department and calculate:
	•	Average Salary
	•	Average Performance Score
	•	Average Experience
	4.	Visualization (Matplotlib + Seaborn)
	•	Create a bar chart showing average salary per department.
	•	Create a boxplot of salaries across departments to check distribution.
	•	Create a scatter plot of Experience_Years vs Salary, colored by Performance_Score.


# ASSIGNMENT 3

  1.	Load Data
	•	Read the CSV file into a Pandas DataFrame.
	•	Check for missing values and handle them appropriately (fill/replace/drop).
	2.	Data Cleaning & Manipulation
	•	Convert the Date column to proper datetime format.
	•	Extract Year and Month as new columns.
	•	Add a new column Revenue_per_Unit = Revenue / Units_Sold.
	3.	Exploratory Analysis
	•	Find the top 3 products by total revenue.
	•	Calculate average monthly sales per region.
	•	Use groupby and agg to get total revenue and average units sold per product.
	4.	NumPy Integration
	•	Use NumPy functions to calculate:
	•	Overall mean, median, and standard deviation of Revenue.
	•	A NumPy array of Revenue_per_Unit for correlation analysis.
	5.	Visualization (Matplotlib/Seaborn)
	•	Plot a bar chart of total revenue per region.
	•	Create a line plot showing monthly revenue trends.
	•	Plot a scatter plot of Units_Sold vs. Revenue, colored by Region.


# ASSIGNMENT 3

- create a 1D and 2D arrays
- create a 2D array having values from 1 to 50
- reshape a 2D array
- change a 3D array to 2D array
- example for broadcasting
-  join 2 array using concatenate
- example for vstack and hstack
- create a DataFrame with colums - Name and Marks for 3 students
- find average of Marks
- create another DataFrame in a way to merge with the above DataFrame
- use merge,join and concat for joining 2 DataFrames
- plot a histogram using Marks
