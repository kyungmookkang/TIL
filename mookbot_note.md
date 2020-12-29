# *# 묵봇 복습장*

## 기본기



### 1. 디렉토리 생성

```
mkdir  <foldername>   # 폴더 생성

cd  <foldername>   # 폴더로 이동
```



### 2. 초기화

````
초기화는 `git init` 을 통해 진행한다.

`git status` 로 확인한다.
````

 

### 3. 파일 생성

```
$touch *.txt

파일 생성

$rm *.txt

파일 삭제
```



### 4. add하기

```
git add <생성한_파일_이름>
```

### 5. commit 하기

```
git cmmit 했을 시,
esc를 누르고, :q! 로 나온다.

git commit -m 'message_name'
```



### 6. log 보기

```
git log
```



### 7. 원격 저장소(remote repo) 등록하기

```
git remote add origin <URL>

git remove -v 	# 등록한 remote 확인


git remote rm <remote_repo_name>	 # remote 제거
```



### 8. 원격 저장소에 push 하기

```
git push origin master
```

## Summary

| 명령어                           | 설명                                                |
| -------------------------------- | --------------------------------------------------- |
| `git init`                       | 빈 디렉토리(폴더)를 git 저장소(repo)로 초기화 한다. |
| `git add <filename>`             | 을 Stage에 올린다.                                  |
| `git commit -m 'commit message'` | commit하기                                          |
| `git log -2`                     | 최근 2개의 로고                                     |
| `git log --pretty=oneline`       | commit 내용이 한줄에 보여짐                         |
| `git commit --amend`             | commit 내용 수정                                    |

| 명령어                     | 설명                                   |
| -------------------------- | -------------------------------------- |
| `~`                        | 홈 폴더                                |
| `ctrl+c`                   | cancel. 동작 취소                      |
| `cd ..`                    | 뒤로가기                               |
| `cd 알파벳+Tab`            | 해당 알파벳으로 시작하는 디렉토리 검색 |
| `cd 디렉토리_이름`         | 해당 디렉토리로 이동                   |
| `cd ~/디렉토리_이름`       |                                        |
| `mv 원래이름/ 변경할_이름` | 디렉토리 이름 변경                     |
| `mv *.py *.txt`            | 파일 확장자 변경                       |
| `git remove 삭제파일_이름` | 삭제한 파일을 복구                     |
| `rm -rf 디렉토리_이름`     | 디렉토리 삭제                          |
| `rm -rf .git`              | git 삭제                               |
| `vim`                      | 터미널 문서 편집기                     |
| `*.md`                     | 정리 내용 확장자                       |

- 1. commit은 stage에 있는 내용을 찍는다.
- 1. stage에 올리는 명령어는 'git add'



## 응용



### 1. branch

```
$git branch <branch_name>		# 브랜치 생성

$git branch -d <branch_name>		# 브랜치 삭제

$git branch		# 브랜치 확인

$git switch -c <branch_name>		# 브랜치 생성 후 전환

$git switch <branch_name>		# 브랜치 전환

$git merge <branch_name>		# 브랜치 병합 !!! 꼭 Master 브랜치로 이동 후 병합하기 !!!

$git merge --abort 		# 브랜치 병합 취소
```



### 2.  원격 저장소 복제

`local`에 없는 상태에서 원격 저장소의 data를 가져온다.

```
$git clone <URL>

Cloning into <name>...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
```



### 3. push

`add` 하고 `commit` 한 코드를 내보낸다.

```
$git push <remote> <branch>

$git push origin master

Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 295 bytes | 295.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To <URL>
   e6b2104..5284d48  master -> master
```

강제 푸시  `$ git push origin +master`





### 4. push 취소

```
$git reset HEAD^;

Unstaged changes after reset:
$git reflog
$git log -g #확인

$git push origin master -f #강제 push
```

### 

### 5. pull

`local`에 없는 data를 내려받아 연결된 remote branch와 자동으로 merge한다.

```
$git pull <remote> <branch>
```

### pull 취소

```
git reset --hard ORIG_HEAD
```



## Summary

| 명령어                                    | 설명                        |
| ----------------------------------------- | --------------------------- |
| `touch 디렉토리_이름/*.md`                | 디렉토리에 *.md 파일을 추가 |
| `.gitignore`                              | 무시할 파일을 담는 디렉토리 |
| `git branch -r`                           | 원격 브랜치 확인            |
| `git branch -a`                           | 로컬 브랜치 확인            |
| `git switch -h`                           | help. 안내                  |
| `git log --pretty=format:"%h %s" --graph` | 그래프형 commit history     |



