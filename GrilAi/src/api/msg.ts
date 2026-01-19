import request from '@/utils/request';

export const sendMsg = (msg: object) => {
  return request({
    url: '/msg/send',
    method: 'post',
    data: msg,
  });
};
export const getMsgList = (id: string) => {
  return request({
    url: `/api/history/${id}`,
    method: 'get',
  });
};
export const delMsgList = (id: string) => {
  return request({
    url: `/api/history/${id}`,
    method: 'delete',
  });
};
