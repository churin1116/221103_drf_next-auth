import '../styles/globals.css'
import { SessionProvider } from 'next-auth/react'
import StateContextProvider from '../context/StateContext'

function MyApp({ Component, pageProps: { session, ...pageProps } }) {
  return (
    <SessionProvider session={session}>
      <StateContextProvider>
        <Component {...pageProps} />
      </StateContextProvider>
    </SessionProvider>
  )
}

export default MyApp