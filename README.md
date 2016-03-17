#Ranking Module

The ranking module of Furnito is used to create a meaningful ranking for query terms from a document set.

It currently consists of three parts:
 - TF (term frequency)
 - IDF (inverted document frequency)
 - TF-IDF (combining the two previous parts)

TF currently consists of multiple options so performance of each options can be measured. The options are:
 - Raw frequency
 - Log Normalized
 - Double Normalized at 0.5
 - Double Normalized at K

IDF currently consists of the following options:
 - Normal IDF
 - Smoothed IDF
 - Maxed IDF

https://en.wikipedia.org/wiki/Tf–idf#Definition

/TODO: Vector Space Model - http://blog.josephwilk.net/projects/building-a-vector-space-search-engine-in-python.html
/Explanation VSM: http://www.site.uottawa.ca/~diana/csi4107/cosine_tf_idf_example.pdf
