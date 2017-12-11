# 1. Machine Learning Foundations: A Case Study Approach

## 1.1 Linear Regression

* Use polynomial features to create non-linear function

## 1.2 Confusion Matrices

* Can be used to weight false/true positive/negative

### 1.3 Word count representation for measuring similarity

* Bag of words

#### 1.3.1 Measuring similarity

<p align="center">
  <img src="https://i.imgur.com/mhdAUqH.png" />
</p>

Similarity = 13

<p align="center">
  <img src="https://i.imgur.com/F1mquSL.png" />
</p>

Same documents, concatenated. Similarity = 52. That's bad (bias for long documents)

Solution: Normalize vectors

<p align="center">
  <img src="https://i.imgur.com/KBarfgg.png" />
</p>

#### 1.3.2 Prioritizing important words with tf-idf

A document about sports might have some common words, such as: "the", "player", "field", "goal"
But it might also have rare words which are important "describers" of the article, for instance: "futbol", "Messi".

Solution: Emphasize words appearing in few docs. Equivalently, discount word W based on number of documents containing word W

Important words:

Appears frequently in document -> Common locally

Appears rarely in corpus -> Rare globally

#### 1.3.3 Calculating tf-idf vectors (Term frequency - inverse document frequency)

Term frequency vector in downweighted based on inverse document frequency

* Inverse document frequency (globally)

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\large&space;log(\frac{docs}{1&space;&plus;&space;docs\_using\_word})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\large&space;log(\frac{docs}{1&space;&plus;&space;docs\_using\_word})" title="\large log(\frac{docs}{1 + docs\_using\_word})" /></a>
</p>

<p align="center">
  <img src="https://i.imgur.com/AOP3T8C.png" />
</p>

#### 1.3.4 Retrieving similar documents using nearest neighbor search

* Distance metric

#### 1.3.5 k-means: A clustering algorithm

0. Initialize cluster centers
1. Assign observations to closest cluster center
2. Revise cluster centers as mean of assigned observations

## 1.3 Recommender Systems

* Recommend Products
* Recommend Friends
* Drug repurposing

### 1.3.1 Co-occurrence matrix

<p align="center">
  <img src="https://i.imgur.com/uooUkyY.png" />
</p>

### 1.3.2 Making recommendations using co-occurences 

User someone purchased "diapers".

1. Look at "diapers" row of matrix
2. Recommend other items with largest counts
