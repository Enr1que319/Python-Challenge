# python-challenge

[![](img/python.jpg)]()   

## Introduction

This project is made to help companies to carry out different activities using the power of programming languages, in this case python is the selected programin lenguaje.

This project is divided into 2 different themes that are:

- PyBank
- PyPoll

These will be explained in more detail below.

## PyBank

[![](img/bank.png)]()  

In this proyect we  developed a Python script that analyze the financial records of a company. The goal of this script is to make some calculations which are the following:

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

The following tools were used to developed the program with the analysis:

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

## PyPoll

[![](img/Vote.jpg)]()  

In this proyect we  developed a Python script that can helps a small rural town to modernize the vote counting process.
The goal of this script is to make some calculation which are the following:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote.

#### Data

For this project the information used is in the resources folder 'election_data.csv'. The dataset is composed of two columns: Voter ID, County and Candidate.

##### Schema

|      Column    | Data Type |
| -------------- |---------- |
|   Voter ID     |   `int`   |
|   Country      |   `str`   |
|  Candidate     |   `str`   |

#### Tools

The following tools were used to developed the program with the analysis:

- Python 3
- Pandas

#### Output

```
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------



```
