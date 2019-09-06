+++ 
draft = false

title = "Example post"
description = "Hey"

tags = []
categories = []
series = []
hideReadingTime = false

katex = "false"
date = 2019-09-05T13:27:24-04:00
+++

{{< notebook "Week1_Class_Exercises_Solutions_Final.ipynb" >}}

<!-- Notebook Start -->


# Week 1 Exercises

Today we will explore gender bias in natural language processing. We will learn about our first models to probe gender bias in word vectors. As a reminder, word vectors are a machine's representation of a word, learned from reading a large corpus of text to understand the context that words are used in. For example, since the words "good" and "great" are used in similar contexts, they have similar word vectors!

These kinds of word vectors are used in everything from Google Search to Spotify recommendations, so if they are biased, this is a major problem.

Today we will be using GloVe vectors, which are a standard type of word vector used in a variety of real-world applications. These word vectors were trained on 6 billion word tokens, sourced from Wikipedia 2014 + Gigaword5. If you're interested you can find more information [here](https://nlp.stanford.edu/projects/glove/).

Run the below cell by highlighting it and typing Shift+Enter. This will import the required packages and download the GloVe vectors, which will take a few minutes.


```python
import torchtext.vocab as vocab
import numpy as np
np.random.seed(42)

VEC_SIZE = 300
glove = vocab.GloVe(name='6B', dim=VEC_SIZE)
```

    .vector_cache/glove.6B.zip: 862MB [03:05, 4.65MB/s]                           
    100%|█████████▉| 399433/400000 [00:44<00:00, 8886.22it/s]

## Part 1
Below we have included a short helper function that retrieves the word vector for a given word.


```python
def get_word_vector(word):
    return glove.vectors[glove.stoi[word]].numpy()
```

Observe the results of this helper function below. Notice that we are outputting a numpy array of dimensionality (300,). This means that the output is a 300-dimensional vector.


```python
good = get_word_vector('good') # get the word vector for 'good'
print(good.shape)
```

    (300,)


Below, use the above vector and the word vector for 'great' to determine the cosine similarity between 'good' and 'great'. Do the same for 'good' and 'human' (two words that are less similar). You'll need *np.linalg.norm* and *np.dot*.


```python
great = get_word_vector('great') # YOUR CODE HERE
human = get_word_vector('human') # YOUR CODE HERE
def compute_cosine_similarity(a, b):
    # YOUR CODE HERE:
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    # END CODE

print("Good-great similarity %f" % compute_cosine_similarity(good, great))
print("Good-human similarity %f" % compute_cosine_similarity(good, human))
```

    Good-great similarity 0.641005
    Good-human similarity 0.313640


**Expected output:**

Good-great similarity 0.641005

Good-human similarity 0.313640

Now, use our helper function to retrieve the "gender vector", or the vector representing 'woman' minus the vector representing 'man' (woman - man). 


```python
# YOUR CODE HERE
man = get_word_vector('man')
woman = get_word_vector('woman')
gender_vector = woman - man
# END CODE
print('First value of gender vector: %f ' % gender_vector[0])
print('Shape of gender vector: ', gender_vector.shape)
```

    First value of gender vector: -0.220370 
    Shape of gender vector:  (300,)


**Expected output:**

First value of gender vector: -0.220370 

Shape of gender vector:  (300,)

Now fill in the below function that computes linear regression on any word. Use the gender_vector to provide weights (*w*), and do not use a bias term (*b*). You'll need our helper function *get_word_vector* and *np.dot*.


```python
def compute_linear_regression(word):
    # YOUR CODE HERE
    word_vector = get_word_vector(word)
    return np.dot(gender_vector, word_vector)
    # END CODE
```

Check to make sure your model matches the expected output for 'programmer':


```python
compute_linear_regression('programmer')
```




    -1.0347012



**Expected output:**
-1.0347012

Feel free to play around with the model by changing the input word in the below cell! How does the score for 'programmer' compare to the score for 'nurse'? For 'homemaker'? What does this tell us about our word vectors?


```python
compute_linear_regression('nurse')
```




    8.855267



## Part 2

Now we will build a more sophisticated logistic regression model to make predictions on our word vectors. Eventually, this model will actually learn the weights (*w*) and bias (*b*) by itself! It will also output a probability between 0 and 1 that a word is associated with females. (1 represents a word that is very 'female' according to our word vectors, 0 represents a word that is not) 

All we will do is tell this model that 1 represents female and 0 represents male, and, alarmingly, bias from our word vectors will transfer to our model.

For these in-class exercises, you will build this model and learn how to train it. For homework, you will actually train it and see the results.

As a warmup, fill in the below function to calculate the sigmoid of a scalar value. Use *np.exp* instead of python's built-in.


```python
def sigmoid(z):
    # YOUR CODE HERE
    return 1.0 / (1 + np.exp(-z))
    # END CODE
print("sigmoid(0.5) is %f" % sigmoid(0.5))
```

    sigmoid(0.5) is 0.622459


**Expected output:**

sigmoid(0.5) is 0.622459

Next, fill in the below function to compute logistic regression on a word given weights and bias. Note that you are not training the model yet, just computing what is known as the "forward pass". This should look similar to your *compute_linear_regression* function, but you are using the weights and bias given instead of the *gender_vector*, and you are using sigmoid to produce the final output.


```python
def compute_logistic_regression(word, weights, bias):
    # YOUR CODE HERE
    word_vector = get_word_vector(word)
    return sigmoid(np.dot(weights, word_vector) + bias)
    # END CODE

np.random.seed(42)
rand_weights = np.random.randn(VEC_SIZE)
rand_bias = np.random.rand()
print("Predicted output: %f" % compute_logistic_regression('hello', rand_weights, rand_bias))
```

    Predicted output: 0.000089


**Expected output:**

Predicted output: 0.000089

Don't read too much into this output, it was randomly generated. 



Congratulations on completing the first set of class exercises!

For homework, we will use the functions you just wrote to show that bias transfers from the word vectors to models trained on them.


```python

```
<!-- Notebook End -->








