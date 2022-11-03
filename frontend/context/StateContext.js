import { createContext, useState } from 'react';

export const UserContext = createContext();
export const DataContext = createContext();

export default function StateContextProvider(props) {
    const [user, setUser] = useState({ username:'1' });
    const [data, setData] = useState({ index: 0, phase: 0 });
    
    return (
        <UserContext.Provider value={{ user, setUser }}>
            <DataContext.Provider value={{ data, setData }}>
                {props.children}
            </DataContext.Provider>
        </UserContext.Provider>
    );
}