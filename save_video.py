import cv2
import os

def make_video(folder):
    """
    Takes all the pics in the folder given and make a video
    out of it.
    """
    # Sorting on dates, ISO ftw
    filenames = sorted(os.listdir(folder))

    # Completely arbitrary values, probably will need to fix that later
    # If the video is too fast or too slow, change the fps value manually
    fps = 2
    if 20 <= len(filenames) <= 40:
        fps = 4
    elif 41 <= len(filenames) <= 200:
        fps = 10
    elif 201 <= len(filenames) <= 500:
        fps = 20
    elif len(filenames) > 500:
        fps = 40

    # Find out size of the pictures we're taking
    first_pic = cv2.imread('%s/%s' % (folder, filenames[0]))

    # shape gives a tuple (height, width, layer)
    height, width, _ = first_pic.shape

    # magic below, might need to change the codec for your own webcam
    fourcc = cv2.VideoWriter_fourcc('mp4v')

    video = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))

    for filename in filenames:
        video.write(cv2.imread('%s/%s' % (folder, filename)))

    video.release()
dir_path = 'data'
new_video = make_video(dir_path)