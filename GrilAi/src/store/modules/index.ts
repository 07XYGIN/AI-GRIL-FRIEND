import { defineStore } from 'pinia';
import { reactive, ref } from 'vue';
import { getUserInfo } from '@/api/user';
const useUserStore = defineStore(
  'user',
  () => {
    const code = ref<string>('');
    const userinfo = reactive({
      createTime: undefined,
      userId: undefined,
      userName: undefined,
    });
    const setCode = (co: string) => {
      code.value = co;
    };
    const getCode = () => {
      return code.value;
    };
    const getUserId = ()=>{
      return userinfo.userId;
    }
    const UserInfo = async () => {
      const { data } = await getUserInfo();
      userinfo.createTime = data.createTime;
      userinfo.userId = data.userId;
      userinfo.userName = data.userName;
    };
    return {
      code,
      userinfo,
      setCode,
      getCode,
      UserInfo,
      getUserId
    };
  },
  {
    persist: true,
  }
);

export default useUserStore;
