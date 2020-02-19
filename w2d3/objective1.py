# Not yet optimized => Still O(N^2)


def rotate_image(image):
    output = [[] for i in image]

    for i in image:
        for j in range(len(image)):
            output[j].append(i.pop(-1))

    print(output)


rotate_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
