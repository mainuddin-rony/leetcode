def channelModel(x, y, distance_type):
    """Method to calculate channel model probability for errors."""
    # corpus = ' '.join(self.ng.words)
    if distance_type == 'ins':
        if x == '#':
            return addmatrix[x + y] / corpus.count(' ' + y)
        else:
            return addmatrix[x + y] / corpus.count(x)
    if distance_type == 'sub':
        return submatrix[(x + y)[0:2]] / corpus.count(y)
    if distance_type == 'trans':
        return revmatrix[x + y] / corpus.count(x + y)
    if distance_type == 'del':
        return delmatrix[x + y] / corpus.count(x + y)