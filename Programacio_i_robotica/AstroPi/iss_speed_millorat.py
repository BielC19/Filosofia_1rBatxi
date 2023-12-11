from exif import Image
from datetime import datetime
import cv2
import math


def get_time(image):
    with open(image, 'rb') as image_file:
        img = Image(image_file)
        time_str = img.get("datetime_original")
        time = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
    return time


def get_time_difference(image_1, image_2, image_3, image_4, image_5):
    time_1 = get_time(image_1)
    time_2 = get_time(image_2)
    time_3 = get_time(image_3)
    time_4 = get_time(image_4)
    time_5 = get_time(image_5)

    time_difference = datetime.datetime(seconds=0)
    time_difference -= time_5 - time_4
    time_difference -= time_4 - time_3
    time_difference -= time_3 - time_2
    time_difference -= time_2 - time_1

    print(time_difference.seconds)
    return time_difference.seconds


def convert_to_cv(image_1, image_2, image_3, image_4, image_5):
    image_1_cv = cv2.imread(image_1, 0)
    image_2_cv = cv2.imread(image_2, 0)
    image_3_cv = cv2.imread(image_3, 0)
    image_4_cv = cv2.imread(image_4, 0)
    image_5_cv = cv2.imread(image_5, 0)
    return image_1_cv, image_2_cv, image_3_cv, image_4_cv, image_5_cv


def calculate_features(image_1, image_2, image_3, image_4, image_5, feature_number):
    orb = cv2.ORB_create(nfeatures = feature_number)
    keypoints_1, descriptors_1 = orb.detectAndCompute(image_1_cv, None)
    keypoints_2, descriptors_2 = orb.detectAndCompute(image_2_cv, None)
    keypoints_3, descriptors_3 = orb.detectAndCompute(image_3_cv, None)
    keypoints_4, descriptors_4 = orb.detectAndCompute(image_4_cv, None)
    keypoints_5, descriptors_5 = orb.detectAndCompute(image_5_cv, None)
    return keypoints_1, keypoints_2, keypoints_3, keypoints_4, keypoints_5, descriptors_1, descriptors_2, descriptors_3, descriptors_4, descriptors_5


def calculate_matches(descriptors_1, descriptors_2, descriptors_3, descriptors_4, descriptors_5):
    brute_force = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = brute_force.match(descriptors_1, descriptors_2, descriptors_3, descriptors_4, descriptors_5)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches


image_1 = 'photo_0683.jpg'
image_2 = 'photo_0684.jpg'
image_3 = 'photo_0685.jpg'
image_4 = 'photo_0686.jpg'
image_5 = 'photo_0687.jpg'

def display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, image_3_cv, keypoints_3, image_4_cv, keypoints_4, image_5_cv, keypoints_5, matches):
    match_img = cv2.drawMatches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, image_3_cv, keypoints_3, image_4_cv, keypoints_4, image_5_cv, keypoints_5, matches[:100], None)
    resize = cv2.resize(match_img, (1600,600), interpolation = cv2.INTER_AREA)
    cv2.imshow('matches', resize)
    cv2.waitKey(0)
    cv2.destroyWindow('matches')


def find_matching_coordinates(keypoints_1, keypoints_2, keypoints_3, keypoints_4, keypoints_5, matches):
    coordinates_1 = []
    coordinates_2 = []
    coordinates_3 = []
    coordinates_4 = []
    coordinates_5 = []
    for match in matches:
        image_1_idx = match.queryIdx
        image_2_idx = match.trainIdx
        image_3_idx = match.trainIdx
        image_4_idx = match.trainIdx
        image_5_idx = match.trainIdx
        (x1,y1) = keypoints_1[image_1_idx].pt
        (x2,y2) = keypoints_2[image_2_idx].pt
        (x3,y3) = keypoints_3[image_3_idx].pt
        (x4,y4) = keypoints_4[image_4_idx].pt
        (x5,y5) = keypoints_5[image_5_idx].pt
        coordinates_1.append((x1,y1))
        coordinates_2.append((x2,y2))
        coordinates_3.append((x3,y3))
        coordinates_4.append((x4,y4))
        coordinates_5.append((x5,y5))
    return coordinates_1, coordinates_2, coordinates_3, coordinates_4, coordinates_5


def calculate_mean_distance(coordinates_1, coordinates_2, coordinates_3, coordinates_4, coordinates_5):
    all_distances = 0
    merged_coordinates = list(zip(coordinates_1, coordinates_2, coordinates_3, coordinates_4, coordinates_5))
    for coordinate in merged_coordinates:
        x_difference = coordinate[0][0] - coordinate[1][0]
        y_difference = coordinate[0][1] - coordinate[1][1]
        distance = math.hypot(x_difference, y_difference)
        all_distances = all_distances + distance
    return all_distances / len(merged_coordinates)


def calculate_speed_in_kmps(feature_distance, GSD, time_difference):
    distance = feature_distance * GSD / 100000
    speed = distance / time_difference
    return speed


time_difference = get_time_difference(image_1, image_2, image_3, image_4, image_5) # Get time difference between images
image_1_cv, image_2_cv, image_3_cv, image_4_cv, image_5_cv = convert_to_cv(image_1, image_2, image_3, image_4, image_5) # Create OpenCV image objects
keypoints_1, keypoints_2, keypoints_3, keypoints_4, keypoints_5, descriptors_1, descriptors_2, descriptors_3, descriptors_4, descriptors_5 = calculate_features(image_1_cv, image_2_cv, image_3_cv, image_4_cv, image_5_cv, 10000) # Get keypoints and descriptors
matches = calculate_matches(descriptors_1, descriptors_2, descriptors_3, descriptors_4, descriptors_5) # Match descriptors
display_matches(image_1_cv, keypoints_1, image_2_cv, image_3_cv, image_4_cv, image_5_cv, keypoints_2, keypoints_3, keypoints_4, keypoints_5, matches) # Display matches
coordinates_1, coordinates_2, coordinates_3, coordinates_4, coordinates_5 = find_matching_coordinates(keypoints_1, keypoints_2, keypoints_3, keypoints_4, keypoints_5, matches)
average_feature_distance = calculate_mean_distance(coordinates_1, coordinates_2, coordinates_3, coordinates_4, coordinates_5)
speed = calculate_speed_in_kmps(average_feature_distance, 12648, time_difference)
print(speed)