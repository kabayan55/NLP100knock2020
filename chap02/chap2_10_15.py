def knock10():
    """
    10. 行数のカウント
    行数をカウントせよ．確認にはwcコマンドを用いよ．
    """
    with open('../data/popular-names.txt', mode='r') as file:
        print(len(file.readlines()))

def knock11():
    """
    11. タブをスペースに置換
    タブ1文字につきスペース1文字に置換せよ．
    確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
    """
    with open('../data/popular-names.txt', mode='r') as file:
        line_space = ''
        for line in file:
            line_space += line.replace('\t', ' ')
        print(line_space)

def knock12():
    """
    12. 1列目をcol1.txtに，2列目をcol2.txtに保存
    各行の1列目だけを抜き出したものをcol1.txtに，
    2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
    確認にはcutコマンドを用いよ．
    """
    col1 = []
    col2 = []
    with open('../data/popular-names.txt', mode='r') as file:
        for line in file:
            elems = line.split()
            col1.append(elems[0])
            col2.append(elems[1])
    with open('../data/col1.txt', mode='w') as col1_file:
        col1_file.write('\n'.join(col1))
        col1_file.write('\n')
    with open('../data/col2.txt', mode='w') as col2_file:
        col2_file.write('\n'.join(col2))
        col2_file.write('\n')

def knock13():
    """
    13. col1.txtとcol2.txtをマージ
    12で作ったcol1.txtとcol2.txtを結合し，
    元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
    確認にはpasteコマンドを用いよ．
    """
    with open('../data/col1.txt', mode='r') as col1_file:
        with open('../data/col2.txt', mode='r') as col2_file:
            with open('../data/merged.txt', mode='w') as merged_file:
                for col1, col2 in zip(col1_file, col2_file):
                    merged_file.write(col1.strip()+'\t'+col2.strip()+'\n')

def knock14(n_pre):
    """
    14. 先頭からN行を出力
    自然数Nをコマンドライン引数などの手段で受け取り，
    入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
    """
    with open('../data/popular-names.txt', mode='r') as file:
        for line, i in zip(file, range(int(n_pre))):
            print(line)

def knock15(n_post):
    """
    15. 末尾のN行を出力
    自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
    確認にはtailコマンドを用いよ．
    """
    with open('../data/popular-names.txt', mode='r') as file:
        lines_list = []
        for line in file:
            lines_list.append(line.strip())
        for i in range(len(lines_list)-n_post, len(lines_list)):
            print(lines_list[i])

def main(n):
    print('10:')
    knock10()
    print('11:')
    knock11()
    knock12()
    knock13()
    print('14:')
    knock14(n)
    print('15:')
    knock15(n)

if __name__ == "__main__":
    n = input()
    main(int(n))
