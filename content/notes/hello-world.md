+++ 
draft = true
date = 2019-08-05T22:52:06-04:00
title = "hi"
description = "hi"
tags = ["hello", "notebook"]
categories = ["notebook", "hi"]
externalLink = ""
series = []
katex = "true"
hideReadingTime = true
+++

## Style Demo

# h1 Heading
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading


---

**This is bold text**

__This is bold text__

*This is italic text*

_This is italic text_

~~Deleted text~~

This is text with inline math $\sum_{n=1}^{\infty} 2^{-n} = 1$ and with math blocks:

$$
\sum_{n=1}^{\infty} 2^{-n} = 1
$$

| Heading | Another heading |
| :----:  | :-------------: |
|  text   |      text       |
|  text   |      text       |
|  text   |      text       |

> Block quotes are
> written like so.
>
> They can span multiple paragraphs,
> if you like.

Some text, and some `code` and then a nice plain [link with title](https://github.com/davidhampgonsalves/davidhampgonsalves.com-hugo "title text!").

and then

+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
+ Very easy!

vs.

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa

## Code

Inline `code`

``` js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
```

## Hugo shortcode for figure

{{< figure src="/images/N90.jpg" caption="N90 nebula, \"New stars shed light on the past\" by ESA/Hubble" >}}

Enable katex by adding `katex = "true"` to the [front matter](https://gohugo.io/content-management/front-matter/)  

```toml
+++
katex = "true"
+++
```

It's almost a dropin alternative to the mathjax solution, you should just choose one of them.  

Inline math looks like this  

```tex
This is text with inline math $\sum_{n=1}^{\infty} 2^{-n} = 1$
```

This is text with inline math $\sum_{n=1}^{\infty} 2^{-n} = 1$  
and with math blocks:  


```tex
$$
\sum_{n=1}^{\infty} 2^{-n} = 1
$$
```

$$
\sum_{n=1}^{\infty} 2^{-n} = 1
$$

```html
<html>
<p>hi</p>
</html>

```
{{< highlight html >}}
<section id="main">
  <div>
   <h1 id="title">{{ .Title }}</h1>
    {{ range .Pages }}
        {{ .Render "summary"}}
    {{ end }}
  </div>
</section>
{{< /highlight >}}

{{< gist spf13 7896402 >}}

## More Text

Pause to consider proposition #3. Typography is visual, so it’s easy to conclude that it’s primarily an artistic or aesthetic pursuit. Not so. Typography is primarily utilitarian. "Hello"

#### More Text

Therefore, good typography is measured on a utilitarian yardstick. Typography that is aesthetically pleasant, but that doesn’t reinforce the meaning of the text, is a failure. Typography that reinforces the meaning of the text, even if aesthetically unpleasant, is a success.

### More Text

Does that mean that effective typography can be ugly? Sure. Sometimes ugly is better than pretty. "Hello"

Pause to consider proposition #3. Typography is visual, so it’s easy to conclude that it’s primarily an artistic or aesthetic pursuit. Not so. Typography is primarily utilitarian.

Therefore, good typography is measured on a utilitarian yardstick. Typography that is aesthetically pleasant, but that doesn’t reinforce the meaning of the text, is a failure. Typography that reinforces the meaning of the text, even if aesthetically unpleasant, is a success.

Does that mean that effective typography can be ugly? Sure. Sometimes ugly is better than pretty.

Pause to consider proposition #3. Typography is visual, so it’s easy to conclude that it’s primarily an artistic or aesthetic pursuit. Not so. Typography is primarily utilitarian.

Therefore, good typography is measured on a utilitarian yardstick. Typography that is aesthetically pleasant, but that doesn’t reinforce the meaning of the text, is a failure. Typography that reinforces the meaning of the text, even if aesthetically unpleasant, is a success.

Does that mean that effective typography can be ugly? Sure. Sometimes ugly is better than pretty.

Pause to consider proposition #3. Typography is visual, so it’s easy to conclude that it’s primarily an artistic or aesthetic pursuit. Not so. Typography is primarily utilitarian.

Therefore, good typography is measured on a utilitarian yardstick. Typography that is aesthetically pleasant, but that doesn’t reinforce the meaning of the text, is a failure. Typography that reinforces the meaning of the text, even if aesthetically unpleasant, is a success.

Does that mean that effective typography can be ugly? Sure. Sometimes ugly is better than pretty.

What he said reminded me of a folk tale about an old woman and her rooster. Every morning, the rooster crows and the sun rises immediately after. One day, after a fight with the villagers, she decides to teach said villagers a lesson and kills her rooster. In her mind, she has punished the village by plunging it into eternal darkness, but the run rises as usual, leaving her red-faced and a good rooster short. The moral of this story is made out to be the perils of arrogance but I think the tale is additionally a warning against superstition.



# Hi


# Week 1 Exercises

Today we will explore gender bias in natural language processing. We will learn about our first models to probe gender bias in word vectors. As a reminder, word vectors are a machine's representation of a word, learned from reading a large corpus of text to understand the context that words are used in. For example, since the words "good" and "great" are used in similar contexts, they have similar word vectors!

These kinds of word vectors are used in everything from Google Search to Spotify recommendations, so if they are biased, this is a major problem.

Today we will be using GloVe vectors, which are a standard type of word vector used in a variety of real-world applications. These word vectors were trained on 6 billion word tokens, sourced from Wikipedia 2014 + Gigaword5. If you're interested you can find more information [here](https://nlp.stanford.edu/projects/glove/).

Run the below cell by highlighting it and typing Shift+Enter. This will import the required packages and download the GloVe vectors, which will take a few minutes.


```
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


```
def get_word_vector(word):
    return glove.vectors[glove.stoi[word]].numpy()
```

Observe the results of this helper function below. Notice that we are outputting a numpy array of dimensionality (300,). This means that the output is a 300-dimensional vector.


```
good = get_word_vector('good') # get the word vector for 'good'
print(good.shape)
```

    (300,)


Below, use the above vector and the word vector for 'great' to determine the cosine similarity between 'good' and 'great'. Do the same for 'good' and 'human' (two words that are less similar). You'll need *np.linalg.norm* and *np.dot*.


```
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


```
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


```
def compute_linear_regression(word):
    # YOUR CODE HERE
    word_vector = get_word_vector(word)
    return np.dot(gender_vector, word_vector)
    # END CODE
```

Check to make sure your model matches the expected output for 'programmer':


```
compute_linear_regression('programmer')
```




    -1.0347012



**Expected output:**
-1.0347012

Feel free to play around with the model by changing the input word in the below cell! How does the score for 'programmer' compare to the score for 'nurse'? For 'homemaker'? What does this tell us about our word vectors?


```
compute_linear_regression('nurse')
```




    8.855267



## Part 2

Now we will build a more sophisticated logistic regression model to make predictions on our word vectors. Eventually, this model will actually learn the weights (*w*) and bias (*b*) by itself! It will also output a probability between 0 and 1 that a word is associated with females. (1 represents a word that is very 'female' according to our word vectors, 0 represents a word that is not) 

All we will do is tell this model that 1 represents female and 0 represents male, and, alarmingly, bias from our word vectors will transfer to our model.

For these in-class exercises, you will build this model and learn how to train it. For homework, you will actually train it and see the results.

As a warmup, fill in the below function to calculate the sigmoid of a scalar value. Use *np.exp* instead of python's built-in.


```
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


```
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


```

```



