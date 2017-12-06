# 1. Machine Learning Foundations: A Case Study Approach

# 1.1 Linear Regression

* Use polynomial features to create non-linear function

# 1.2 Confusion Matrices

* Can be used to weight false/true positive/negative

## 1.3 Word count representation for measuring similarity

* Bag of words

### 1.3.1 Measuring similarity

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

### 1.3.2 Prioritizing important words with tf-idf

A document about sports might have some common words, such as: "the", "player", "field", "goal"
But it might also have rare words which are important "describers" of the article, for instance: "futbol", "Messi".

Solution: Emphasize words appearing in few docs. Equivalently, discount word W based on number of documents containing word W
