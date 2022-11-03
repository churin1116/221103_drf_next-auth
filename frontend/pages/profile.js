import { getSession } from 'next-auth/react'
import Link from 'next/link'
import Image from 'next/image'

export default function Profile({ user }) {
  return (
    <div className="flex flex-col items-center">
        <h1 className="text-3xl mb-3 font-bold">Profile</h1>
        <div className="border w-14 mb-5"></div>
        <img src={user.image} className="rounded-full mb-3" width={100} height={100} alt='profile_img' />
        <p className="text-xl">{user.name}</p>
        <p>{user.email}</p>
        <Link href="/" className='mt-4'>
        Back
        </Link>
    </div>
  )
}

export async function getServerSideProps(context) {
  const session = await getSession(context)

  if (!session) { // セッション情報が取得出来なかったらメインページへ
    return {
      redirect: {
        destination: '/',
        permanent: false,
      },
    }
  }

  return {
    props: {
      user: session.user,
    },
  }
}