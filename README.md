# 221103_drf_next-auth
DRFとnextjs、next-authを使った Google認証/POST の最小限コード

note : https://note.com/churin_1116/n/n274cde46da85


## 導入方法

1. Google OAuth の登録

https://qiita.com/cokemaniaIIDX/items/bdb9a00bef3c6c2365f5
と同じ。最後のredirect_urlだけ異なるので注意。http://127.0.0.1:3000/api/auth/callback/google
![image](https://user-images.githubusercontent.com/90027034/199681028-a8ccdfa3-4727-4f04-845c-0b21e9f92378.png)


2. リポジトリをダウンロードするだけでは、node_modulesなどが抜けているのでおそらく再現できない。あくまでmodels.pyなどの内容把握用。

```yaml

--- backend ---

python -m venv venv
venv\Scripts\activate

pip install django django-cors-headers djangorestframework djangorestframework-simplejwt PyJWT dj-rest-auth django-allauth
django-admin startproject backend
cd backend
python manage.py startapp testapp  # postsなど
python manage.py startapp accounts # カスタムユーザー、認証
.gitignoreやsettings_local.pyも作成
あとのコードはこのリポジトリの通り

makemigrations/migrate
createsuperuser
```

一度、管理画面を開く。Google Cloud Consoleで取得したクライエントID・シークレットをDjango管理画面の「Social applications」にも追加→入力・保存（プロバイダーはGoogle、名前は自由。一番下のサイトをexample.comを選択し右へ移動させる。keyは空欄でOK）すれば完了。
![image](https://user-images.githubusercontent.com/90027034/199682789-68067dcc-7563-42fb-a056-ad891c9a4f45.png)

```yaml
--- frontend ---

npx create-next-app {アプリ名}
npm install sass axios（グーグル認証を追加する場合。axios : DRFのAPIをたたくために使用。fetchでも可） 
npm install -D tailwindcss postcss autoprefixer 
npx tailwindcss init -p

# tailwind.config.jsファイルを書き換え
# Styles/globals.cssを丸ごと消して書き換え
# _app.jsに「import '../public/style.scss'」を追加

configなどと同じ高さに「.env.local」を作成

NEXTAUTH_URL=http://127.0.0.1:3000/
DJANGO_URL=http://127.0.0.1:8000/
NEXT_PUBLIC_RESTAPI_URL=http://127.0.0.1:8000/
NEXTAUTH_SECRET=https://generate-secret.now.sh/32
GOOGLE_CLIENT_ID=***.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=GOCSPX-***
```

あとはそれぞれサーバーを起動させればOK。
.env.localは一度サーバーを切り、再起動させないと反映されないので注意。

![image](https://user-images.githubusercontent.com/90027034/199677331-d5f7e2cb-b92f-418b-a412-34aa8748404d.png)
![image](https://user-images.githubusercontent.com/90027034/199677527-0dfdc2ff-2968-4655-b43d-4632c665b39d.png)
