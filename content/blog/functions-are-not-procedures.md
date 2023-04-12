---
title: "Functions are not procedures"
date: 2023-04-26
draft: false
---

I would like to play around a bit with the [go programming language](https://go.dev/). It is not a bad idea to learn a new programming language every once in a while to get to know different ways of thinking about computational problems. I did that extensively in the first years of my professional career when I was working abroad and had a lot of time during my lonely hotel nights. I do it very little today where I prefer to spend my free time with my family.

I mostly work with Oracle SQL and PL/SQL in my job. The last time I played around with alternative languages was in 2019 when I studied some data science with R and Python. Now I would like to learn some go because it's the language in which Hugo is written, the static site generator which I use to render this site. To get started, I evaluated several resources and finally decided to buy John Arundel's book ["For the Love of Go"](https://bitfieldconsulting.com/books/love). A great book, as far as I can tell after the first three chapters.

In these first chapters, a `calculator` package is built. It contains, amongst others, the functions `Add` and `Multiply`:

```go
// Package calculator does simple calculations.
package calculator

// Add takes two numbers and returns the result 
// of adding them together.
func Add(a, b float64) float64 {
  return a + b
}

// Multiply takes two numbers and returns the result 
// of multiplying one by the other.
func Multiply(a, b float64) float64 {
  return a * b
}
```

I like the way packages and functions are introduced, and I especially like the test-driven approach promoted by the book and by the language itself. A `calculator_test` package is presented immediately. It contains test functions for all the functions in the `calculator` package.

What I do *not* like in the above code snippet, however, is the *names* of the two functions.

`Add` and `Multiply` are verbs in imperative mood. They are *commands*. Commands make good names for *procedures* but not for functions. Procedures like `write`, `draw`, `save` should do what their name implies, and they should not return any result. Functions, on the other hand, do return a result, and they should be named by what they return. They should also not do anything except return a result or, to be more precise, they should not produce any abstract side-effects. That's what Bertrand Meyer calls the **Command-Query Separation Principle**[^1].

[^1]: Bertrand Meyer explains the Command-Query Separation Principle in his influential book "Object-Oriented Software Construction, 2{{< super "nd" >}} edition" (OOSC-2), on page 751. The book's full text has recently been made [freely available online](https://bertrandmeyer.com/OOSC2/).

If we name the functions by what they return, namely the `Sum` and the `Product` of two numbers:

```go
// Package calculator does simple calculations.
package calculator

// Returns the sum of a and b.
func Sum(a, b float64) float64 {
  return a + b
}

// Returns the product of a and b.
func Product(a, b float64) float64 {
  return a * b
}
```

then the code which calls them looks a lot nicer:

```go
s := calculator.Sum(2, 3)
p := calculator.Product(4, 5)
```

This reads as: 
- Let `s` be the **sum** of 2 and 3.
- Let `p` be the **product** of 4 and 5.

I find this a lot more intuitive than any of the following:
- Let `s` be the *result* of adding 2 and 3.
- Multiply 4 by 5 and assign the *result* to `p`.

If you only program in languages which treat procedures just as functions which do not return any result (or maybe return something like `void`), then this insistance on different naming patterns might seem a mere matter of taste. But there are languages which distinguish strongly between functions (which are *called*) and procedures (which are *executed* or *applied*).

To Oracle, calling a function which returns a value is conceptually equal to selecting a value from a table, so the syntax is the same. For our example above, it would be:

```sql
select calculator.Sum(2, 3) from dual;
select calculator.Product(4, 5) from dual;
```

A procedure, on the other hand, needs to be executed:

```sql
exec calculator.Start;
```

Fortunately, my developer colleagues at Avaloq do care about function and variable names and about many other small things which make our code more readable, understandable and maintainable.