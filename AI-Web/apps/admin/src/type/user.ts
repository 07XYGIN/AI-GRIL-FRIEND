export interface User{
    username: string;
    password: string;
    age: number;
    sex?: 0 | 1,
    email: string;
}

export interface RegisterForm {
    username: string
    password: string
    age: number
    email: string,
    sex?: 0 | 1,
}
