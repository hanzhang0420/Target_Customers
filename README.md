# Target_Customers
Binary Classification, Offer Promotion to Target Customers 

Part1: data clean 

Part2: iaps customer 

Part3: model 



Target Customer Classification Summary 
Han Zhang

Introduction 


Four tables are provided and contain 22576 customers’ time based activity information. I use the data before the first 24 hr break (a user does not use the app for 24 hrs). There are two reasons for that 1) before that time break, 70% self-converted customers have made their first purchases. It guarantees the bulk of the revenue from true payers. 2)  46.4% of users left after the 24 hr break and sending them promotion offer may help them stay.   

Feature Engineer  
Some of the Generated Features:
total_story is the total num of unique stories&chapters episode users played.
active_session/spend_day are the number of days each user that start/spend money at least one session in the app on any given day.
avg_session_duration averaged session duration.
avg_session_per_day averaged number of sessions per day.
avg_amount_per_day averaged spent amount per day.
weekend the weekend information of the installment (0 is weekday and 1 is weekend).

Self-Converted Customers 
•	47.4% of true payers make the first purchase during the first day of play. 
•	The more customers spend in the game; the more revenue they generate. 
•	True payer customers are more engaged to the game; retention rate drops slower. 
•	67.6% of them buy more than once. 

Model: Target Customers 
Models: 1. Logistic Regression      2. KNN       3. Random Forest
I choose these three models because 1) suitable for classification problem 2) they can return probability predictions and therefore the threshold can be modified. The soft label is important here (I adopt 0.1 as the threshold). 3) fewer parameters to tune.  

Metrics:  False Negative/ (False Negative + True Negative), Recall 
Results:  Apply the model to all the users, FN/(FN+TN) can achieve ~0.0035.   
Important Features: 


Summary: As shown by the model, how users are engaged with the game is important to determine whether they are true payer or not. How frequency they play the game, how much gems they spend (time & spend) are important to explore.  

Question 1. Specify a target group of users. Justify your choice using the sample data.

Building a model to classify true payer and non-payers is still the best way to do I think. For each user, I find the time point when the user stops using the game over 24 hr and use the data before that time point. Then apply the classification model (20 features) to find the "non-payers". The important features are related to the engagement of each user. 
Question 2. Specify a test and evaluation protocol. How long should the test run? How will you know if you have successfully increased revenue?

Assumption: 
The promotion conversion rate is missing and here I adopt the promotion conversion rate of 2%, statistical power 80%, and a confidence interval of 95%. 
A/B test:
Randomly group new users into treatment and control groups. The experiment runs for 7 days (eliminate bias from weekend/weekdays, enough time to collect data, enough time for customers to convert).  Sample Size ~10000 per group.  

Control group: No promotion. Revenue rate (0.1136).   
Treatment group: Based on the users’ data before the 24hr break, apply models to classify non-payer customers and send promotion offer to those customers. Lifted revenue rate (0.13).  

Comments: 
Other metrics worth looking at, the total number of payers, Gini index of the payers, the retention rate etc.  Long-term effect: some non-payers may transit to be true payers because of the promotion pay.  

Future Action Items   
The analysis is still daily based and the hourly based analysis might be useful.  
Cross-device tracking? Some users might use multiple devices to play the game.  That explains why some users pay even before the first session. 
What factors affect the conversion time and the amount of revenue?  I did not dig deep into the iaps data, features such as prod type might be useful. 


