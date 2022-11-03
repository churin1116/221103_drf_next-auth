import { useSession, signIn, signOut } from "next-auth/react"
import Link from 'next/link'

export default function Navigation() {
    const { data: session } = useSession();

    return (
        <>
            {session && session.accessToken ? (
            <>
                <Link href="/profile">
                    <p className="">Profile</p>
                </Link>
                <div className="inline-block cursor-pointer" onClick={() => signOut()}>Logout</div>
            </>
            ) : (
            <>
                <div className="inline-block cursor-pointer" onClick={() => signIn()}>Login</div>
            </>
            )}
        </>
    )
}