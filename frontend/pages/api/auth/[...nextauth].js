import NextAuth from "next-auth"
import GoogleProvider from "next-auth/providers/google"
import axios from 'axios'

export default NextAuth({
  providers: [
    GoogleProvider({
        clientId: process.env.GOOGLE_CLIENT_ID,
        clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    }),
    // ...add more providers here
    ],
    callbacks: { // https://next-auth.js.org/configuration/callbacks
        // signIn : 
        async signIn({ user, account, profile, email, credentials }) {
            //console.log('signIn: ',user, account, profile, email, credentials);
            if (account.provider === "google") {
                //const { accessToken, idToken } = account;
                const accessToken = account.access_token;
                const idToken = account.id_token;
                console.log(`access-token: \n${accessToken}\nid-token: \n${idToken}`);

                try {
                    const response = await axios.post( // ※axios : DRFのAPIをたたくために使用。fetchでも可
                        `${process.env.DJANGO_URL}api/social/login/google/`, // djangoのaccounts/urls.pyで勝手に設定しているだけなので、公式に/social/login/などはない
                        {
                            access_token: accessToken, // Django apiに入るためのアクセストークンを取得
                            id_token: idToken,
                        }
                    )
                    // レスポンスからアクセストークンを取得
                    const { access_token } = response.data;
                    const { userId } = response.data.user;
                    user.accessToken = access_token;
                    user.userId = userId;
                    account.userId = userId;
                    //console.log(account);
                    //console.log('access_token: ',access_token);
                    return true;
                } catch (error) {
                    // エラーの時はDjangoのコンソールやrestAPIサイトでアクセストークンなどを入力して試すと割とはっきりした原因が返ってくる
                    console.log('access_token: miss',error);
                    return true // Do different verification for other providers that don't have `email_verified`
                }
            }
            return false;
        },
        // jwtとsessionを組み合わせて、ログインしたユーザーの情報を取得できる（３，useSessionで取り出し）
        async jwt({ token, account }) {
            // サインイン直後にトークンへのOAuth access_tokenを永続化
            //console.log('jwt:',token,account);
            if (account) {
                token.accessToken = account.access_token // １，account → tokenにデータを移す（最初に↑のsignInでresponse→accountに移す）
                token.userId = account.userId
            }
            return token
        },
        async session({ session, token, user }) {
            // プロバイダーからクライエント側にユーザー情報を送信
            // user: データベースを作成するとデータベースから取得したuserデータが含まれるように
            //console.log('user:',session,token,user);
            session.accessToken = token.accessToken // ２，token → sessionにデータを移す
            session.userId = token.userId
            return session
        }
    }
})