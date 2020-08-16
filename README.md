# Project Euler Solutions
Solving Project Euler problems.

### What is Project Euler?
Named after the famous mathamatician [Leonhard Euler](https://en.wikipedia.org/wiki/Leonhard_Euler) (Sounds like 'oiler'), a man so profoundly influential in math that many things are named after the first person to discover/prove something *after* he did to prevent everything from having 'Euler' in it's name. 
This is a collection of programming and math challange to test and learn programming and logic skills.  

### About this repo
I wrote these solutins in Python 3 using a number of different programming techniques. In many cases helper functions are included and can take arguments. This was done to make the solutions more universal so rather than having a 'magic number' in the code that technically answers the question posited you can feed in the test case and get a result. For example in `problem_1` the question asks for the sum of all numbers that are multiples of 3 or 5 below 1000; you'll find a one-liner that solves the problem but relies on the number `1000` being hard coded which makes it useless if the problem becomes "What's the same sum for numbers up to 2000?". There is also a helper function that will give all of multiples used to get that sum because I wanted to see what they were.