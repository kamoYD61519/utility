#実行中のプログラムが認識しているカレントディレクトリを確認する
#ファイル読み込み等でpathエラーが出た際のデバッグ用コード
import os

# console あり
current_dir=os.getcwd()
print("Current directory:", current_dir)

# no-consoleならファイルに保存
my_path = '/Users/user' # ここを自分の開発環境に合わせて変更する
output_file = f'{my_path}/current_dir.txt'
try:
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Current Directory: {current_dir}\n")
except Exception as e:
    # 例外発生時はエラー内容をファイルに記録
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Error: {e}\n")
