# Python_Games


#### Import the randrange function from the random module
```python
from random import randrange
```



#### Define a list of words to choose from
```python
list_of_words = ['LEARNING', 'PYTHON', 'CREATING', 'GAME']
```



#### Randomly select a word from the list
```python
word = list_of_words[randrange(len(list_of_words))]
```



#### Create a string of dashes with the same length as the selected word
```python
hidden_word = '-' * len(word)
```



#### Print the hidden word to the console
```python
print(f'Hidden word is: {hidden_word}')
```



#### Set the number of incorrect guesses the player is allowed to make
```python
mistake_count = 6
```



#### Begin the game loop
```python
while mistake_count > 0 and hidden_word.count('-') != 0:
    # Initialize variables for tracking the user's guess
    index_count = 0
    letter_count = 0
```

​    
#### Prompt the user to guess a letter
```python
print('Pick a letter:')
picked_letter = input().capitalize()

# Check if the letter is in the word
for letter in word:
    if picked_letter == letter:
        hidden_word = hidden_word[:index_count] + picked_letter + hidden_word[index_count+1:]
        letter_count += 1
    index_count += 1
```

#### If the letter is not in the word, decrement the mistake count and display the hangman

```python
if letter_count == 0:
    mistake_count -= 1
    print(f'WRONG! Number of mistakes left: {mistake_count}')
    print(hangman[6 - mistake_count])

# If the letter is in the word, display the updated hidden word
else:
    print(f'CORRECT! There is a letter {picked_letter} in the secret word!')
    print(hidden_word)

# Print a separator between each guess
print('==============================================================')
```

#### If the player runs out of guesses, print "HANGED!!!"
```python
if mistake_count == 0:
    print('HANGED!!!')
    
```


#### If the player correctly guesses the word, print "CONGRATULATIONS!!!"
```python
else:
    print('CONGRATULATIONS!!!')
```

