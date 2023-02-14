# Summary of "SSD: Single Shot MultiBox Detector" Paper

The "SSD: Single Shot MultiBox Detector" paper proposes several improvements for object detection, including:

## Part 1

Using a small convolutional filter to predict object categories and offsets in bounding box locations.

## Part 2

Using separate predictors (filters) for different aspect ratio detections. Applying these predictors to multiple feature maps from the later stages of a network to perform detection at multiple scales.

## Part 3

At training time, default boxes are matched to ground truth boxes, with positive matches treated as correct detections and negatives as incorrect. The SSD model adds feature layers to the end of a base network, which predict the offsets to default boxes of different scales and aspect ratios and their associated confidences.

## Part 4

For each ground truth box, we are selecting from default boxes that vary over location, aspect ratio, and scale in order to determine which default boxes correspond to a ground truth detection and train the network accordingly.
