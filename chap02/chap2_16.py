import pandas as pd

def knock16(n_files):
    """
    16. ファイルをN分割する
    自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
    同様の処理をsplitコマンドで実現せよ．
    """
    df = pd.read_csv('../data/popular-names.txt', sep='\t', header=None)
    if len(df)%n_files == 0:
        n_row = len(df) // n_files
    else:
        n_row = len(df) // n_files + 1

    for i in range(n_files):
        df.loc[n_row * i:n_row * (i + 1)].to_csv(f'../chap02/16_devided_{i}.tsv',
                                                 sep='\t', index=False, header=None)


if __name__ == "__main__":
    n = input()
    knock16(int(n))
