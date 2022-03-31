from numpy import *


def Inference(x):
    # ranging through each pixel in image
    classInferences = zeros(10).astype(int)
    for i in range(64):
        # per target class
        for ii in range(10):


if __name__ == '__main__':
    # Initialize frequency_array
    freq_arr = zeros(10).astype(int)
    n = int((80/100)*(1797))  # 80% of data to be used as training data

    # loop training data to set up frequency array
    # generating array to hold training data
    training_data = []
    training_data_labels = []
    for i in range(n):
        tmp = input().split(',')
        tmp = [int(x) for x in tmp]
        freq_arr[tmp[len(tmp)-1]] += 1
        training_data_labels += [tmp[len(tmp)-1]]
        training_data += [tmp[0:len(tmp)-1:1]]

    # build class conditional model
    cc_model = zeros((64, 10))
    for i in range(n):
        tmp = training_data[i]
        label = training_data_labels[i]
        # loop training_data example to update ccmodel
        for r in range(64):
            if(tmp[r] == 1):
                # pixel is on => update ccmodel
                cc_model[r][label] += 1/freq_arr[label]
    # smoothing
    k = 1
    for rr in range(64):
        for cc in range(10):
            if (cc_model[rr][cc] == 0):
                # now we smooth?
                cc_model[rr][cc] = k / (10 + (64*k))

    # take in test data
    test_data = []
    for i in range(1797):
        if(i < n):
            continue
        else:
            tmp = input().split(',')
            [int(x) for x in tmp]
            test_data += [tmp]
