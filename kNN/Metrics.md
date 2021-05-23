# Metrics

https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9

https://rubikscode.net/2020/10/19/14-popular-machine-learning-evaluation-metrics/

https://neptune.ai/blog/performance-metrics-in-machine-learning-complete-guide

https://developers.google.com/machine-learning/crash-course/classification/true-false-positive-negative


* note that we have a balanced sett (100 pieces of data for each song)

## Accuracy 
* total number of correct predictions over total number of predictions
* could be misleading, especially when there is an imbalanced dataset where one kind of instance is more popular than the others
* Models that overfit can have an accuracy of 100%

## Precision
* (TP) / (TP + FP)
* talks about how precise/accurate model is *out of those predicted positive* (how many of them actually positive)
* Good measure for when the cost of a false positive is high 
* ex: E-mail Spam (false positive means e-mail with critical info could be lost)

## Recall 
* (TP) / (TP + FN)
* use when high cost associated with a false negative

## F1 Score
* F1 = 2 * (precision * recall)/(precision + recall)
* want a balance between precision and recall AND there is an uneven class distribution

## What constitutes TP, FP, TN, FN in our case?
* Ex: Jazz
* True Positive: Song is Jazz and is classified as Jazz
* True Negative: Song is not Jazz and is not classified as Jazz
* False Positive: Song is not Jazz, but is classified as Jazz
* False Negative: Song is Jazz, but is classified as not Jazz

* In our scenario, we don't want ANY false positives, false negatives
* Want something that reflects this, could be F1 or ROC/AUC

https://neptune.ai/blog/f1-score-accuracy-roc-auc-pr-auc
* Choose between Accuracy, F1, ROC AUC
* Accuracy is good when:
  * problem is balanced
  * every class is equally important to us
* F1 score
  * when you care more about the positive class (true positives, false positives)
  * can be easily explained to business takeholders(?)
* ROC AUC 
  * Visualizes tradeoff between True Positive Rate and False Positive Rate
  * care about ranking predictions and not necessarily about outputting well-calibrated probabilities 
  * should not use it when data is heavily imbalanced 
  * should use it when you care equally about positive and negative classes
* PR AUC 
  * Combines precision and recall in single visualization
  * For every threshold, calculate and plot 
  * higher recall = lower precision (and vice versa)
  * Apply when
    * data is heavily imbalanced 
    * when you care more about positive than negative class
* Accuracy vs ROC AUC
  * calculate accuracy on predicted classes, but you calculate ROC AUC on predicted scores
  * accuracy is suspect to imbalance issues (if we can categorize all in the majority class correctly, it looks like we have good accuracy but we've omitted failures in the minority scores)
  * if problem is balanced (yes!) and we *care about both positive and negative predictions* accuracy is a good choice 
  * ROC AUC is especially good at ranking predictions (what does it mean to rank predictions?) 
* F1 score vs Accuracy 
  * F1 score is balancing precision and recall on the positive class
  * accurracy looks at both positive and negative
 
https://machinelearningmastery.com/calibrated-classification-model-in-scikit-learn/
* Sometimes maybe useful to figure out the probability that an item belongs to a certain category 
* Not really necessary for us because with an equally balanced dataset the probabilities are identical (no skew)

https://deepai.org/machine-learning-glossary-and-terms/f-score
* F score (you can tune a parameter called beta to place more emphasis on recall/precision)
* F1 is useful when 
  * There are either differing costs in false positives or false negatives, such as in the mammogram example
  * Or where there is a large class imbalance, such as ...


https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc

