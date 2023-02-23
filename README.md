# Fetch-Coding-Exercise

## Overview
This project report's user's point balances of all payers. User's points may come from transaction mutiple payers. 
Each transaction record contains: payer (string), points (integer), timestamp (date) and will be stored in transaction.csv.
The rule of spending points is oldest points (based on timestamp) need to be spent first. Also, no points will go negative when user
check their balance. 

---

## Table of Contents

- [Code Installation](#installation)
- [Usage](#usage)

---
## Code Installation

To run the script, make sure you have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed on your machine.

```
git clone https://github.com/ZejunZhou/Fetch-Coding-Exercise.git

cd Fetch-Coding-Exercise

```
---
## Usage

To run the script, make sure you have [Python3](https://www.python.org/downloads/) installed on your machine. Then, go to the project directory and run the following command:

```
Python3 practice.py argument1 argument2
```

* argument1 is the amount of points to spend
* argument2 is the name of csv file storing payer's points, which has to be **transactions.csv**

### Example

User spend 5000 points from their account

```
python3 practice.py 5000 transactions.csv

```