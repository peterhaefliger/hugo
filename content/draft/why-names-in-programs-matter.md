---
title: "Why names in programs matter"
date: 2023-04-20
draft: false
---

I would like to play around a bit with the [go programming language](https://go.dev/). It is not a bad idea to learn a new programming language every once in a while to get to know different ways of thinking about computational problems. I did that extensively in the first years of my professional career when I was working abroad and had a lot of time during my lonely hotel nights. I do it very little today where I prefer to spend my free time with my family.

I mostly work with Oracle SQL and PL/SQL in my job. The last time I played around with alternative languages was in 2019 when I studied some data science with R and Python. Now I would like to learn some go because it's the language in which HUGO is written, the static site generator which I use to render this site. To get started, I evaluated several resources and finally decided to buy John Arundel's book ["For the Love of Go"](https://bitfieldconsulting.com/books/love). A great book, as far as I can tell after the first three chapters.

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

I like the way packages and functions are introduced with this practical example, and I especially like the test-driven approach promoted by the book and by the language itself. A `calculator_test` package is presented immediately. It contains test functions for all the functions in the `calculator` package:

```go
package calculator_test

import (
"calculator"
"testing"
)

func TestAdd(t *testing.T) {
  t.Parallel()
  var want float64 = 5
  got := calculator.Add(2, 3)
  if want != got {
    t.Errorf("want %f, got %f", want, got)
  }
}

func TestMultiply(t *testing.T) {
  t.Parallel()
  var want float64 = 20
  got := calculator.Multiply(4, 5)
  if want != got {
    t.Errorf("want %f, got %f", want, got)
  }
}
```

What I do *not* like about the above code snippets, however, is the names of the two functions under test.

`Add` and `Multiply` are verbs in imperative mood. They are *commands*. Commands make good names for *procedures* but not for functions. Procedures like `write`, `draw`, `save` should do what their name implies, and they should not return any result. `TestAdd` and `TestMultiply` are good examples: They do what their name implies, namely test the function they claim to test, and they do not return a result. *Functions*, on the other hand, do return a result[^1], and they should be *named by what they return*.

[^1]: In fact, functions should *not do anything but* return a result. To be more precise, they should not produce any abstract side-effects. That's what [Bertrand Meyer](https://bertrandmeyer.com/) calls the **Command-Query Separation Principle**. It guarantees referential transparency and can be informally understood as "asking a question should not change the answer". For a rigorous definition and explanation, see Bertrand's classic book "Object-Oriented Software Construction, 2{{< super "nd" >}} edition" (OOSC-2), pg. 751. The book's full text has recently been made [freely available online](https://bertrandmeyer.com/OOSC2/).

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

then the code which calls them is more expressive:

```go
s := calculator.Sum(2, 3)
p := calculator.Product(4, 5)
```

This reads as: 
- Let `s` be the **sum** of 2 and 3.
- Let `p` be the **product** of 4 and 5.

I find this a lot more intuitive than any of the following:
- Let `s` be the *result* of *adding* 2 and 3.
- *Multiply* 4 by 5 and assign the *result* to `p`.

While the first is only cumbersome, the second is actually an overspecification and violates the principle of separation of concerns as I will elaborate on further below.

Or, in the context of the above `calculator_test` package:

```go
func TestSum(t *testing.T) {
  t.Parallel()
  var want float64 = 5
  got := calculator.Sum(2, 3)
  if want != got {
    t.Errorf("want %f, got %f", want, got)
  }
}
```

As the function under test is named by what it returns, line 4 nicely reads: "We got the sum of 2 and 3". This is followed by the check on line 5: "If what we want is not what we got, then ...".[^2]

[^2]: While I am writing this, I wonder if quality would improve if code were read aloud. Should we not only have code reviews, but also "code slams"? Maybe not, but code certainly benefits from being *explained*: If the reviewer does not only read your code but you actually have to explain it to them, you will catch many things which just "don't sound right".

    And while I am writing about explaining code to the reviewer, my colleague [Uğur Gürel](https://www.linkedin.com/in/uguerel/) points me to [Rubber Duck Debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging). So the idea seems to be quite accepted that explaining code (or a concept or a design) to someone (even a rubber duck) helps uncover its flaws because it forces one to to rigorously think and reason about it instead of just glossing over it ("I know that this works - somehow...").

Unfortunately, some programming languages treat procedures just as functions which do not return any result (as go seems to do, judging from the implementation of the `calculator_test` package where `TestAdd` and `TestMultiply` are declared as `func` even though they are procedures) or which maybe return something like `void`. If you only program in languages which handle procedures this way, then my insistence on different naming patterns might seem a mere matter of taste. But there are languages which distinguish strongly between functions (which are *called*) and procedures (which are *executed*).

To Oracle, calling a function which returns a value is conceptually equal to selecting a value from a table, so the syntax is the same. For our example above, it would be:

```sql
select calculator.Sum(2, 3) from dual;
select calculator.Product(4, 5) from dual;
```

A procedure, on the other hand, needs to be executed:

```sql
exec calculator.Start;
```

With a function, the caller asks for something (in our example for the sum or the product of two numbers), while with a procedure, they ask (a package or module or object) to do something (in our example the calculator to start). It is sometimes argued that asking for a result is asking to compute that result (in our example: asking for the sum is asking to add and asking for the product is asking to multiply). But that's not true because the value could also be cached. Obeying the principle of separation of concerns, it should make no difference to the caller of the `Product` function whether the calulator multiplies the inputs to calculate the result or whether it selects the result from a pre-computed table.[^3] Asking for a result is *not* asking to compute it.

[^3]: That's what Bertrand Meyer calls the  **Uniform Access Principle**: "All services offered by a module should be available through a uniform notation, which does not betray whether they are implemented through storage or through computation." For a detailed explanation, see "Object-Oriented Software Construction, 2{{< super "nd" >}} edition" (OOSC-2), pg. 57, [freely available online here](https://bertrandmeyer.com/OOSC2/).

For the sake of completeness: There is a small variation to the recommendation that functions should be named by what they return and it applies to boolean functions, i.e. functions which return either true or false. They usually answer a yes/no question and their name  should reflect this. Boolean function names often denote a logical predicate or a property or quality of an object which can be true or false: 

```go
if button.Enabled {...}
if customer.Retired {...}
```

or maybe

```go
if button.IsEnabled {...}
if customer.IsRetired {...}
```

or, to take up the above PL/SQL calculator example again:

```sql
begin
  if calculator.Off then
    calculator.Start;
  end if;
end;
```

But do names in programs really matter? After all, they are just names. Probably not if you regard a program merely as a set of instructions for a machine. The compiler will remove them anyway. Then you might just as well name your functions f{{< sub "1" >}} to f{{< sub "n" >}}. But if you understand a program as a text to communicate interface specifications, design patterns, data structures and algorithm implementations to your fellow programmers, then you should definitely care. 

Fortunately, my developer colleagues at Avaloq do care about function and procedure and variable names and about many other small things which make our code more readable, understandable and maintainable.