## MobileNet Paper Summary

### Depthwise Separable Filters
The core building blocks of MobileNet are depthwise separable filters, which factorize a standard convolution into two separate layers: a depthwise convolution and a 1x1 pointwise convolution.

The depthwise convolution filters each channel in the input feature map separately, producing an intermediate filtered output feature map. The pointwise convolution then combines the depthwise filtered outputs into the final output feature map.

### Network Structure
The MobileNet network is built using depthwise separable filters, with a focus on reducing the number of parameters and computation required by the network.

### Width Multiplier (α)
A hyperparameter called width multiplier (α) is introduced to control the size of the model. By reducing α, the number of filters in each layer is reduced, leading to a smaller and faster model. For a given layer and width multiplier α, the number of input and output channels are scaled by α.

### Resolution Multiplier (ρ)
Another hyperparameter called resolution multiplier (ρ) is introduced to control the spatial resolution of the output feature maps and reduce the computational cost of the network. By reducing ρ, the spatial resolution of the output feature maps is reduced, leading to a smaller and faster model.

The information and questions above are based on the "MobileNet: Efficient Convolutional Neural Networks for Mobile Vision Applications" paper by Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Wei Wei, Tong Narang, James Philbin, and Kilian Q. Weinberger.

### Q&A
Q: What's the number of 1x1 convolution filters? Is it N?

A: Yes, it is N in this paper, where N is the output channels of a layer. The number of 1x1 convolution filters determines the number of output channels of the pointwise convolution, which combines the depthwise filtered outputs into the final output feature map.
