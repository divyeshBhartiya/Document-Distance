# Document-Distance

## What is Document Distance?
The distance between two documents to be the angle between their word frequency vectors. The document distance problem is thus the problem of computing the distance between two given text documents.
Document similarities are measured based on the content overlap between documents. With the large number of text documents in our life, there is a need toautomatically process those documents for information extraction, similarity clustering, and search applications. There exist a vast number of complex algorithms to solve this problem. One of such algorithms is a cosine similarity - a vector based similarity measure. The cosine distance of two documents is defined by the angle between their feature vectors which are, in our case, word frequency vectors. The word frequency distribution of a document is a mapping from words to their frequency count.

## Concept Used: Cosine Similarity
https://en.wikipedia.org/wiki/Cosine_similarity
http://mlwiki.org/index.php/Cosine_Similarity

## Courtesy: MIT OpenCourseWare
I would recommend to follow the below link which I refered for creating this repo.
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/recitation-videos/MIT6_006F11_rec02.pdf

## Other Links: 
http://6.006.scripts.mit.edu/~6.006/spring08/wiki/index.php?title=Document_Distance_Problem_Definition
https://courses.csail.mit.edu/6.006/fall10/lectures/lecture1.pdf

## Summary:
This repo consists of 8 implementations for computing the Document Distance between the documents. Each implementation is different from one another. When you move from 1st implementation to 8th implementation, you will observe the improvement in the performance. 8th being the most optimised one and 1st being the least optimised one.
This repo provides a practical understanding about the Big O Notation and Time Complexity.
Use "python -m cProfile -s time docDistance8th.py" command to run the individual implementation one by one and note the time taken to achieve the Document Distance.

Cheers, Enjoy!!
