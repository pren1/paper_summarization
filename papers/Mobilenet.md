# MobileNet Paper Summary

## Introduction
- MobileNet is a deep neural network designed for efficient on-device inference.
- The network uses depthwise separable convolutions to reduce computational cost.

## Depthwise Separable Filters
- Standard convolutions filter and combine inputs into outputs in one step.
- Depthwise separable convolutions split this process into two layers: a depthwise convolution and a pointwise convolution.
- The depthwise convolution filters each channel of the input independently.
- The pointwise convolution then combines the filtered channels into a set of output features.

## MobileNet Network Structure
- The MobileNet network is built on depthwise separable filters.
- The network has two hyper-parameters to reduce computational cost: width multiplier and resolution multiplier.
- The width multiplier reduces the number of channels in each layer, while the resolution multiplier reduces the size of the input image.

## Width Multiplier
- For a given layer and width multiplier, the number of input channels becomes αM and the number of output channels becomes αN.

## Resolution Multiplier
- The resolution multiplier reduces the size of the input image, thereby reducing the computational cost of the network.

## Conclusion
- MobileNet is a deep neural network designed for efficient on-device inference using depthwise separable filters and hyper-parameters to reduce computational cost.
