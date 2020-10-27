# Green Thumb


SheHacks 2018 project that detects whether or not an item is compostable. 

Function: 

1) text image of the item to a number 
2) the program will then text back to the user if the item is compostable or not

-- Had a 96.6667% success rate

How I did it:

Basically I used the Twillio API for its messaging services and machine vision API
called Clarifai to generate a list of words associated with the incoming image.
