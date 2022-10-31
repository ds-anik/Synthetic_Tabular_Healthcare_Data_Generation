# WGAN
This is an implementation of Wasserstein GAN with gradient penalty (WGAN-GP) to generate tabular data containig both categorical and continuous features. The generator and critic’s structures are fully connected neural networks with 256 neurons using batch normalization, ReLU (only in generator), and LeakyReLU (only in critic) in their internal layers. To generate both data types, the generator uses a tangent hyperbolic activation function for the continuous columns and a Gumbel Softmax function for the categorical ones. Finally, the model uses the Adam as optimizer in the training process.

## Prerequisite

```
numpy
pandas
scikit-learn
matplotlib
seaborn
scipy
hyperopt
tensorboard==2.1.0
tensorflow==2.1.0
tensorflow-estimator==2.1.0
tensorflow-probability==0.9.0
```