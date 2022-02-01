from utils import *
import numpy as np


def warpPerspective(img, transform_matrix, output_width, output_height):
    """
    TODO : find warp perspective of image_matrix and return it
    :return a (width x height) warped image
    """
    out = np.empty((output_width, output_height, 3), np.float64)
    rows = img.shape[0]
    cols = img.shape[1]
    for i in range(0, rows):
        for j in range(0, cols):
            x_in = np.array([[i],[j],[1]])
            x_temp = transform_matrix.dot(x_in)
            x_out = np.array([[x_temp[0][0]/x_temp[2][0]],[x_temp[1][0]/x_temp[2][0]]])
            if(x_out[0][0]>=0 and x_out[1][0]>=0 and x_out[1][0]<output_height and x_out[0][0]<output_width):
                out[int(x_out[0][0])][int(x_out[1][0])] = img[i][j]
    return out.astype(np.uint8)

    pass


def grayScaledFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    filter_matrix = np.array([[0.299,0.587,0.114],
                              [0.299,0.587,0.114],
                              [0.299,0.587,0.114]])
    return Filter(img, filter_matrix)
    pass


def crazyFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    filter_matrix = np.array([[0,1,1],
                              [1,0,0],
                              [0,0,0]])
    return Filter(img, filter_matrix)
    pass


def customFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    filter_matrix = np.array([[1,0,1],
                              [0,2,1],
                              [0,0,4]])
    inverted = np.linalg.inv(filter_matrix)
    custom =  Filter(img, filter_matrix)
    showImage(custom, "Custom Image")
    return Filter(custom, inverted)
    pass


def scaleImg(img, scale_width, scale_height):
    """
    TODO : Complete this part based on the description in the manual!
    """
    out = np.empty((img.shape[0]*scale_width, img.shape[1]*scale_height , 3), np.float64)
    rows = out.shape[0]
    cols = out.shape[1]
    for i in range(0, rows):
        for j in range(0, cols):
            out[i][j] = img[int(i/scale_width)][int(j/scale_height)]
    return out
    pass


def cropImg(img, start_row, end_row, start_column, end_column):
    """
    TODO : Complete this part based on the description in the manual!
    """
    return img[start_column:end_column,start_row:end_row]
    pass


if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')

    # You can change width and height if you want
    width, height = 300, 400

    showImage(image_matrix, title="Input Image")

    # TODO : Find coordinates of four corners of your inner Image ( X,Y format)
    #  Order of coordinates: Upper Left, Upper Right, Down Left, Down Right
    pts1 = np.float32([[106, 214], [378, 179], [159, 644], [495, 577]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    m = getPerspectiveTransform(pts1, pts2)

    warpedImage = warpPerspective(image_matrix, m, width, height)
    showWarpPerspective(warpedImage)

    grayScalePic = grayScaledFilter(warpedImage)
    showImage(grayScalePic, title="Gray Scaled")

    crazyImage = crazyFilter(warpedImage)
    showImage(crazyImage, title="Crazy Filter")

    customFilterPic = customFilter(warpedImage)
    showImage(customFilterPic, title="ّInverted Custom Filter")

    croppedImage = cropImg(warpedImage, 50, 300, 50, 225)
    showImage(croppedImage, title="Cropped Image")

    scaledImage = scaleImg(warpedImage, 2, 3)
    showImage(scaledImage, title="Scaled Image")
