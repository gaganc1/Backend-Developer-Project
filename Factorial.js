function factorial(n) {
    // Base case: factorial of 0 is 1
    if (n === 0) {
        return 1;
    }
    // Recursive case: factorial of n is n times factorial of (n-1)
    else {
        return n * factorial(n - 1);
    }
}

// Test the function with some values
let num = 4;
console.log(`The factorial of ${num} is: ${factorial(num)}`);

num = 8;
console.log(`The factorial of ${num} is: ${factorial(num)}`);

num = 12;
console.log(`The factorial of ${num} is: ${factorial(num)}`);
