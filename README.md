# python-challenge

[![](img/python.jpg)]()   

## Introduction

This project is made to help companies to carry out different activities using the power of programming languages, in this case python is the selected programin lenguaje.

This project is divided into 2 different themes that are:

- PyBank
- PyPoll

These will be explained in more detail below.

## PyBank

[![](img/bank.jpg)]()  

In this proyect we  developed a Python script that analyze the financial records of a company. The goal of this script are make some calculation which are the following:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The net total amount of "Profit/Losses" over the entire period
- The average of the changes in "Profit/Losses" over the entire period
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in losses (date and amount) over the entire period

#### Data

For this project the information used is in the resources folder 'budget_data.csv'. The dataset is composed of two columns: Date and Profit/Losses.

##### Schema

|      Column    | Data Type |
| -------------- |---------- |
|      Date      |   `date`  |
|  Profit/Losses |   `int`   |

#### Tools

The following tools were used to developed the program with the analysis

- Python 3
- Pandas

#### Output

```
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)

```



