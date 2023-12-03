from moviepy.editor import VideoFileClip

# 動画をGIFに変換する関数
def convert_video_to_gif(input_file, output_file, fps=10):
    # 動画ファイルの読み込み
    clip = VideoFileClip(input_file)

    # GIFに変換
    clip.write_gif(output_file, fps=fps)

# メイン関数
if __name__ == "__main__":
    # 入力動画ファイル名
    input_file = "input_video.mp4"

    # 出力GIFファイル名
    output_file = "output_video.gif"

    # GIFのフレームレート
    fps = 10

    # convert_video_to_gif 関数を呼び出して、動画を GIF に変換
    convert_video_to_gif(input_file, output_file, fps)
