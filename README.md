# python-challenge

For this assignment, we created two scripts (main.py) that loaded csv files and then crunched some numbers to provide a general summary of either finances (part 1) or polling results (part 2). 

Much of my code is commented so one can find my strategy and workflow in the scripts. That said, below I highlight a few useful functions that helped quit a bit:

* **Py-Bank**: I struggled quite a bit with trying to find the difference between to successive rows in the csv file. Creating the for loop that used the variable to iterate through the profit/loss column would only return the value of the current iteration, but not the next iteration. I couldn't figure out good solution using this strategy. Therefore I googled around and found that I can use the **enumerate** function to return the value of the iteration. Using **enumerate**, I could then track the index number of the for loop, and therefore easily grab the profit/loss value of the next iteration. By grabbing both values, I could then easily calculate the difference and track  month-to-month changes. 

* I used the **round** function to bring the statistics values to two decimals.

* **Py-Poll**: The loaded csv file was quite large, and therefore writing the script and debugging could take some time. As a short-cut, I forced the for loop that grabbed VoterID, county and candidate exit early by making a conditional If statement stating that if the iteration exceeded a value, it would exit the loop (i.e. **break**)

* **Py-Poll**: I used the sorted function to sort polling results in descending order.

* **Py-Poll**: The markdown file for the assignment presented polling percentages to three decimals. To achieve this I used **'{0:.3f}'.format**.

* **Py-Poll**: You can multiply dashes to make many dashes: **fileOut.write("-" *30)**

* Use **/n** with either **print()** or **fileOut.write** to append a line.

* In summary, here are the useful functions/tools I found:

  * **enumerate**:  https://book.pythontips.com/en/latest/enumerate.html 

  * **break**:  https://www.tutorialspoint.com/python/python_break_statement.htm 

  * **'{0:.3f}'.format**:  https://pyformat.info/ 

  * **fileOut.write("-" *30)**

    