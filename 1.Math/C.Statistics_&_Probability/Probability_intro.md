# 🎲 Probability Essentials – Addition & Multiplication Rules

> *Your friendly guide to understanding when to add and when to multiply probabilities, with real‑world examples and AI/ML applications.*

---

## 📚 Table of Contents

1. [What is Probability?](#what-is-probability)
2. [Key Terminology](#key-terminology)
3. [The Addition Rule](#the-addition-rule)
   - For Mutually Exclusive Events
   - For Non‑Mutually Exclusive Events
   - Worked Examples
4. [The Multiplication Rule](#the-multiplication-rule)
   - For Independent Events
   - For Dependent Events (Conditional Probability)
   - Worked Examples
5. [When to Add vs. When to Multiply](#when-to-add-vs-when-to-multiply)
6. [Real‑World Applications in AI/ML](#realworld-applications-in-aiml)
7. [Practice Problems with Solutions](#practice-problems-with-solutions)
8. [Quick Reference Cheat Sheet](#quick-reference-cheat-sheet)

---

## What is Probability?

**Probability** measures the likelihood that an event will occur. It is expressed as a number between **0** (impossible) and **1** (certain). For example:

- Tossing a fair coin → \( P(\text{Heads}) = \frac{1}{2} = 0.5 \)
- Rolling a fair die → \( P(\text{rolling a 3}) = \frac{1}{6} \approx 0.1667 \)

In data science, probability is the backbone of **statistical inference**, **machine learning** (e.g., Naïve Bayes, logistic regression), and **decision‑making under uncertainty**.

---

## Key Terminology

| Term | Meaning | Example |
|------|---------|---------|
| **Experiment** | Any process that produces an outcome | Tossing a coin, rolling a die |
| **Outcome** | A single result of an experiment | Head, Tail; 1, 2, 3, 4, 5, 6 |
| **Sample Space** | The set of all possible outcomes | {H, T} or {1,2,3,4,5,6} |
| **Event** | A subset of the sample space | Event of getting an even number: {2,4,6} |
| **Mutually Exclusive** | Two events that cannot happen at the same time | Getting Heads and Tails in a single toss |
| **Independent** | Occurrence of one event does not affect the other | Two separate coin tosses |
| **Dependent** | Occurrence of one event affects the probability of the other | Drawing cards without replacement |

---

## The Addition Rule

The addition rule helps us find the probability that **either** event A **or** event B (or both) occurs.

### 🟢 Mutually Exclusive Events

If two events **cannot** occur simultaneously, they are mutually exclusive. For such events:

**Formula**:
$$
P(A \text{ or } B) = P(A) + P(B)
$$

**Example** – Tossing a coin:
- Event A = Heads, Event B = Tails.
- They are mutually exclusive – you cannot get both on the same toss.
- \( P(\text{Heads or Tails}) = P(H) + P(T) = \frac{1}{2} + \frac{1}{2} = 1 \). (It’s certain you’ll get one of them.)

**Example** – Rolling a die:
- Event A = rolling a 1, Event B = rolling a 5.
- They are mutually exclusive.
- \( P(1 \text{ or } 5) = P(1) + P(5) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3} \).

---

### 🟡 Non‑Mutually Exclusive Events

If two events **can** occur at the same time, they are not mutually exclusive. In that case, we must **subtract** the overlap to avoid double‑counting.

**Formula**:
$$
P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)
$$

**Example** – Drawing a card from a standard deck of 52 cards:
- Event A = drawing a King.
- Event B = drawing a Heart.
- These are **not** mutually exclusive because there is a card that is both a King and a Heart – the King of Hearts.
- \( P(K) = \frac{4}{52} \), \( P(\text{Heart}) = \frac{13}{52} \), \( P(K \text{ and Heart}) = \frac{1}{52} \).
- So:
  $$
  P(K \text{ or Heart}) = \frac{4}{52} + \frac{13}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13}
  $$

---

## The Multiplication Rule

The multiplication rule helps us find the probability that **both** event A **and** event B occur.

### 🔵 Independent Events

Two events are independent if the occurrence of one does **not** affect the probability of the other.

**Formula**:
$$
P(A \text{ and } B) = P(A) \times P(B)
$$

**Example** – Tossing a coin twice:
- Event A = Heads on first toss, Event B = Tails on second toss.
- The tosses are independent.
- \( P(H \text{ and } T) = P(H) \times P(T) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4} \).

**Example** – Rolling two dice:
- Event A = rolling a 1 on the first die, Event B = rolling a 2 on the second die.
- \( P(1 \text{ and } 2) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36} \).

---

### 🔴 Dependent Events (Conditional Probability)

Two events are dependent if the outcome of one affects the probability of the other. For dependent events, we use **conditional probability**.

**Formula**:
$$
P(A \text{ and } B) = P(A) \times P(B \mid A)
$$
where \( P(B \mid A) \) is the probability of B **given that** A has already occurred.

**Example** – Drawing two cards **without replacement**:
- Event A = first card is a King.
- Event B = second card is a Queen.
- After drawing a King, there are now 51 cards left, and still 4 Queens.
- \( P(K \text{ first}) = \frac{4}{52} \).
- \( P(Q \mid K) = \frac{4}{51} \).
- So:
  $$
  P(K \text{ and then } Q) = \frac{4}{52} \times \frac{4}{51} = \frac{16}{2652} \approx 0.00603
  $$

**Example** – Drawing two Kings **without replacement**:
- First King: \( \frac{4}{52} \).
- Second King (given first was King): now only 3 Kings left out of 51 cards → \( \frac{3}{51} \).
- So:
  $$
  P(\text{two Kings}) = \frac{4}{52} \times \frac{3}{51} = \frac{12}{2652} = \frac{1}{221}
  $$

---

## When to Add vs. When to Multiply

| Situation | Rule |
|-----------|------|
| **“OR”** – at least one of the events occurs | Use **Addition Rule** |
| Events are mutually exclusive → add without subtraction | \( P(A \cup B) = P(A) + P(B) \) |
| Events are not mutually exclusive → add and subtract intersection | \( P(A \cup B) = P(A) + P(B) - P(A \cap B) \) |
| **“AND”** – both events occur | Use **Multiplication Rule** |
| Events are independent → multiply | \( P(A \cap B) = P(A) \times P(B) \) |
| Events are dependent → multiply with conditional | \( P(A \cap B) = P(A) \times P(B \mid A) \) |

---

## Real‑World Applications in AI/ML

- **Naïve Bayes Classifier**: Relies on conditional probability and the multiplication rule (assuming features are independent). Used in spam detection, sentiment analysis.
- **Logistic Regression**: Estimates probability of binary outcomes using the **sigmoid function** – a probability model.
- **Recommender Systems**: Use probabilities to predict user preferences (e.g., “people who bought X also bought Y”).
- **Uncertainty Quantification**: In decision‑making, we often compute probabilities of various outcomes (e.g., risk assessment).
- **Bayesian Inference**: Updates probabilities as new data arrives – heavily uses conditional probability and the multiplication rule.

---

## Practice Problems with Solutions

### Problem 1
A fair die is rolled. What is the probability of getting a number **greater than 4** **or** an **odd number**?

**Solution**:  
Sample space: {1,2,3,4,5,6}  
Event A = {5,6} (greater than 4) – \( P(A) = 2/6 = 1/3 \)  
Event B = {1,3,5} (odd) – \( P(B) = 3/6 = 1/2 \)  
Intersection A ∩ B = {5} – \( P(A \cap B) = 1/6 \)  
Since they are **not mutually exclusive**, use addition rule:  
\( P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{1}{3} + \frac{1}{2} - \frac{1}{6} = \frac{2}{6} + \frac{3}{6} - \frac{1}{6} = \frac{4}{6} = \frac{2}{3} \).

### Problem 2
A bag contains 3 red marbles and 5 blue marbles. Two marbles are drawn **without replacement**. What is the probability that both are red?

**Solution**:  
\( P(\text{first red}) = \frac{3}{8} \)  
After one red is taken, there are 2 red left out of 7 marbles.  
\( P(\text{second red} \mid \text{first red}) = \frac{2}{7} \)  
So \( P(\text{both red}) = \frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \frac{3}{28} \).

### Problem 3
A coin is flipped and a die is rolled. What is the probability of getting **Heads** and **rolling a number less than 3**?

**Solution**:  
Events are independent.  
\( P(H) = 1/2 \), \( P(\text{number < 3}) = P(1 \text{ or } 2) = 2/6 = 1/3 \)  
\( P(H \text{ and } <3) = \frac{1}{2} \times \frac{1}{3} = \frac{1}{6} \).

---

## Quick Reference Cheat Sheet

```
Mutually Exclusive (cannot both occur):
  P(A or B) = P(A) + P(B)

Non-Mutually Exclusive (can both occur):
  P(A or B) = P(A) + P(B) - P(A and B)

Independent (A does not affect B):
  P(A and B) = P(A) × P(B)

Dependent (A affects B):
  P(A and B) = P(A) × P(B | A)
```

---

## Final Words

Probability rules are the **building blocks** for more advanced topics like Bayes’ theorem, random variables, and statistical inference. Mastering when to add and when to multiply will save you countless mistakes and give you a solid foundation for data science and machine learning.

> 🧠 **Remember**:  
> - **OR** → add (but watch for overlap).  
> - **AND** → multiply (but adjust if events are not independent).

Practice with different scenarios, and soon these rules will become second nature!

---

*Happy learning! 🚀*