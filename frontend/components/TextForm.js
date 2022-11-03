import { useSession } from "next-auth/react";
import { useState, useContext } from "react";
import { StateContext } from '../context/StateContext';
import styles from '../styles/Home.module.scss'

export default function TextForm({ userId=userId,data=data }) {
    // useContext：propsによる値の引き渡しを行うこと無く、Globalにデータの共有できる
    //const user = useContext(UserContext); // ２つ目の引数は、更新のトリガーとなる内容
    //const {data, setData} = useContext(DataContext);
    //const { data, setData } = useContext(StateContext); // ２つ目の引数は、更新のトリガーとなる内容


    const [text, setText] = useState('');
    const { data: session } = useSession();
    

    const create = async (e) => {
        e.preventDefault();
        const now = new Date();
        //console.log(userId, data.index, data.phase, text)
        await fetch(`${process.env.NEXT_PUBLIC_RESTAPI_URL}api/notes/`, {
            method: 'POST',
            body: JSON.stringify({ user:userId, index:data.index, phase:data.phase, note:text, created_at: now.toLocaleString().replace('/','-').replace('/','-') }),
            headers: {
                'Content-Type': 'application/json',
            },
        }).catch((error) => {
            console.log('error in TextForm create',error);
        });
        setText('');
    };
    
    const update = async (e) => {
        e.preventDefault();
        await fetch(`${process.env.NEXT_PUBLIC_RESTAPI_URL}api/note/${note.id}/`, {
            method: 'PUT',
            body: JSON.stringify({Text}),
            headers: {
                'Content-Type': 'application/json',
                //Authorization: `JWT ${cookie.get('access_token')}`,
            },
        }).then((res) => {
            if (res.state === 401) {
                alert('JWT Token not valid');
            }
        });
        setText({ id: 0, content: '' });
        //mutate(); // useSWRのmutate()を実施＝フェッチ後のキャッシュの更新
    };

    return (
        <div>
            <form onSubmit={create} className='flex items-end mb-6'>
                <div className="w-full mr-3">
                    <input
                        className="h-10 px-2 py-1 bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        type='text'
                        value={text}
                        onChange={(e) => 
                            setText(e.target.value)
                        }
                    />
                </div>
                
                <div>
                    <button type="submit" className={`ml-2 h-10 text-lg font-bold w-20 px-1 py-1 pl-3 rounded uppercase ${styles.dialogue_btn_color}`}>
                        {'送信！'}
                    </button>
                </div>
            </form>
        </div>
    );
}

