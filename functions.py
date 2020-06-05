def progress_bar(progress: int, length: int, bar_length: int = 50, finish_mark: str='progress finish!'):
    """
    print progress
    :param progress: the number of present progress
    :param length: the number of total progress
    :param bar_length: bar length
    :param finish_mark: print string what you want when progress finish
    :return: return: True
    """

    progress = progress + 1
    progress_per = progress / length * 100
    progress_per_str = str(int(progress_per * 10) / 10)
    bar = '█' * int(bar_length / 100 * progress_per)
    space = '░' * (bar_length - int(bar_length / 100 * progress_per))

    print('|\r%s%s|    %s%%    %d/%d' % (bar, space, progress_per_str, progress, length), end='')
    if progress == length: print('\n' + finish_mark)

    return True


def make_video(images_path: str, save_path: str):
    """
    make avi file using images in path
    :param images_path: directory path for images
    :param save_path: directory path for video
    :return: True
    """
    import cv2
    import glob

    # when run in window, should replace backslash
    images_path = images_path.replace('\\', '/')
    save_path = save_path.replace('\\', '/')

    files = glob.glob(images_path + '/*.png')
    files = sorted(files)

    # when run in window, glob return backslash so this have to do
    for n, i in enumerate(files): files[n] = i.replace('\\', '/')

    h, w, _ = cv2.imread(files[0]).shape
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter(save_path, fourcc, 60, (w, h))
    length = len(files)

    for n, i in enumerate(files):
        out.write(cv2.imread(i))
        progress_bar(n, length, finish_mark='make finish')

    out.release()
    return True


def video2png(video_path: str, save_path: str):
    """
    video to png file
    save_path: video file directory, save_path: save png directory
    return True
    """
    print('read: %s' % (video_path))
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    for i in range(length):
        progress_bar(i, length, finish_mark = 'video to png finish!')
        frame = cap.read()[1]
        cv2.imwrite(save_path + '_%d.png' % (i), frame)
