# 📊 Descriptive Statistics – Complete Guide for AI/ML

> *Everything you need to know about summarising, visualising, and interpreting data – from basics to real‑world applications.*

---

## 📚 Table of Contents

1. [What is Descriptive Statistics?](#what-is-descriptive-statistics)
2. [Measures of Central Tendency](#measures-of-central-tendency)
   - Mean
   - Median
   - Mode
   - Which One to Use When?
3. [Measures of Dispersion (Spread)](#measures-of-dispersion-spread)
   - Range
   - Variance
   - Standard Deviation
   - Interquartile Range (IQR)
   - Population vs. Sample – Why `n‑1`?
4. [Percentiles and Quartiles](#percentiles-and-quartiles)
5. [The Five‑Number Summary and Box Plots](#the-fivenumber-summary-and-box-plots)
   - Outlier Detection
6. [Histograms and Skewness](#histograms-and-skewness)
   - Left‑Skewed, Right‑Skewed, Symmetric
   - Relationship between Mean, Median, and Mode
7. [Covariance and Correlation](#covariance-and-correlation)
   - Covariance
   - Pearson Correlation Coefficient
8. [Why These Concepts Matter in AI/ML](#why-these-concepts-matter-in-aiml)
9. [Summary Quick Reference](#summary-quick-reference)

---

## What is Descriptive Statistics?

**Descriptive statistics** summarises and organises data so that we can understand its main features. It does **not** make predictions – it simply describes what the data says.

We use descriptive statistics to:

- **Understand the centre** (where most values lie).
- **Understand the spread** (how much values vary).
- **Visualise patterns** (shape, outliers, relationships).

In AI/ML, descriptive statistics is the **first step** before building any model – it helps us decide which algorithms might work, what preprocessing is needed, and how to interpret results.

---

## Measures of Central Tendency

Central tendency tells us the **typical** or **middle** value of a dataset.

### 1. Mean (Arithmetic Average)

The **mean** is the sum of all values divided by the number of values.

**Formula** (for a sample):
$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$

**Example**:  
Heights (cm): `155, 160, 165, 170, 175, 180`

$$
\text{Mean} = \frac{155+160+165+170+175+180}{6} = \frac{1005}{6} = 167.5 \text{ cm}
$$

**When to use**:  
- Data is **symmetric** (bell‑shaped) and has **no outliers**.
- We need a single value that represents the entire dataset mathematically – e.g., for further calculations like variance.

---

### 2. Median (Middle Value)

The **median** is the middle value when data is sorted in ascending order.

- If the number of observations **`n` is odd**, the median is the middle value.
- If **`n` is even**, the median is the average of the two middle values.

**Example**:  
Sorted data: `1, 2, 3, 4, 5, 6` → two middle are `3` and `4` → median = `(3+4)/2 = 3.5`.

**Example with outlier**:  
Heights: `155, 160, 165, 170, 175, 300` → mean = (155+160+165+170+175+300)/6 = 187.5 – heavily influenced by the outlier.  
Sorted: `155, 160, 165, 170, 175, 300` → median = `(165+170)/2 = 167.5` – more representative.

**When to use**:  
- Data is **skewed** or contains **outliers**.
- We want a robust measure of centre.

---

### 3. Mode (Most Frequent Value)

The **mode** is the value that appears most often. A dataset can have one mode (unimodal), two modes (bimodal), or more.

**Example**:  
`2, 4, 4, 6, 7, 7, 7, 9` → mode = `7` (appears 3 times).

**Bimodal example**:  
`3, 5, 5, 6, 6, 8` → modes = `5` and `6`.

**When to use**:  
- **Categorical data** (e.g., favourite colour, most common product).
- To find the most frequent category in any scale (nominal, ordinal, interval, ratio).

---

### 📌 Which Measure to Use When?

| Situation | Best Measure |
|-----------|--------------|
| Symmetric distribution, no outliers | Mean |
| Skewed data or with outliers | Median |
| Categorical data or finding the most common category | Mode |

---

## Measures of Dispersion (Spread)

Dispersion tells us **how spread out** the data is – whether values cluster tightly around the centre or are widely scattered.

### 1. Range

The **range** is the difference between the maximum and minimum values.

$$
\text{Range} = \text{Max} - \text{Min}
$$

**Example**:  
Ages: `14, 13, 10, 20, 28, 75, 15` → range = `75 - 10 = 65`.

**Pros**: Very easy to compute.  
**Cons**: Extremely sensitive to outliers; gives no information about the distribution between min and max.

---

### 2. Variance

The **variance** measures the average of the squared deviations from the mean. It quantifies how far each value is from the mean, on average.

**Population variance** (when we have all data):
$$
\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}
$$
where $\mu$ is the population mean, $N$ is population size.

**Sample variance** (when we have a sample):
$$
s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}
$$

**Why `n‑1`?** – This is called **Bessel’s correction**. It corrects the bias in the sample variance estimate – using `n` would systematically underestimate the population variance. So we divide by `n‑1` to get an unbiased estimate.

**Example**: Petal lengths (cm): `5, 8, 12, 15, 20`  
Sample mean $\bar{x} = (5+8+12+15+20)/5 = 12$.

| $x_i$ | $(x_i - \bar{x})$ | $(x_i - \bar{x})^2$ |
|-------|-------------------|---------------------|
| 5     | -7                | 49                  |
| 8     | -4                | 16                  |
| 12    | 0                 | 0                   |
| 15    | 3                 | 9                   |
| 20    | 8                 | 64                  |
| Sum   |                   | 138                 |

Sample variance $s^2 = 138 / (5-1) = 138/4 = 34.5$.

**Interpretation**: The variance is in **squared units** (cm²), which makes it hard to interpret directly.

---

### 3. Standard Deviation

The **standard deviation** is the square root of the variance. It brings the units back to the original scale.

**Population standard deviation**: $\sigma = \sqrt{\sigma^2}$  
**Sample standard deviation**: $s = \sqrt{s^2}$

From the above example: $s = \sqrt{34.5} \approx 5.87$ cm.

**Interpretation**: On average, each petal length is about 5.87 cm away from the mean of 12 cm.

**Characteristics**:
- **Same units** as the data – easy to understand.
- Sensitive to outliers (like variance).
- The most commonly used measure of spread.

---

### 4. Interquartile Range (IQR)

The IQR is the range of the **middle 50%** of the data. It is the difference between the third quartile (Q3) and the first quartile (Q1).

$$
\text{IQR} = Q3 - Q1
$$

IQR is **robust to outliers** because it ignores the extreme 25% on each side.

We’ll learn how to find Q1 and Q3 in the next section.

---

### Population vs. Sample – Why Does It Matter?

- When we have the **entire population**, we use $\sigma^2$ and divide by $N$.
- When we have a **sample**, we use $s^2$ and divide by $n-1$ to get an **unbiased estimate** of the population variance.

In real‑world AI/ML, we almost always work with samples, so we use $n-1$ and $s^2$.

---

## Percentiles and Quartiles

**Percentiles** divide the data into 100 equal parts. The **k‑th percentile** is the value below which k% of the data falls.

**Quartiles** divide the data into four equal parts:

- **Q1 (First Quartile)**: 25th percentile – lower 25% of data.
- **Q2 (Second Quartile)**: 50th percentile – same as the median.
- **Q3 (Third Quartile)**: 75th percentile – upper 25% of data.

**How to find quartiles** (one common method):

1. Sort the data.
2. Find the median – that is Q2.
3. The median of the lower half (excluding Q2 if n is odd) is Q1.
4. The median of the upper half is Q3.

**Example**: Data: `1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 9, 9`  
Sorted (already).

- n = 19 (odd). Median (Q2) is the 10th value = `5`.
- Lower half (first 9): `1, 2, 2, 2, 3, 3, 4, 5, 5` → median (Q1) = 5th value = `3`.
- Upper half (last 9): `5, 6, 6, 6, 6, 7, 8, 8, 9` → median (Q3) = 5th value = `6`.

Wait – that gives Q1=3, Q3=6. But the PDF gave Q1=3, Q3=7. There might be slight differences in method. We’ll follow the standard method:  
For Q1, find the position = 0.25*(n+1) = 0.25*20 = 5 → 5th value = 3.  
For Q3, position = 0.75*(n+1) = 0.75*20 = 15 → 15th value = 7. So Q1=3, Q3=7. That matches the PDF.  

Thus **IQR = Q3 - Q1 = 7 - 3 = 4**.

---

## The Five‑Number Summary and Box Plots

The **five‑number summary** consists of:

1. **Minimum**
2. **Q1** (First Quartile)
3. **Median** (Q2)
4. **Q3** (Third Quartile)
5. **Maximum**

For our example: `1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 9, 9`

- Minimum = 1
- Q1 = 3
- Median = 5
- Q3 = 7
- Maximum = 9

### 🧮 Outlier Detection Using IQR

We can detect outliers with the **IQR method**:

- **Lower fence** = Q1 - 1.5 × IQR
- **Upper fence** = Q3 + 1.5 × IQR

Any point **outside** these fences is considered a potential outlier.

For our data:  
Lower fence = 3 - 1.5×4 = 3 - 6 = **-3**  
Upper fence = 7 + 1.5×4 = 7 + 6 = **13**

Since all values are between 1 and 9, there are no outliers.

---

### Box Plot (Box‑and‑Whisker Plot)

A box plot visually shows the five‑number summary:

```
        ┌─────┐
        │     │
    ────┼─┐ ┌─┼────
        │ │ │ │
        └─┴─┴─┘
        Min Q1 Med Q3 Max
```

- The box spans Q1 to Q3.
- The line inside is the median.
- Whiskers extend to the minimum and maximum (or to fences, depending on implementation).
- Points beyond whiskers are plotted as dots (outliers).

---

## Histograms and Skewness

A **histogram** groups data into bins and shows the frequency (count) in each bin. It helps us visualise the **shape** of the distribution.

### Skewness

Skewness describes the **asymmetry** of the distribution.

#### 1. Right‑Skewed (Positive Skew)
- The right tail is longer.
- **Mean > Median > Mode**
- Example: income distribution (a few very rich people pull the mean to the right).
- Box plot: the right whisker is longer than the left.

#### 2. Left‑Skewed (Negative Skew)
- The left tail is longer.
- **Mean < Median < Mode**
- Example: exam scores when most students do well (mean pulled down by a few low scores).
- Box plot: left whisker longer.

#### 3. Symmetric
- Mean ≈ Median ≈ Mode.
- Bell‑shaped (normal distribution).

---

## Covariance and Correlation

These measure the **relationship** between two variables.

### Covariance

**Covariance** indicates whether two variables move together (positive) or in opposite directions (negative).

**Sample covariance**:
$$
\text{Cov}(x,y) = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{n-1}
$$

**Example**:  
Students: hours studied (x) and exam scores (y).

| Student | x (hours) | y (score) |
|---------|-----------|-----------|
| 1       | 2         | 50        |
| 2       | 3         | 60        |
| 3       | 4         | 70        |
| 4       | 5         | 80        |
| 5       | 6         | 90        |

$\bar{x} = 4$, $\bar{y} = 70$.

Compute $(x_i - \bar{x})(y_i - \bar{y})$:

| x | y | (x-4) | (y-70) | product |
|---|---|-------|--------|---------|
| 2 | 50| -2    | -20    | 40      |
| 3 | 60| -1    | -10    | 10      |
| 4 | 70| 0     | 0      | 0       |
| 5 | 80| 1     | 10     | 10      |
| 6 | 90| 2     | 20     | 40      |
| Sum product = 40+10+0+10+40 = 100.  

Covariance = 100 / (5-1) = **25**.

**Interpretation**: Positive covariance – as study hours increase, exam scores tend to increase.

**Limitation**: Covariance depends on the units (e.g., if we change hours to minutes, covariance changes), so it’s hard to compare across datasets.

---

### Pearson Correlation Coefficient ($r$)

The **correlation coefficient** standardises covariance by the standard deviations of both variables. It is **unit‑free** and ranges from **-1 to +1**.

$$
r = \frac{\text{Cov}(x,y)}{s_x \cdot s_y}
$$

- $r = +1$: perfect positive linear relationship.
- $r = -1$: perfect negative linear relationship.
- $r = 0$: no linear relationship (but could have non‑linear).

**From the example**:  
We have $s_x = \sqrt{\frac{(2-4)^2+(3-4)^2+(4-4)^2+(5-4)^2+(6-4)^2}{5-1}} = \sqrt{\frac{4+1+0+1+4}{4}} = \sqrt{2.5} \approx 1.58$.  
$s_y = \sqrt{\frac{(50-70)^2+(60-70)^2+(70-70)^2+(80-70)^2+(90-70)^2}{4}} = \sqrt{\frac{400+100+0+100+400}{4}} = \sqrt{250} \approx 15.81$.  

So $r = 25 / (1.58 \times 15.81) \approx 25 / 24.98 \approx 1.00$ – almost perfect positive correlation.

**Interpretation**: $r$ close to 1 means hours studied and exam score are strongly positively linearly related.

**Why use correlation?**  
- It’s standardised – you can compare correlations between different pairs of variables.
- Used in **feature selection** – we want to remove highly correlated features to avoid multicollinearity.

---

## Why These Concepts Matter in AI/ML

- **Mean/Median/Mode** – used to fill missing values (imputation).
- **Variance/Standard Deviation** – feature scaling (e.g., standardisation: $z = \frac{x - \mu}{\sigma}$).
- **IQR** – outlier detection and removal.
- **Skewness** – decide whether to apply transformations (log, square root) to make data more normal.
- **Correlation** – feature selection, understanding relationships between input and target.
- **Histograms/Box plots** – exploratory data analysis (EDA) to understand data distribution before modeling.

---

## Summary Quick Reference

| Concept | Formula / How‑to | Use Case |
|---------|------------------|----------|
| **Mean** | $\frac{\sum x}{n}$ | Symmetric data, no outliers |
| **Median** | Middle value | Skewed data, outliers |
| **Mode** | Most frequent value | Categorical data |
| **Range** | Max - Min | Quick rough spread |
| **Variance (sample)** | $s^2 = \frac{\sum (x-\bar{x})^2}{n-1}$ | Measure of variability (squared units) |
| **Standard deviation (sample)** | $s = \sqrt{s^2}$ | Spread in original units |
| **IQR** | Q3 - Q1 | Robust spread, outlier detection |
| **Five‑number summary** | Min, Q1, Median, Q3, Max | Box plot |
| **Skewness** | Right: Mean>Median>Mode; Left: Mean<Median<Mode | Distribution shape |
| **Covariance** | $\frac{\sum (x-\bar{x})(y-\bar{y})}{n-1}$ | Direction of linear relationship (unscaled) |
| **Correlation $r$** | $\frac{\text{Cov}(x,y)}{s_x s_y}$ | Strength and direction of linear relationship (-1 to +1) |

---

## Final Words

Descriptive statistics is the **foundation** of data analysis. Mastering these concepts will help you:

- Understand your data better.
- Preprocess data correctly.
- Choose appropriate machine learning models.
- Interpret results meaningfully.

Practice with real datasets – try calculating these measures by hand and with Python/Pandas. The more you practice, the more intuitive they become.

---

*Happy learning! 🚀*