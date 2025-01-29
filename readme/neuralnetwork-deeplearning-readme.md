# Neural Network & Deep Learning

A neural network is a method in artificial intelligence that teaches computers to process data in a way that is inspired by the human brain. It is a type of machine learning process that uses interconnected nodes or neurons in a layered structure that resembles the human brain. Examples of neural network is 

Every neural network consists of layers of nodes, or artificial neurons
* an input layer
* one or more hidden layers
* an output layer

Each node connects to others, and has its own associated weight and threshold. If the output of any individual node is above the specified threshold value, that node is activated, sending data to the next layer of the network. Otherwise, no data is passed along to the next layer of the network.

## Deep Learning
Deep Learning and neural networks tend to be used interchangeably in conversation. 
* `Deep Learning` is a neural network that consists of more than three layers—which would be inclusive of the inputs and the output 
* A neural network that only has two or three layers is just a `basic neural network`.

![alt txt](/images/deep-neural-network.png)

## What are neural networks used for?
Some areas where it is used
* Computer Vision
* Speech recognition
* Natural language processing

## How do neural networks work?
Think of each individual node as its own [linear regression](https://www.ibm.com/topics/linear-regression) model, composed of input data, weights, a bias (or threshold), and an output. The formula would look something like this:

∑wixi + bias = w1x1 + w2x2 + w3x3 + bias

output = f(x) = 1 if ∑w1x1 + b>= 0; 0 if ∑w1x1 + b < 0

Once an input layer is determined, weights are assigned. These weights help determine the importance of any given variable, with larger ones contributing more significantly to the output compared to other inputs. All inputs are then multiplied by their respective weights and then summed. Afterward, the output is passed through an activation function, which determines the output. If that output exceeds a given threshold, it “fires” (or activates) the node, passing data to the next layer in the network. This results in the output of one node becoming in the input of the next node. This process of passing data from one layer to the next layer defines this neural network as a feedforward network.

Let’s break down what one single node might look like using binary values. We can apply this concept to a more tangible example, like whether you should go surfing (Yes: 1, No: 0). The decision to go or not to go is our predicted outcome, or y-hat. Let’s assume that there are three factors influencing your decision-making:

Are the waves good? (Yes: 1, No: 0)
Is the line-up empty? (Yes: 1, No: 0)
Has there been a recent shark attack? (Yes: 0, No: 1)
Then, let’s assume the following, giving us the following inputs:

X1 = 1, since the waves are pumping
X2 = 0, since the crowds are out
X3 = 1, since there hasn’t been a recent shark attack
Now, we need to assign some weights to determine importance. Larger weights signify that particular variables are of greater importance to the decision or outcome.

W1 = 5, since large swells don’t come around often
W2 = 2, since you’re used to the crowds
W3 = 4, since you have a fear of sharks
Finally, we’ll also assume a threshold value of 3, which would translate to a bias value of –3. With all the various inputs, we can start to plug in values into the formula to get the desired output.

Y-hat = (1*5) + (0*2) + (1*4) – 3 = 6

If we use the activation function from the beginning of this section, we can determine that the output of this node would be 1, since 6 is greater than 0. In this instance, you would go surfing; but if we adjust the weights or the threshold, we can achieve different outcomes from the model. When we observe one decision, like in the above example, we can see how a neural network could make increasingly complex decisions depending on the output of previous decisions or layers.

## References
* [Neural Network - AWS](https://aws.amazon.com/what-is/neural-network/)
* [Neural Network - IBM](https://www.ibm.com/topics/neural-networks)
* [AI vs. Machine Learning vs. Deep Learning vs. Neural Networks: What’s the difference?](https://www.ibm.com/blog/ai-vs-machine-learning-vs-deep-learning-vs-neural-networks/)