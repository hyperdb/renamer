# renamer

## 概要

srcディレクトリにあるファイルをリネームしてdistディレクトリに移動するPythonスクリプトです。

生成AIを利用して生成した画像をダウンロードした際にファイル名が常に同じになっていることがあり、これをリネームすること目的としたスクリプトです。

リネーム後のファイル名はファイル情報から得られたファイル作成時間（秒）にランダムで生成した6文字の文字列を付加した名称となっています。

>
> This Python script renames files in the src directory and moves them to the dist directory.
>
>This script is intended to rename the file name that is always the same when downloading images generated using the generation AI.
>
>The file name after renaming is the file creation time (in seconds) obtained from the file information, with a randomly generated 6-character string appended to it.
>
(translated by DeepL)

## 作成環境

- Python 3.11.0
