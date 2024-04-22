from anime_dl.utils.progress_bar import ProgressBar


def test():
    total = 2
    progress_bar = ProgressBar("TEST", 1, total)
    for i in range(total):
        progress_bar.print()
