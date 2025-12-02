"""Machine Learning Notes – Explanation
📌 Page 1 — Supervised Learning

Machine Learning is a field where machines learn from data.

Supervised learning → Data is labeled (you know the correct answer/output)

Solves:

Regression problems → Predict continuous values (like salary, price, weight)

Classification problems → Predict categories (like pass/fail, spam/not spam)

Types of features:

Input feature (independent variable)

Output feature (dependent variable / target value)

📌 Page 2 — Regression Example

Example: CGPA → Package prediction

If CGPA increases, salary (package) also changes → numerical prediction → Regression

Algorithms for regression:

Linear Regression

Ridge Regression

Lasso Regression

Support Vector Regression

Decision Tree Regression

Random Forest Regression

📌 Page 3 — Classification Problems

Output is discrete

Examples:

Result prediction → Pass (1) or Fail (0)

Spam detection

Disease prediction

Image classification

📌 Page 4 — Unsupervised Learning

Works with unlabeled data

We don’t know the output beforehand

Solves:

Clustering → grouping customers

Dimensionality reduction

Anomaly detection (fraud detection)

Association (shopping patterns)

📌 Page 5 — Unsupervised Algorithms

K-Means

DBSCAN

PCA (Principal Component Analysis)

📌 Page 6–8 — Linear Regression

It is a supervised ML algorithm used for regression

Types:

Simple linear regression → one input

𝑌
=
𝑚
𝑋
+
𝑏
Y=mX+b

Multiple linear regression → multiple inputs

𝑌
=
𝑚
1
𝑋
1
+
𝑚
2
𝑋
2
+
𝑏
Y=m
1
	​

X
1
	​

+m
2
	​

X
2
	​

+b

Polynomial regression

𝑌
=
𝑏
0
+
𝑏
1
𝑋
+
𝑏
2
𝑋
2
Y=b
0
	​

+b
1
	​

X+b
2
	​

X
2

Shows graph and formula for best fit line

How to calculate:

Slope (m)

Intercept (b)

📌 Page 9–10 — Deep Learning & ANN

Deep Learning is a part of AI + ML

ANN → Artificial Neural Network

Structure inspired by the human brain

Example: Placement prediction

Network has:

Input Layer

Hidden Layer

Output Layer

Weights 
𝑊
1
,
𝑊
2
,
.
.
.
W1,W2,... and Bias 
𝑏
1
,
𝑏
2
,
.
.
.
b1,b2,... are learnable parameters

📌 Page 11–14 — Perceptron & Activation Functions

Perceptron → basic unit (neuron)

Activation function decides neuron output

Types shown:

Sigmoid (for binary classification)

Tanh (values: −1 to 1)

ReLU

Leaky ReLU (fixes dead neuron problem)

Graphs are shown for each function.

📌 Page 15–16 — Forward Propagation

Inputs are multiplied by weights

Bias is added

Activation function applied layer-by-layer

Final output is the prediction 
𝑦
^
y
^
	​


📌 Page 17–18 — Loss Functions

Used to check error between actual & predicted value

For Regression:

MSE → Mean Squared Error

MAE → Mean Absolute Error

For Classification:

Binary Cross Entropy (2 classes)

Categorical Cross Entropy (more than 2 classes)

📌 Page 19 — Backpropagation

Used for training neural networks

Adjust weights to reduce error

Uses Gradient Descent:

Update formula:

𝑊
𝑛
𝑒
𝑤
=
𝑊
𝑜
𝑙
𝑑
−
𝜂
∂
𝐿
∂
𝑊
W
new
	​

=W
old
	​

−η
∂W
∂L
	​


η = learning rate

📌 Page 20 — Overview

ANN used for tabular data

Shows Input → ANN → Output block diagram

🎯 Quick Summary
Concept	Type	What it predicts?
Supervised Learning	Labeled data	Regression & Classification
Unsupervised Learning	Unlabeled data	Clustering, grouping
Linear Regression	Regression	Continuous output
ANN / Deep Learning	Supervised	Complex tasks
Loss Functions	Regression & Classification	Measures model error


"""
