# simpleduplex
A script to help users print two-side pages in special cases
Actually, my intention with this script is help users to print two-side jobs in a manual fashion. But sometimes users may have special requirements. Let's say that the document they want to print is 7 pages, but they want to skip page 2 (because page 2 is not relevant), but they want to print all the other pages anyway, so the "regular" output for the first batch of pages would be: 
side-one: 1,3,5,7 
side-two: 2,4,6 

However, in this special case in which they want to omit certain pages, the output should be like this: 
side-one: 1,4,6 
side-two: 3,5,7 

What if they want to skip more than to pages, let's say, 2-3, so the new sequence would be: 
side-one: 1,5,7 
side-two: 4,6 

and what if they enter sequences of pages they want to avoid, for example, 2, 4-5; the output would be: 
side-one: 1,6 
side-two: 3,7 

This simple duplex script handles this type of cases, making office work easier
