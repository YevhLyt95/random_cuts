# random_cuts
Project by tutorial, but I correct mystakes and add some changes to random generated data in order to make usage of this method more proper
The second graph shows the distribution of the "depth" of points in the random cut tree. The depth of a point shows how far it is in the tree hierarchy, i.e. how many times the data had to be cut to isolate this point. Light points are closer to the root - they are isolated quickly, which may hint at their loneliness or anomaly. Dark points are deeper in the tree - they are grouped with others and require more cuts to separate them, which already looks like dense clusters.

If the graph shows clearly distinguished areas with similar depths, this is a signal of data clustering: the random cut tree "prompted" us where the data is closely related. But points whose depth differs sharply from their neighbors may be signs of anomalies.
