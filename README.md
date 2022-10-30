* AB breakdown
Part A and Part B both exist in p1.py

* Description
For part A, I first get the input from the file, then split out each words that are separated by " " to store them in an array. If they are 'Mr. ' or 'Mrs. ', I combine it with the next word. I handle abbreviation by first spliting the words from '.' and store them in an array. For each element in the array, if it is a letter, I combine it with the previous letters. If it is not a letter, I split it out and become a token itself. For contractions, I remove the "'" to combine the word together. For handeling punctuations, I find the puctuations in each word and remove them. Each word that is separated by punctiuation will become a token. 
For handeling stop words, I first read each stop word in the file and store them in an array. I use the array that I already tokenized and look for each stop words in there by comparing each token to each stop words. If it is a stop word, I remove it out of the array. 
Then I handle 2 steps of Porter stemming. For step 1a, I first find if 'sses' in each token and replace it with 'ss'. Then I delete 's' by checking if there is a vowel before the 's'. Then I replace 'ied' and 'ies' by 'i' with its length is greater than 4 and by 'ie' otherwise. For step 1b, created 2 functions to handle removing 'eed' and 'eedly', and handle removing 'ed', 'edly', 'ing', 'ingly'. The result is an array that has been tokenized, removed stop words, and stemmed.

For Part B, handle reading and writing the file the same way as Part A. I then used Part A function to tokenize, remove stop words, and stem. I then created a dictionary that store all tokens and the number of times they appear. Next, I sort the dictionary and get the first 300 items that occur the most in the list.

I think it takes a lot of time for my code to run my handle_punctuation() function because it compares each punctuation in the list to each character in the word. It also takes a lot of time to remove an empty string because each time we remove, it rearanges the array. Finally, it takes a large amount of time to remove stop words because my tokens are stored in an array, and each time a stop word is found, I remove it, and it will rearrange the whole array. With a large input, this will be very costly in time.

* Libraries
I use matplotpb to draw the word growth graph

* Dependencies
I use matplotpb to draw the word growth graph
Instruction:
- In your terminal, type:
pip3 install -U matplotlib

* Building
On your local code editor, hit run

* Running
Both of my Part A and Part B are in one file. If you run, it will read and write the file for both parts