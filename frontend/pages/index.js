import styles from '../styles/Home.module.scss'

import { useEffect, useState, createContext, useContext } from 'react';
import { UserContext, DataContext } from '../context/StateContext';
import { signIn, signOut, useSession } from 'next-auth/react'

import Layout from '../components/Layout';
import Navigation from '../components/Navigation'
import TextForm from '../components/TextForm';


export default function Home() {

  let userId = '';
  const { data: session } = useSession(); // sessionからデータ取得
  if (session) userId = session.userId;
  // console.log(session);

  const { data, setData } = useContext(DataContext);
  const [note, setNote] = useState('初期値');
  
  const setPage = (index,phase) => {
    setData({ index: index, phase: phase });
    setNote('セット！');
  }

  const tests = e => console.log(1);

  return (
    <Layout title='main-page'>
      <div className="main-content">
        <Navigation />
        <br/><br/>
        <button className='bg-yellow-300' onClick={() => setPage(1, 1)}>Click!</button>
        
        {note != 'note' && <TextForm userId={userId} data={data} />}
        
        <p className="hidde">index/phase : { data.index },{ data.phase }</p>
        <p>note    : { note }</p>
      </div>
    </Layout>
  )
}
