# TDD 101 with Python
This repository shows concepts and exercises related to TDD and automated testing.

Disclaimer: this repo is a work in progress, if you have any suggestion please contact me.

## Automated Testing
What for? 

* Do not repeat the same test over and over again
* Be save again regression errors
* Have confidence while refactoring

## Test Pyramid

I don't want to duplicate information, I recommend reading this excellent post of Martin Fowler [Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html).

## Test Drive Development (TDD)
As simple as this:

1. Write a test
    1. You better start with the name of the test in the following format when possible:
    
        `
        [Name of the method]_[what it is supposed to do]_[under what conditions]
        ` 
        
        Nice name examples can be found in the *sum_of_numbers* folder
     
    2. Write the three parts of the test:
        
        `
        Test settings, test execution, assertion
        `
2. Run the test and see it fail
3. Write the minimum amount of code to pass the test
4. Repeat the cycle
   * Use another set of parameters to be passed to the method
   * Think of different values the parameters could have