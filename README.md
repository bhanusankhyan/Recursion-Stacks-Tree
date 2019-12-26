# Problem 1:

Given an array X and a number y, find the contiguous subarray of smallest length whose sum is greater than y. Note that array X contains only the positive numbers

### Example 

Test 1 - X = [9, 18, 42, 98], y = 21

Output subarray can be either [42] or [98]

Test 2 - X = [9, 18, 2, 4, 5], y = 21

Output subarray of smallest length is  [9, 18]



# Problem 2:

You are given a CSV file employees.csv as shown below. In this file,  the managerid column refers to the id of the employee who is a manager. So, the manager is also an employee. For example Ramesh is the manager of Dinesh in the CSV file given below.

employees.csv

Id, name, managerid
1, Dinesh, 2
2, Ramesh, 4
3, Sandeep, 4
4, Abhishek, NULL

You have to read this csv file and create a tree like structure in which parent node is the manager of the child node. You can use “\t” tab for indentation or showing the hierarchy.

### Output for the above file - 

Abhishek - 4
    Ramesh - 2
        Dinesh - 1
    Sandeep - 3

