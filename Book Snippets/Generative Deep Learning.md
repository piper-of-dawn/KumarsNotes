## Generative Learning
### Human brain as a generative model
Finally, if we are to truly say that we have built a machine that has acquired a
form of intelligence that is comparable to a human’s, generative modeling
must surely be part of the solution. One of the finest examples of a generative
model in the natural world is the person reading this book. Take a moment to
consider what an incredible generative model you are. You can close your eyes
and imagine what an elephant would look like from any possible angle. You
can imagine a number of plausible different endings to your favorite TV show,
and you can plan your week ahead by working through various futures in your
mind’s eye and taking action accordingly. Current neuroscientific theory
suggests that our perception of reality is not a highly complex discriminative
model operating on our sensory input to produce predictions of what we are
experiencing, but is instead a generative model that is trained from birth to
produce simulations of our surroundings that accurately match the future.

### Representational Learning
_It is about projecting a higher dimensional data to a lower dimensional latent space._ Suppose you wanted to describe your appearance to someone who was looking for you in a crowd of people and didn’t know what you looked like. You wouldn’t start by stating the color of pixel 1 of your hair, then pixel 2, then pixel 3, etc. Instead, you would make the reasonable assumption that the other person has a general idea of what an average human looks like, then amend this baseline with features that describe groups of pixels, such as I have very blonde hair or I wear glasses. With no more than 10 or so of these statements, the person would be able to map the description back into pixels to generate an image of you in their head. The image wouldn’t be perfect, but it would be a close enough likeness to your actual appearance for them to find you among possibly hundreds of other people, even if they’ve never seen you before. 

### Generative Modelling and Statistical Distributions

#### Likelihood Function
$$ \mathcal{L}(\theta, x) = p_x(\theta) $$
- The likelihood function is a function of the parameter. It is mapping of a parameter to its probability.
- Suppose, we have a set of observations $(x_1 \dots x_n)$ sampled from a normal distribution, the question we ask is what mean $\mu$ and variance $\sigma^2$, would have generated these observations. 
- Now we know that the likelihood function maps a parameter to its probability. We can now ask the question, what value of $\mu$ and $\sigma^2$ would have generated these observations with the highest probability. This is the maximum likelihood estimation. $$ \mathcal{L}(\mu, \sigma^2) = \prod_{i=1}^n p_{x_i}(\mu, \sigma^2) $$
- The righthand side is the joint probability of the observations. We can take the log of the likelihood function to make the computation easier.
$$ \log \mathcal{L}(\mu, \sigma^2) = \sum_{i=1}^n \log p_{x_i}(\mu, \sigma^2) $$
- And the maximization problem can be stated as:  $$ \hat{\mu}, \hat{\sigma^2} = \arg \max_{\mu, \sigma^2} \log \mathcal{L}(\mu, \sigma^2) $$
### Taxonomy of Generative Model
The generative models are the models that aim to represent the underlying true data-generating distribution. The generative models can model the underlying density either explicitly or implicitly. 
Explicit density models would explicitly specify the density of the underlying distribution, such as Gaussian or Uniform, and would try to learn the parameters of the distribution through maximum likelihood or Bayesian inference. 

## Deep Learning


