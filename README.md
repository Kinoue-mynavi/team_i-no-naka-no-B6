# team_i-no-naka-no-B6

## Git 運用手順

1. 最新の差分をPULL

事前に、`git branch`でmainブランチにいることを確認する。

```shell
git pull
```

2. ブランチ作成

```shell
git checkout -b 【自分の苗字(半角英数)】
```

3. ブランチが作成されたかを確認する

```shell
git branch
```
↓自分が作成したブランチ名に「*」が入っていればOK
```shell
* 【自分の苗字(半角英数)】
main
```

4. ローカルで変更したコードをステージングする

```shell
git add .
```

5. 変更をコミット

```shell
git commit -m "【任意のコミットメッセージを入力】"
```

6. ローカルのコミットをリモートに反映

```shell
git push origin 【自分の苗字(半角英数)】
```

7. Githubにアクセスする

https://github.com/Kinoue-mynavi/team_i-no-naka-no-B6/pulls

アラートが出ているので、ボタンクリックしてPull Requestを作成する（「Create Pull Request」）
