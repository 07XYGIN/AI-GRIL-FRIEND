import request from '@/utils/request';
export interface registerForm {
  userName: string | undefined;
  password: string;
  newPassword: string | undefined;
  code?: string;
}

export interface loginForm {
  userName: string | undefined;
  password: string | undefined;
  code?: string | undefined;
}

export const register = (register: registerForm) => {
  return request({
    url: 'api/register',
    method: 'POST',
    data: register,
  });
};

export const login = (login: loginForm) => {
  return request({
    url: 'api/login',
    method: 'POST',
    data: login,
  });
};
